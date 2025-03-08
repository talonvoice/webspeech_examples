# see the list at the top of webspeech.py
# e.g. "english mode" or "german mode"

{user.webspeech_language} mode:
    mode.disable("command")
    mode.enable("dictation")
    mode.enable("user.{webspeech_language}")
