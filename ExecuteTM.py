from Tape import Tape

class ExecuteTM:

	def __init__(self):
		self.state = None
		self.settings = {}
		self.instructions = {}
		# used for visualisation
		self.steps = []


	def _parse_file(self, filename):
		"""
		Parses a .txt file with Turing Machine instructions
		and settings
		"""
		with open(filename) as file:
			instructions = file.readlines()
			settings_list = instructions.pop(0).split("|")

		self.settings = {
			"amount_tapes":		int(settings_list[0]),
			"amount_states":	int(settings_list[1]),
			"input_alphabet":	set(settings_list[2].split(",")),
			"tape_alphabet":	set(settings_list[3].split(",")),
			"blank_character":	settings_list[4],
			"accepted_states":	set(settings_list[5].split(";")[0])
		}

		for instruction in instructions:
			state, task = instruction.split(">")
			self.instructions[tuple(state.split(","))] = task.replace("\n", "").split(",")



		print("Settings:", self.settings)
		print("Instructions:", self.instructions)



	def exec_TM(self, inputstring):
		"""
		Executing the instruction previously parsed on the inputstring
		"""
		tape = Tape(inputstring, self.settings) # TODO: make independent of amount of Tapes

		if tape.forbidden_characters():
			raise Exception("Forbidden characters in tape:", tape.forbidden_characters())

		# initial setup
		self.state = "q0"
		terminated = False
		i = 0 # for testing purposes

		while not terminated:
			# save old values for later comparison
			step = (tape.output, tape.position, self.state)
			self.steps.append(step)
			old_tape, old_position, old_state = step

			state = (self.state, tape.read())
			print("state      ", state, tape.position)

			if state in self.instructions:
				print("instruction", self.instructions[state])
				new_state, new_char, direction = self.instructions[state]
				self.state = new_state
				tape.write(new_char)
				tape.move(direction)

				if self.state[1:] in self.settings["accepted_states"]:
					print("Accepted state reached!", self.state)
					terminated = True
				elif old_tape == tape.output and old_position == tape.position and old_state == self.state:
					print("Tape values, position and state hasn't changed!")
					terminated = True
			else:
				print("Instruction not found!")
				terminated = True

			# temporarily avoiding infinite loops
			i += 1
			if i > 1000:
				terminated = True
				print("Killed it, because doesn't stop!")

		print("TERMINATED!")
		print("Input:   ", tape.input)
		print("Output:  ", tape.output)
		print("State:   ", self.state)
		print("Position ", tape.position)
		print("Character", tape.read())


# Tests
if __name__ == '__main__':

	tm = ExecuteTM()

	tm._parse_file("tapes/bsp.txt")
	tm.exec_TM("BB01111BB")
	print("Steps taken", tm.steps)

	# tm._parse_file("tapes/finde_eins.txt")
	# tm.exec_TM("22110010100101011010001010122")
	# print("Steps taken", tm.steps)