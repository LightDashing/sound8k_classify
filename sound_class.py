from tensorflow.keras.models import load_model
import librosa
import numpy as np
import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"


def audio_read(file, sr=22050) -> np.ndarray:
    """Loads audio using librosa and return mfcc array, shaped (1, 20, 5)"""
    y, sample_rate = librosa.load(file, sr=sr)
    mfcc = np.mean(librosa.feature.mfcc(y, sample_rate, n_mfcc=100).T, axis=0).reshape((1, 20, 5))
    return mfcc


class Model:

    def __init__(self):
        self.model = load_model("model.hdf5", compile=False)
        self.classes = {1: "Гудок автомобиля", 2: "Дети", 3: "лай собаки", 4: "дрель", 5: "Двигатель",
                        6: "Выстрел", 7: "Отбойный молоток", 8: "Сирена", 9: "Музыка на улице", 0: "Кондиционер"}

    def predict(self, mfcc: np.ndarray) -> str:
        """Predicts audio class using numpy array shaped (1, 20, 5) with mfcc of audio"""
        predict = np.argmax(self.model.predict(mfcc), axis=1)
        return self.classes[predict[0]]

    def load_predict(self, file, sr=22050) -> str:
        """Loads audio using librosa and then predicts it's class"""
        audio = audio_read(file, sr)
        predicts = self.predict(audio)
        return predicts

