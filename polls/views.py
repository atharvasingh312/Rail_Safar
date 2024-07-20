from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import speech_recognition as sr
from .rec_to_tran import record_audio, transcribe_speech
from .speaking import speak_tex
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
from gtts import gTTS
import os
import pygame


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\ABHISHEK SINGH\Desktop\SIH\Rail_Safar\arctic-window-399718-fa60c692e358.json"

@csrf_exempt
def record_and_transcribe(request):
    output_filename = r'C:\Users\ABHISHEK SINGH\Desktop\SIH\Rail_Safar\polls\op.wav'
    record_duration = 5

    # Record audio from the microphone
    record_audio(output_filename, duration=record_duration)
    
    # Get the selected language from the POST data
    target_language = request.POST.get('target')
    # print(target_language)
    # Transcribe the recorded audio to the selected language
    transcribe_text = transcribe_speech(output_filename,target_language)

    response_data = {
        'transcribed_text': transcribe_text,
    }

    return JsonResponse(response_data)

@csrf_exempt
def speak_text(request):
    if request.method == 'POST':
        target_language = request.POST.get('target')
        text = request.POST.get('text_data')
        speak_tex(text, target_language)  # Call speak_text with both text and target_language
        return HttpResponse("Text spoken.")
    else:
        return HttpResponse("Invalid Request")

def index(request):
    return render(request,'index.html')

def user(request):
    return render(request,'user.html')

def admin(request):
    return render(request,'admin.html')

def speech_to_text(request):
    if request.method == 'POST':
        try:
            audio_data = request.body
            r = sr.Recognizer()
            with sr.AudioData(audio_data) as source:
                audio = r.record(source)
                text = r.recognize_google(audio)
                return JsonResponse({'text': text})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'})
