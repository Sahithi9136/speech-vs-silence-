
import webrtcvad
import numpy as np
from .config import SAMPLE_RATE, FRAME_MS, VAD_MODE, SPEECH_THRESHOLD

def detect_speech(audio):
    vad = webrtcvad.Vad(VAD_MODE)
    frame_size = int(SAMPLE_RATE * FRAME_MS / 1000)

    speech_frames = 0
    total_frames = 0

    audio = np.asarray(audio, dtype=np.int16)

    for i in range(0, len(audio) - frame_size, frame_size):
        frame = audio[i:i+frame_size]
        total_frames += 1
        if vad.is_speech(frame.tobytes(), SAMPLE_RATE):
            speech_frames += 1

    ratio = speech_frames / max(total_frames, 1)

    return {
        "speech_detected": ratio >= SPEECH_THRESHOLD,
        "speech_ratio": round(ratio, 3),
        "speech_frames": speech_frames,
        "total_frames": total_frames
    }
