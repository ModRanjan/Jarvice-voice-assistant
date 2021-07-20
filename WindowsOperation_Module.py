import os
import subprocess
import time

def restart():
    subprocess.call(["shutdown", "/r"])
def shutdown():
    subprocess.call(["shutdown", "/s"])

def hibernate():
    subprocess.call(["shutdown", "/h"])


def logoff_or_signoff():
    time.sleep(5)
    subprocess.call(["shutdown", "/l"])

