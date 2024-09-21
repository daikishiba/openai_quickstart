from openai import OpenAI
from pathlib import Path
# 音声を再生
import playsound

client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"

text_input = input(("Enter the text you want to convert to speech: "))

response = client.audio.speech.create(
	model='tts-1',
	voice='alloy',
	input=text_input
)

with open(speech_file_path, 'wb') as audio_file:
    for chunk in response.iter_bytes():
        audio_file.write(chunk)

playsound.playsound(speech_file_path)