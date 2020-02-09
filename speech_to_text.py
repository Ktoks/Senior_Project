import sys
import os
import subprocess
from language_specific_dbs import *
from pynput.keyboard import Key, Controller
# from mycroft_reference import DeepSpeechSTT as ds

# will probably be replaced by microft
import speech_recognition as sr
#####

import time

# called inside of recognize_my_voice only
def send_keystrokes(voice_input):
    keyboard = Controller()

    for char in voice_input:
        # time.sleep(.1)
        keyboard.press(char)
        keyboard.release(char)

# converts text list to string while mapping to pythonic words
def get_mapped_strings(text_list):
    sending_string = ""

    # single string
    if len(text_list) == 1:
        try:
            sending_string = python_db[text_list[0].lower()]
        except:
            sending_string = text_list[0]
        return sending_string

    # plural strings
    for item in text_list.split():
        temp_string = ""
        try:
            temp_string = python_db[item.lower()]
        except:
            temp_string = item
        sending_string += temp_string + " "
    return sending_string.strip()
    

def recognize_my_voice(language_choice):
    r = sr.Recognizer()

    # initializing our source as a microphone
    # with sr.Microphone(device_index=1) as source:
    with sr.Microphone() as source:
        # # may or may not need the following: 
        r.adjust_for_ambient_noise(source)

        # where prewhile was
        while True:
            audio = r.listen(source)

            try:
                # text_list = r.recognize_google(audio, language="en-US")
                text_list = r.recognize_sphinx(audio, language="en-US")
                
                sending_string = get_mapped_strings(text_list)

                send_keystrokes(sending_string)
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

# when listening, hey sae command spoken- begin listening for commands

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

    while True:

        if open_editor(editor_choice, file_or_folder):

            try:
                recognize_my_voice(selection)
            except:
                # selection = input("Please try again" + selection_menu())
                print("\nExiting SAE")
        else:
            print("Could not open that editor... Sorry ")


if __name__ == '__main__':
    main(sys.argv)
