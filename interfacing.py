import speech_recognition as sr
from tools import *
from pynput.keyboard import Key, Controller

# called inside of recognize_my_voice only
def control_plus_key(keyboard,key_pressed):
	with keyboard.pressed(Key.ctrl):
		keyboard.press(key_pressed)

def send_keystrokes(voice_input, editMode):
	keyboard = Controller()
	if editMode:
		if voice_input == "copy":
			control_plus_key('y')
		elif voice_input == "paste":
			control_plus_key('p')
	if voice_input == "esc" or voice_input == "escape":
		print("escape reached(send_keystrokes)")
		keyboard.press(Key.esc)
		keyboard.release(Key.esc)
		return 0

	elif voice_input == "enter":
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		return 0
	for char in voice_input:
		# time.sleep(.1)
		keyboard.press(char)
		keyboard.release(char)

	# elif command == "delete":
	#     print("Need to implement deleting the currently highlighted section")
	# elif command == "highlight":
	#     print("Need to implement highlighting text on the document")
	# elif command == "escape":
	#     send_keystrokes('\esc')
	# elif command == "enter":
	#     send_keystrokes('enter')


def get_language_choice(menu):
	print(menu)
	choice = ""
	r = sr.Recognizer()
	# with sr.Microphone(device_index=1) as source:
	with sr.Microphone() as source:

		r.adjust_for_ambient_noise(source)
		while choice != 0 or choice != 1:
			audio = r.listen(source)
			print("listening(get_language_choice)")
			try:
				# choice = r.recognize_google(audio, language="en-US")
				temp_choice = r.recognize_sphinx(audio, language="en-US")
				choice = temp_choice[0]
			except:
				print("Please choose one: " + "\n" + menu)
		return choice

# this is only reached if hey sae is said


def recognize_commands(command_db):
	r = sr.Recognizer()
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		for _ in range(3):
			audio = r.listen(source)
			try:
				text_list = r.recognize_google(audio, language="en-US")
				# text_list = r.recognize_sphinx(audio, language="en-US")
				text_list = convert_list_of_chars_to_list_of_strings(text_list)

				tempcommand = check_for_command_hotwords(text_list, command_db)
				print(tempcommand, "read from hotwords(recognize_commands)")

				return tempcommand
			except:
				print("Sorry, could not recognize your voice (recognize_commands)")


def recognize_my_voice(language_choice):
	r = sr.Recognizer()
	# with sr.Microphone(device_index=1) as source:
	with sr.Microphone() as source:
		# may or may not need the following:
		r.adjust_for_ambient_noise(source)
		while True:
			audio = r.listen(source)
			print("listening(recognize_my_voice)")
			try:
				text_list = r.recognize_google(audio, language="en-US")
				# text_list = r.recognize_sphinx(audio, language="en-US")
				text_list = convert_list_of_chars_to_list_of_strings(text_list)
				# print("text list first word:", text_list[0], "second:",text_list[1],"(recognize_my_voice)")
				command = check_for_language_hotwords(
					text_list, language_choice)
				if command in Commands:
					return command
				else:
					print("Output " + command + "(recognize_my_voice)")
					send_keystrokes(command, False)
			except:
				print("Sorry, didn't understand you.(recognize_my_voice)")
