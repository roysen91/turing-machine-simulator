from Tape import Tape
from ExecuteTM import ExecuteTM
from VisualTM import VisualTM
import unittest

class TestCollatz(unittest.TestCase):
	"""
	Running tests on ExecuteTM
	"""
	def setUp(self):
		self.tm = ExecuteTM()
		self.tm._parse_file("tapes/col.txt")
		self.tm.exec_TM("1,1,1")

	def test_after_parse_bsp(self):
		self.assertEqual(self.tm.settings["amount_tapes"], 1)
		self.assertEqual(self.tm.settings["amount_states"], 18)
		self.assertEqual(self.tm.settings["input_alphabet"], set("01"))
		self.assertEqual(self.tm.settings["tape_alphabet"], set("01B"))
		self.assertEqual(self.tm.settings["blank_character"], "B")
		self.assertEqual(self.tm.settings["accepted_states"], {'17'})
		
	def test_output(self):
		self.assertEqual(self.tm.get_steps()[-1][2], "q17")
		
class TestFolgen(unittest.TestCase):
	"""
	Running tests on ExecuteTM
	"""
	def setUp(self):
		self.tm = ExecuteTM()
		self.tm._parse_file("tapes/Folgen.txt")
		self.tm.exec_TM("1,1,0,A,0,1,1,1,0")

	def test_after_parse_bsp(self):
		self.tm._parse_file("tapes/bsp.txt")
		self.assertEqual(self.tm.settings["amount_tapes"], 1)
		self.assertEqual(self.tm.settings["amount_states"], 4)
		self.assertEqual(self.tm.settings["input_alphabet"], set("01"))
		self.assertEqual(self.tm.settings["tape_alphabet"], set("01B"))
		self.assertEqual(self.tm.settings["blank_character"], "B")
		print(self.tm.settings["accepted_states"])
		self.assertEqual(self.tm.settings["accepted_states"], {'3'})
	def test_output(self):
		self.assertEqual(self.tm.get_steps()[-1][2], "q3")



if __name__ == "__main__":
	unittest.main()
