from Tape import Tape
from ExecuteTM import ExecuteTM
from VisualTM import VisualTM
import unittest

class Tests(unittest.TestCase):
	"""
	Running tests on ExecuteTM
	"""
	def setUp(self):
		print("setup")
		self.tm = ExecuteTM()

	def test_before_exec(self):
		self.assertEqual(self.tm.settings, {})
		self.assertEqual(self.tm.instructions, {})
		self.assertEqual(self.tm.tape_amount, 0)
		self.assertIsNone(self.tm.state)

	def test_after_parse_bsp(self):
		self.tm._parse_file("tapes/bsp.txt")
		self.assertEqual(self.tm.settings["amount_tapes"], 1)
		self.assertEqual(self.tm.settings["amount_states"], 4)
		self.assertEqual(self.tm.settings["input_alphabet"], set(["0","1"]))
		self.assertEqual(self.tm.settings["tape_alphabet"], set(["0","1","B"]))
		self.assertEqual(self.tm.settings["blank_character"],"B")
		self.assertEqual(self.tm.settings["accepted_states"], set())

		self.tm.exec_TM("BB11111BB")






if __name__ == "__main__":
	unittest.main()
