import argparse
import os
import pyaudio
import wave
from google.cloud import speech_v1p1beta1 as speech
from google.oauth2 import service_account
from googletrans import Translator  # Import the Translator class from googletrans library

def record_audio(filename, duration=5, sample_rate=16000, channels=1):
    audio = pyaudio.PyAudio()

    # Set up the audio stream
    stream = audio.open(format=pyaudio.paInt16,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=1024)
    frames = []
    # Record audio for the specified duration
    print("Recording")
    for _ in range(0, int(sample_rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)
    print("Finished recording.")
    # Stop and close the audio stream
    stream.stop_stream()
    stream.close()
    # Terminate the PyAudio object
    audio.terminate()
    # Save the recorded audio to a WAV file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

def transcribe_speech(input_file, target_language):
    # Replace with the path to your service account JSON key file
    credentials_path = r"C:\Users\ABHISHEK SINGH\Desktop\SIH\Rail_Safar\arctic-window-399718-fa60c692e358.json"
    # Initialize the Google Cloud Speech-to-Text client
    credentials = service_account.Credentials.from_service_account_file(
        credentials_path, scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    # print(input_file)
    client = speech.SpeechClient(credentials=credentials)
    # Configure the recognition request
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code=target_language,
    )
    with open(input_file, 'rb') as audio_file:
        content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)
    # Perform speech recognition
    response = client.recognize(config=config, audio=audio)
    # Extract and return the transcribed text in Hindi
    transcribed_text = ""
    for result in response.results:
        transcribed_text += result.alternatives[0].transcript
    print(transcribed_text)
    return transcribed_text


# TEST

# if __name__ == "__main__":
#     output_filename = r'C:\Users\ABHISHEK SINGH\Desktop\chatbot_test\chatbot_test\output_audio.wav'
#     record_duration = 5
#     # Record audio from the microphone
#     record_audio(output_filename, duration=record_duration)
#     print(f"Audio recorded and saved to {output_filename}")
#     # Transcribe the recorded audio to Hindi text
#     transcribe_text = transcribe_speech(output_filename)
#     print("Transcribed text")
#     print(transcribe_text)
