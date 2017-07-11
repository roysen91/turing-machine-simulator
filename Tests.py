from Tape import Tape
from ExecuteTM import ExecuteTM
from VisualTM import VisualTM
import unittest

class TestCollatzKorrekt(unittest.TestCase):
	"""
	Running tests on ExecuteTM
	"""
	def setUp(self):
		self.tm = ExecuteTM()
		self.tm._parse_file("tapes/col.txt")
		self.tm.exec_TM("1,1,1")

	def test_after_parse(self):
		self.assertEqual(self.tm.settings["amount_tapes"], 1)
		self.assertEqual(self.tm.settings["amount_states"], 18)
		self.assertEqual(self.tm.settings["input_alphabet"], set("01"))
		self.assertEqual(self.tm.settings["tape_alphabet"], set("01B"))
		self.assertEqual(self.tm.settings["blank_character"], "B")
		self.assertEqual(self.tm.settings["accepted_states"], {'17'})
		
	def test_output(self):
		self.assertEqual(self.tm.get_steps()[-1][-1], "q17")
		
class TestFolgenKorrekt(unittest.TestCase):
	"""
	Running tests on ExecuteTM
	"""
	def setUp(self):
		self.tm = ExecuteTM()
		self.tm._parse_file("tapes/Folgen.txt")
		self.tm.exec_TM("1,1,0,A,0,1,1,1,0")

	def test_after_parse(self):
		self.assertEqual(self.tm.settings["amount_tapes"], 2)
		self.assertEqual(self.tm.settings["amount_states"], 6)
		self.assertEqual(self.tm.settings["input_alphabet"], set("01A"))
		self.assertEqual(self.tm.settings["tape_alphabet"], set("01BA"))
		self.assertEqual(self.tm.settings["blank_character"], "B")
		self.assertEqual(self.tm.settings["accepted_states"], {'3'})
	def test_output(self):
		self.assertEqual(self.tm.get_steps()[-1][-1], "q3")

class TestFolgenFehler(unittest.TestCase):
	"""
	Running tests on ExecuteTM
	"""
	def setUp(self):
		self.tm = ExecuteTM()
		self.tm._parse_file("tapes/Folgen.txt")
		self.tm.exec_TM("1,1,1,A,0,1,0")

	def test_after_parse(self):
		self.assertEqual(self.tm.settings["amount_tapes"], 2)
		self.assertEqual(self.tm.settings["amount_states"], 6)
		self.assertEqual(self.tm.settings["input_alphabet"], set("01A"))
		self.assertEqual(self.tm.settings["tape_alphabet"], set("01BA"))
		self.assertEqual(self.tm.settings["blank_character"], "B")
		self.assertEqual(self.tm.settings["accepted_states"], {'3'})
	def test_output(self):
		self.assertEqual(self.tm.get_steps()[-1][-1], "q4")


if __name__ == "__main__":
	unittest.main()
