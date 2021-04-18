# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simpleui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(360, 303)
        self.actionSave_as_txt = QAction(MainWindow)
        self.actionSave_as_txt.setObjectName(u"actionSave_as_txt")
        font = QFont()
        font.setFamily(u"Segoe UI")
        self.actionSave_as_txt.setFont(font)
        self.actionSave_as_csv = QAction(MainWindow)
        self.actionSave_as_csv.setObjectName(u"actionSave_as_csv")
        self.actionSave_as_csv.setFont(font)
        self.actionLoad_csv = QAction(MainWindow)
        self.actionLoad_csv.setObjectName(u"actionLoad_csv")
        self.actionLoad_csv.setFont(font)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionExit.setFont(font)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.linePath = QLineEdit(self.centralwidget)
        self.linePath.setObjectName(u"linePath")
        self.linePath.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.linePath, 1, 0, 1, 1)

        self.predictButt = QPushButton(self.centralwidget)
        self.predictButt.setObjectName(u"predictButt")
        self.predictButt.setFont(font)

        self.gridLayout.addWidget(self.predictButt, 5, 0, 1, 1)

        self.openFile = QPushButton(self.centralwidget)
        self.openFile.setObjectName(u"openFile")
        self.openFile.setFont(font)

        self.gridLayout.addWidget(self.openFile, 3, 0, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMaximumSize(QSize(16777215, 12))
        font1 = QFont()
        font1.setPointSize(8)
        self.progressBar.setFont(font1)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)

        self.gridLayout.addWidget(self.progressBar, 8, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 0, 1, 1)

        self.openFolder = QPushButton(self.centralwidget)
        self.openFolder.setObjectName(u"openFolder")
        self.openFolder.setFont(font)

        self.gridLayout.addWidget(self.openFolder, 4, 0, 1, 1)

        self.listView = QListWidget(self.centralwidget)
        self.listView.setObjectName(u"listView")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy1)
        self.listView.setMinimumSize(QSize(0, 0))
        self.listView.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.listView, 1, 1, 7, 1)

        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnMinimumWidth(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 360, 21))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSave_as_txt)
        self.menuFile.addAction(self.actionSave_as_csv)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLoad_csv)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sound Classification", None))
        self.actionSave_as_txt.setText(QCoreApplication.translate("MainWindow", u"Save as txt", None))
        self.actionSave_as_csv.setText(QCoreApplication.translate("MainWindow", u"Save as csv", None))
        self.actionLoad_csv.setText(QCoreApplication.translate("MainWindow", u"Load csv", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(tooltip)
        self.linePath.setToolTip(QCoreApplication.translate("MainWindow", u"Path to folder or file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.predictButt.setToolTip(QCoreApplication.translate("MainWindow", u"Predict audio files classes", None))
#endif // QT_CONFIG(tooltip)
        self.predictButt.setText(QCoreApplication.translate("MainWindow", u"Predict", None))
#if QT_CONFIG(tooltip)
        self.openFile.setToolTip(QCoreApplication.translate("MainWindow", u"Open audio file", None))
#endif // QT_CONFIG(tooltip)
        self.openFile.setText(QCoreApplication.translate("MainWindow", u"File", None))
#if QT_CONFIG(tooltip)
        self.openFolder.setToolTip(QCoreApplication.translate("MainWindow", u"Open folder with only audio files", None))
#endif // QT_CONFIG(tooltip)
        self.openFolder.setText(QCoreApplication.translate("MainWindow", u"Folder", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

