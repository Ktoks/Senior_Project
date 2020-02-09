from unittest.mock import patch
import unittest

import speech_to_text

class TestSae(unittest.TestCase):

    def test01_send_keystrokes_exists(self):
        self.assertTrue('send_keystrokes' in dir(speech_to_text),
                "Function send_keystrokes is not in directory")

    
    def test01_get_mapped_strings(self):
        self.assertEqual("while True", speech_to_text.get_mapped_strings("while true"))

    def test02_get_mapped_strings(self):
        self.assertNotEqual("while true", speech_to_text.get_mapped_strings("while true"))


    def test01_recognize_my_voice(self):
        self.assertTrue('recognize_my_voice' in dir(speech_to_text),
                "Function recognize_my_voice is not in directory")

    def test01_selection_menu(self):
        self.assertEqual("\nWhich language would you like to test?\n'0' = Python 3(Not yet implemented\n'1' = C++(Not yet implemented)\n", speech_to_text.selection_menu())

    def test01_open_editor(self):
        self.assertTrue(speech_to_text.open_editor("null", "~"))

if __name__ == '__main__':
    unittest.main()