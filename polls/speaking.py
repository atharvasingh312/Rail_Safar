
import os
from google.cloud import translate_v2 as translate
from gtts import gTTS
import pygame

# Set Google Cloud credentials environment variable
# "D:\arctic-window-399718-fa60c692e358.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\ABHISHEK SINGH\Desktop\chatbot_test\chatbot_test\arctic-window-399718-fa60c692e358.json"

def speak_tex(text, target_language):
    # Translate the text to the target language
    # translated_text = translate_text(text, target_language)

    # Convert text to speech

    tts = gTTS(text, lang=target_language)

    # Save the speech to a temporary file
    tts.save(r"C:\Users\ABHISHEK SINGH\Desktop\SIH\Rail_Safar\polls\temp.mp3")
    
    # Play the speech
    pygame.mixer.init()
    pygame.mixer.music.load(r"C:\Users\ABHISHEK SINGH\Desktop\SIH\Rail_Safar\polls\temp.mp3")
    pygame.mixer.music.play()
    # Wait for the music to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Adjust the tick rate as needed

    # Close the mixer to release the file
    pygame.mixer.quit()
