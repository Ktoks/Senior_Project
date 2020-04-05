import sys
import os
import subprocess
from language_specific_dbs import *
from myHotwords import *
from pynput.keyboard import Key, Controller
# from mycroft_reference import DeepSpeechSTT as ds

# will probably be replaced by microft
import speech_recognition as sr
#####

import time



# called inside of recognize_my_voice only
def send_keystrokes(voice_input):
    keyboard = Controller()

    # if voice_input == "esc":
    #     keyboard.esc
    # if voice_input == "enter":
    #     keyboard.enter

    for char in voice_input:
        # time.sleep(.1)
        keyboard.press(char)
        keyboard.release(char)

# converts text list to string while mapping to pythonic words
def get_mapped_strings(text_list):
    sending_string = ""

    if len(text_list) == 1:
        try:
            temp_sending_string = python_db[text_list[0].lower()]
            print(temp_sending_string,"temp string(get_mapped_strings)")
            sending_string = temp_sending_string
        except:
            sending_string = text_list[0]
        return sending_string

    for item in text_list:
        temp_string = ""
        try:
            temp_string = python_db[item.lower()]
        except:
            temp_string = item
        sending_string += temp_string
    return sending_string.strip()

def convert_list_of_chars_to_list_of_strings(text_list):
    converted_strings = []
    some_word = ""
    for i in range(len(text_list)):
        if text_list[i] == ' ':
            converted_strings.append(some_word)
            some_word = ""
            continue
            # if len(word_lengths) == 1:
            #     converted_strings = str(text_list[:i+1])
            # else:
            #     converted_strings += str(text_list[word_lengths[-1]:i])
            #     if i < len(text_list) - 1:
            #         converted_strings += ' '
        else:
            some_word += text_list[i]
            continue
    if len(some_word) > 0:
        converted_strings.append(some_word)

        
            

    # print(converted_strings)
    return converted_strings
# print(convert_list_of_chars_to_list_of_strings(['h','e','l','l','o',' ','w','o','r','l','d']) ==["hello", "world"])
# print(convert_list_of_chars_to_list_of_strings(['h','e','l','l','o']) == ["hello"])
# print(convert_list_of_chars_to_list_of_strings(['h','e','l','l','o',' ','w','o','r','l','d',' ','h','o','w',' ','a','r','e',' ','y','o','u','?']) ==["hello", "world", "how", "are", "you?"])
# note: punctuation is added onto the end of the previous string
    
def recognize_my_voice(language_choice):
    r = sr.Recognizer()

    # initializing our source as a microphone
    # with sr.Microphone(device_index=1) as source:
    with sr.Microphone() as source:
        # # may or may not need the following: 
        r.adjust_for_ambient_noise(source)
        command = ""
        index = 0
        while True:
            audio = r.listen(source)
            print("listening(recognize_my_voice)")
            try:
                text_list = r.recognize_google(audio, language="en-US")
                # text_list = r.recognize_sphinx(audio, language="en-US")
                text_list = convert_list_of_chars_to_list_of_strings(text_list)
                print("text list first word:", text_list[0], "second:",text_list[1],"(recognize_my_voice)")
                try:
                    tempcommand = checkForHotWords(text_list)
                    if tempcommand != "":
                        print("Good command: " + command)
                        command = tempcommand
                        break
                    print("Try again(recognize_my_voice)")
                    
                except: 

                    sending_string = get_mapped_strings(text_list) + " " # add python or c++ here?
                    index +=1
                    send_keystrokes(sending_string)
                    print(str(index) + "('th) keystroke sent(1st recognize_my_voice)")

            except:
                sending_string = get_mapped_strings(text_list) + " " # add python or c++ here?

                send_keystrokes(sending_string)
                index += 1
                print(str(index) + "('th) keystroke sent(2nd recognize_my_voice)")
        return command


def checkForHotWords(text_list):
    sending_string = ""

    if len(text_list) == 1:
        try:
            temp_sending_string = uCommands[text_list[0].lower()]
            print(temp_sending_string, "checkforhotwords1")
            sending_string = temp_sending_string
        except:
            print("no matching hotword")
            return ""

    if len(text_list) == 2:
        text_list = text_list.split()
        temp_string = ""
        try:
            temp_string = dCommands[text_list[0].lower() + " " + text_list[1].lower()]
            print(temp_string, "checkforhotwords2")
            sending_string = temp_string
        except:
            print("no matching hotwords")
            return ""
    return sending_string


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

def recognize_commands():   # this is only reached if hey sae is said
    r = sr.Recognizer()
    command = ""

    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source)

        while True:
            audio = r.listen(source)

            try:
                text_list = r.recognize_google(audio, language="en-US")
                # text_list = r.recognize_sphinx(audio, language="en-US")
                
                try:
                    tempcommand = checkForHotWords(text_list)
                    print(tempcommand, "read(recognize_commands)")
                    command = tempcommand
                    break
                except:
                    print("Please try a different command")
            except:
                print("Sorry, could not recognize your voice (recognize_commands)")
    return command

def execute_command(command):
    if len(command) == 1:
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
        elif command == "delete":
            print("Need to implement deleting the currently highlighted section")
        elif command == "highlight":
            print("Need to implement highlighting text on the document")
        elif command == "escape":
            send_keystrokes('\esc')
        elif command == "enter":
            send_keystrokes('\n')

# when listening, hey sae command spoken- begin listening for commands

# def main(argv):
def main():
    
    editor_choice = "code"
    file_or_folder = 'test.txt'

    # editor input to open the editor
    # if len(argv) > 1:
    #     editor_choice = argv[1]
    #     if len(argv) > 2:
    #         file_or_folder = argv[2]

    # selection = input(selection_menu()) # need to make this voice activated
    selection = 0


    while True:
        command = ""
        if open_editor(editor_choice, file_or_folder):

            try:
                temp_command = recognize_my_voice(selection)
                command = temp_command
            except:
                # selection = input("Please try again" + selection_menu())
                print("\nExiting SAE")
                sys.exit()
        else:
            print("Could not open that editor... Sorry ")
        if command != "":
            if command == "hey sae":
                command = recognize_commands()
            else:
                execute_command(command)
        else:
            print("Hey Sae was not in voice command.")



if __name__ == '__main__':
    main()
