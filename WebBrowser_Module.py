import webbrowser
import os 
def open_facebook():
    webbrowser.open('www.facebook.com')
def open_google():
    webbrowser.open('www.google.com')

def close_browser():
    browserExe = "chrome.exe" 
    os.system("taskkill /f /im "+browserExe) 