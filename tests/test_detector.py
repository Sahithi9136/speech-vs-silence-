
from app.speech_detector import detect_speech
import numpy as np

audio = np.zeros(16000, dtype=np.int16)
print(detect_speech(audio))
