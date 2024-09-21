import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from openai import OpenAI
import os

client = OpenAI()

# 録音設定
duration = 5  # 5秒間録音
sample_rate = 44100  # サンプリングレート

print("Recording...")

# 音声を録音
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
sd.wait()  # 録音が終わるまで待機

# WAVファイルとして保存
output_filename = "output.wav"
wav.write(output_filename, sample_rate, audio_data)

print("Finished recording. Saved as output.wav")

# OpenAI Whisper APIを使用して音声をテキストに変換
with open(output_filename, "rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        model='whisper-1',
        file=audio_file
	)

# 結果を表示
print("Transcription: ", transcription.text)
