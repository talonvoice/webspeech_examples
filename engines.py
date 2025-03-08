from talon import speech_system
from talon.engines.webspeech import WebSpeechEngine
webspeech = WebSpeechEngine()
speech_system.add_engine(webspeech)
