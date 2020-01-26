from pynput.keyboard import Key, Controller

# will probably be replaced by microft
import speech_recognition as sr
#####

import time

def recognize_my_voice():
    # initialize r to recognize our audio
    r = sr.Recognizer()

    # initializing our source as a microphone
    with sr.Microphone() as source:
        # will print to the screen
        print("Speak anything: ")
        # listen to the source and save it in audio
        audio = r.listen(source)
        
        try:
            # convert audio into text here-- try mycroft here?
            text = r.recognize_google(audio)
            # print out what it thinks you said
            print("You said: {}".format(text))
        except:
            print("Sorry, could not recognize your voice")



def send_keystrokes_to_document():
    keyboard = Controller()

    for char in "This is a sentence written in Python3!":
        time.sleep(.12)
        keyboard.press(char)
        keyboard.release(char)

def selection_menu():
    return "\nWhich part would you like to test?\n'0' = recognize_my_voice\n'1' = send_keystrokes_to_document"

def main():
    selection = input(selection_menu())
    try:
        choice = int(selection)
        if choice == 0:
            recognize_my_voice()
        elif choice == 1:
            send_keystrokes_to_document()
    except:
        selection = input("Please try again" + selection_menu())

if __name__ == '__main__':
    main()
