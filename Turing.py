from ExecuteTM import ExecuteTM
from VisualTM import VisualTM
import os
import sys

"""
A couple of test cases
python3 Turing.py col 0,1,0 collatz gnome-open
python3 Turing.py col 1,1 collatz gnome-open
python3 Turing.py Folgen 1,1,0#0,1,1,1,0 folgen gnome-open
python3 Turing.py Folgen 1,0,1#0,1,0 folgen gnome-open

"""


class Turing:
	"""
	This class executes the Turing machine and build a visualized pdf
	from the command line, like so:
	`python3 Turing.py <tm txt file name> <comma separated inputstring> <output filename without ending> <open command>`
	"""
	def __init__(self, turing_machine, inputstrings = "", filename = "tm", viewername = None):

		turing_machine += ".txt" if turing_machine[-4:] != ".txt" else ""

		if not os.path.isfile("tapes/{}".format(turing_machine)):
			raise Exception("No such Turing machine:", "tapes/{}".format(turing_machine))

		self.output_file(turing_machine, inputstrings, filename, viewername)

	def output_file(self, turing_machine, inputstrings, filename, viewername = None):

		print("Executing", "tapes/{}".format(turing_machine))
		print("With inputstring(s)", inputstrings)
		print("Opening with", viewername)
		tm = ExecuteTM()
		tm._parse_file("tapes/{}".format(turing_machine))
		tm.exec_TM(inputstrings)
		vis = VisualTM()
		vis.write_file(tm.get_steps(), filename)

		files_to_remove = ["tex", "snm", "nav", "aux", "toc", "log", "out"]

		print("Cleaning up...")
		for file_ending in files_to_remove:
			if os.path.isfile("./{}.{}".format(filename, file_ending)):
				print("Deleting", "{}.{}".format(filename, file_ending))
				os.remove("./{}.{}".format(filename, file_ending))

		if viewername:
			vis.set_viewer(viewername)

		vis.visualize()


Turing(*sys.argv[1:])