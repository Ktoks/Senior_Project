from language_specific_dbs import *
from myHotwords import *


def convert_list_of_chars_to_list_of_strings(text_list):
	converted_strings = []
	some_word = ""
	for i in range(len(text_list)):
		if text_list[i] == ' ':
			converted_strings.append(some_word)
			some_word = ""
			continue
		else:
			some_word += text_list[i]
			continue
	if len(some_word) > 0:
		converted_strings.append(some_word)

	# print(converted_strings)
	return converted_strings
# print(convert_list_of_chars_to_list_of_strings(['h','e','l','l','o',' ','w','o','r','l','d']) ==["hello", "world"])
# print(convert_list_of_chars_to_list_of_strings(['h','e','l','l','o',' ','w','o','r','l','d',' ','h','o','w',' ','a','r','e',' ','y','o','u','?']) ==["hello", "world", "how", "are", "you?"])
# note: punctuation is added onto the end of the previous string


def handle_hotwords(hotword_db, word, lang_mode):
	try:
		temp_sending_string = hotword_db[word.lower()]
		print(temp_sending_string, "matched(handle_hotwords)")
		if lang_mode:
			return temp_sending_string + ' '
		return temp_sending_string
	except:
		if lang_mode:
			print("no matching hotword:", word, "(handle_hotwords)")
			return word + ' '
		return ""


def check_for_command_hotwords(text_list, command_db):
	sending_string = ""
	# for word in text_list:
	sending_string += handle_hotwords(command_db, text_list, False)
	return sending_string


def check_for_language_hotwords(text_list, language_choice):
	possible_command = check_for_command_hotwords(text_list, Commands)
	if len(possible_command) != 0:
		return possible_command
	sending_string = ""
	if language_choice == 0:
		lang_commands = python_db   # change later???
	if language_choice == 1:
		lang_commands = cpp_db
	for word in text_list:
		sending_string += handle_hotwords(lang_commands, word, True)
	return sending_string.strip()
