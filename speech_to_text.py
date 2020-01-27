import sys
import os
import subprocess
from pynput.keyboard import Key, Controller

# will probably be replaced by microft
import speech_recognition as sr
#####

import time


def send_keystrokes_to_document(voice_input):
    keyboard = Controller()

    for char in voice_input:
        time.sleep(.1)
        keyboard.press(char)
        keyboard.release(char)


def recognize_my_voice(language_choice):
    # initialize r to recognize our audio
    r = sr.Recognizer()

    # initializing our source as a microphone
    with sr.Microphone() as source:

        # will print to the screen
        print("Speak anything: ")
        # listen to the source and save it in audio
        audio = r.listen(source)
        text = "Not input"

        language_choice = None  # Not Implemented
        if language_choice == None:
            print("Language serving is not yet implemented.\n")

        while "the end" not in str(text) or KeyboardInterrupt:
            audio = r.listen(source)
            text = "Not input"

            try:
                # convert audio into text here-- try mycroft here?
                text = r.recognize_google(audio)
                # print out what it thinks you said
                print("Spoken: {}".format(text))
                send_keystrokes_to_document(str(text))
            except:
                print("Sorry, could not recognize your voice")


def selection_menu():
    return "\nWhich language would you like to test?\n'0' = Python 3(Not yet implemented\n'1' = C++(Not yet implemented)\n"


def open_editor(editor_choice, file_or_folder):
    try:
        if file_or_folder != "" or file_or_folder != None:
            file_or_folder = '.'
        # subprocess.Popen([editor_choice, file_or_folder])
        return True
    except Exception as e:
        print(str(e))
        return False

def main(argv):

    editor_choice = "code"
    file_or_folder = 'test.txt'

    # editor input to open the editor
    if len(argv) > 1:
        editor_choice = argv[1]
        if len(argv) > 2:
            file_or_folder = argv[2]

    # selection = input(selection_menu()) # need to make this voice activated
    selection = 0

    # if the editor opens
    if open_editor(editor_choice, file_or_folder):

        try:
            recognize_my_voice(selection)
        except:
            selection = input("Please try again" + selection_menu())
    else:
        print("Could not open that editor... Sorry ")


if __name__ == '__main__':
    main(sys.argv)
