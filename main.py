from soundui import Ui_MainWindow
from help import Ui_Help
from about import Ui_About
from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog, QListWidgetItem, QWidget, QDialog
from PySide2.QtCore import QCoreApplication
from sound_class import Model
import os
import sys


class HelpWindow(QDialog, Ui_Help):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.okButton.clicked.connect(self.close)
        self.show()


class AboutWindow(QDialog, Ui_About):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
        self.show()


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.progressBar.hide()
        self.openFile.clicked.connect(self.open_file)
        self.openFolder.clicked.connect(self.open_folder)
        self.predictButt.clicked.connect(self.predict)
        self.actionSave_as_csv.triggered.connect(self.save_csv)
        self.actionSave_as_txt.triggered.connect(self.save_txt)
        self.actionExit.triggered.connect(self.exit)
        self.actionLoad_csv.triggered.connect(self.load_csv)
        self.actionHelp.triggered.connect(self.help)
        self.actionAbout.triggered.connect(self.about)
        self.processQueue = []
        self.model = Model()

    def exit(self):
        self.close()
        sys.exit()

    def help(self):
        help_window = HelpWindow()
        help_window.exec_()
        help_window.deleteLater()

    def about(self):
        about_window = AboutWindow()
        about_window.exec_()
        about_window.deleteLater()

    def open_file(self):
        filename = QFileDialog.getOpenFileName(self, "Open audio file", filter="Audio files (*.wav *mp3 *flac *ogg)")
        self.linePath.setText(filename[0])

    def open_folder(self):
        folder_name = QFileDialog.getExistingDirectory(self, "Open directory with audio files")
        self.linePath.setText(folder_name)

    def list_add(self, predicts: list):
        for pred in predicts:
            item = QListWidgetItem()
            item.setText(f"{pred[0]} - {pred[1]}")
            self.listView.addItem(item)

    def save_csv(self):
        name = QFileDialog.getSaveFileName(self, "Save CSV", filter="CSV file (*.csv)")
        with open(name[0], "w", encoding='utf-8') as f:
            f.write(f"filename,class")
            for i in range(self.listView.count()):
                text = self.listView.item(i).text()
                f.write(f"\n{text[:text.find('-') - 1]},{text[text.rfind('-') + 2:]}")

    def load_csv(self):
        file_name = QFileDialog.getOpenFileName(self, "Open CSV file", filter="CSV text (*.csv)")
        with open(file_name[0], "r", encoding="utf-8") as f:
            fullpath = file_name[0]
            fullpath = fullpath[:fullpath.rfind("/")]
            self.linePath.setText(fullpath)
            firstline = f.readline()
            if firstline[:firstline.find(",")] == "filename":
                for line in f.readlines():
                    file = (fullpath + "/" + line[:line.find(",")], int(line[line.rfind(",") + 1:].strip("\n")))
                    self.processQueue.append(file)
            elif firstline[:firstline.find(",")] == "filename":
                for line in f.readlines():
                    file = (line[:line.find(",")], int(line[line.rfind(",") + 1:].strip("\n")))
                    self.processQueue.append(file)

    def save_txt(self):
        name = QFileDialog.getSaveFileName(self, "Save CSV", filter="TXT file (*.txt)")
        with open(name[0], "w", encoding='utf-8') as f:
            for i in range(self.listView.count()):
                text = self.listView.item(i).text()
                f.write(f"\n{text[:text.find('-') - 1]} - {text[text.rfind('-') + 2:]}")

    def predict(self):
        predicts = []
        path = self.linePath.text()
        if self.processQueue:
            self.listView.clear()
            self.progressBar.setVisible(True)
            self.progressBar.reset()
            self.progressBar.setMaximum(len(self.processQueue))
            self.progressBar.setMinimum(1)
            predicts = []
            for file in self.processQueue:
                preds = self.model.load_predict(file[0], file[1])
                predicts.append((file[0][file[0].rfind("/") + 1:], preds))
                self.progressBar.setValue(self.progressBar.value() + 1)
                QCoreApplication.processEvents()
            self.progressBar.hide()
            self.processQueue = []
        elif os.path.isdir(path):
            self.listView.clear()
            self.progressBar.setVisible(True)
            files = [name for name in os.listdir(path) if os.path.isfile(path + "/" + name)]
            self.progressBar.reset()
            self.progressBar.setMaximum(len(files))
            self.progressBar.setMinimum(1)
            predicts = []
            for file in files:
                preds = self.model.load_predict(f"{path}/{file}")
                predicts.append((file, preds))
                self.progressBar.setValue(self.progressBar.value() + 1)
                QCoreApplication.processEvents()
            self.progressBar.hide()
        elif os.path.isfile(path):
            self.listView.clear()
            predicts.append((path[path.rfind("/")+1:], self.model.load_predict(path)))
        self.list_add(predicts)


app = QApplication()
window = MainWindow()
window.show()
sys.exit(app.exec_())
