from Assistant_Details_Module import name
from Database_Module import speak_is_on,get_assistant_name
from Speak_Module import speak
def output(o):
    name=get_assistant_name()
    if speak_is_on():
        speak(o)

