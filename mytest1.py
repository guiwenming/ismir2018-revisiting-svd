
import librosa
import numpy as np

# SR = 22050
# y, _ = librosa.load('E:/GwmDoc/MusicData/jamendo/train/01 - 10min.mp3', sr=SR)
# print(SR)

label = np.zeros((10,))
end = np.array([10],dtype=int)
label[:end] = 8
