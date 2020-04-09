# import sys
from edit_dbs import *
# import speech_recognition as sr
# from pynput.keyboard import Key, Controller
from interfacing import *



# will eventually pass in type of editor preferences
def edit_mode_main():
    # handle arguments?
    print("Entered Edit Mode")
    send_keystrokes("esc", True)
    while True:
        command = recognize_commands(edit_db)
        print(command, "(edit_mode_main)")

    return 0
