from Tape import Tape

class ExecuteTM:
	"""
	Class for handling of reading Turing Machine instructions
	and executing them on any incoming tape(s)
	"""
	def __init__(self):
		"""
		Sets up the
		"""
		self.state = None
		self.settings = {}
		self.instructions = {}
		self.tape_amount = 0
		# used for visualisation @see get_steps()
		self._steps = []


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


	def exec_TM(self, inputstrings):
		"""
		Executing the instruction previously parsed on the inputstring(s)

		@param str inputstrings separated with | for multiple tapes
		"""
		inputstrings = inputstrings.split("|")
		self.tape_amount = len(inputstrings)
		self._steps = [[] for _ in range(self.tape_amount)]
		tapes = [Tape(inputstring, self.settings) for inputstring in inputstrings]

		if any([tape.forbidden_characters() for tape in tapes]):
			raise Exception("Forbidden characters in tape:", [tape.forbidden_characters() for tape in tapes])

		# initial setup
		self.state = ["q0"]*self.tape_amount
		terminated = [False]*self.tape_amount
		attempts = [0]*self.tape_amount # for testing purposes

		while not all(terminated):
			# save old values for later comparison
			for i, tape in enumerate(tapes):
				if terminated[i]: continue
				print("tape", i, tape.output)
				step = (tape.output, tape.position, self.state[i])
				self._steps[i].append(step)
				old_tape, old_position, old_state = step

				state = (self.state[i], tape.read())
				print("state      ", state, tape.position)

				if state in self.instructions:
					print("instruction", self.instructions[state])
					new_state, new_char, direction = self.instructions[state]
					self.state[i] = new_state
					tape.write(new_char)
					tape.move(direction)

					if new_state[1:] in self.settings["accepted_states"]:
						print("Accepted state '{}' reached for tape {}".format(new_state, i))
						terminated[i] = True
					elif old_tape == tape.output and old_position == tape.position and old_state == self.state[i]:
						print("Tape values, position and state hasn't changed for tape:", i)
						terminated[i] = True
				else:
					print("Instruction not found for tape", i)
					terminated[i] = True

				# temporarily avoiding infinite loops
				attempts[i] += 1
				if attempts[i] > 1000:
					print("Killed it, because doesn't stop! Tape:", i)
					terminated[i] = True


		print("ALL TERMINATED!")
		for i, tape in enumerate(tapes):
			print("Summary:")
			print("Tape:    ", i)
			print("Input:   ", tape.input)
			print("Output:  ", tape.output)
			print("State:   ", self.state)
			print("Position ", tape.position)
			print("Character", tape.read())
			print("-"*20)


	def get_steps(self, i = 0):
		"""
		After the Turing Machine is executed, this function will return
		a list with all steps taken during the execution
		@return list self._steps with tuples (tape state, head position, head state)
		"""
		print("get_steps for tape", i)
		return self._steps[i]


# Tests
if __name__ == '__main__':

	tm = ExecuteTM()

	tm._parse_file("tapes/bsp.txt")
	tm.exec_TM("BB11111BB|BB00011BB|BB00111BB|BB01111BB|B001111BB|BB011110B|BB01BBBBB")
	for i in range(tm.tape_amount):
		print(tm.get_steps(i))

	# tm._parse_file("tapes/finde_eins.txt")
	# tm.exec_TM("22110010100101011010001010122")
	# print("Steps taken", tm.get_steps())