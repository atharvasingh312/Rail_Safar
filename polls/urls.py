
from . import views
# from django.conf.urls import url
from django.urls import path
urlpatterns = [
    path("", views.index, name="index"),
    path('user/', views.user, name='user'),
    path('admin/', views.admin, name='admin'),
    path('speech-to-text/',views.speech_to_text,name='speech_to_text'),
    path('record_and_transcribe/', views.record_and_transcribe, name='record_and_transcribe'),
    path('speak_text/', views.speak_text, name='speak_text'),
]
