import sys
import os
import subprocess
from language_specific_dbs import *
from myHotwords import *
from interfacing import *
from tools import *
# from pynput.keyboard import Key, Controller
# from mycroft_reference import DeepSpeechSTT as ds
# will probably be replaced by microft
# import speech_recognition as sr
import time
from edit_mode import edit_mode_main

def handle_arguments():
    pass
    sys.argv
    editor_choice = "code"
    file_or_folder = 'test.txt'
    # editor input to open the editor
    # if len(argv) > 1:
    #     editor_choice = argv[1]
    #     if len(argv) > 2:
    #         file_or_folder = argv[2]

def selection_menu():
    return "\nWhich language would you like to test?\n'0' = Python 3\n'1' = C++\n"


# def open_editor(editor_choice, file_or_folder):
#     try:
#         if file_or_folder != "" or file_or_folder != None:
#             file_or_folder = '.'
#         # subprocess.Popen([editor_choice, file_or_folder])
#         return True
#     except Exception as e:
#         print(str(e))
#         return False

def execute_command(command):
    # keyboard = Controller()
    if command == "quit":
        sys.exit();
    elif command == "save":
        print("Need to implement saving the document")
    elif command == "close":
        print("Need to implement closing the current document")
    elif command == "new":
        print("Need to implement opening a new document")
    elif command == "open":
        print("Need to implement opening document")
    elif command == "edit mode":
        print("edit mode reached(execute_command)")
        edit_mode_main()

def main():
    handle_arguments()
    # selection = get_language_choice(selection_menu()) # need to make this voice activated
    selection = 0
    while True:
        command = recognize_my_voice(selection)
        print(command, "(main)")

        if command == "hey sae":
            command = recognize_commands()
        execute_command(command)


if __name__ == '__main__':
    main()
