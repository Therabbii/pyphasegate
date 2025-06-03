import encrypt_text
from unittest import TestCase

class TestEncryption(TestCase):

	def test_encrypt_function_exists(self):
		encrypt_text.get_encryption(ord)
	
	def test_input_is_in_strings(self):
		actual = " "
		expected = " "
		self.assertEqual(actual , expected)
	def test_each_letter_is_encrypted_to_the_thirteenth_character_after_it(self):
		actual = encrypt_text.get_encryption("Hello , World!")
		expected = "Uryyb , Jbeyq!"
		self.assertEqual(actual , expected)
