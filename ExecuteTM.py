from Tape import Tape

log = lambda *x: x

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

		self.tape_amount = int(settings_list[0])

		self.settings = {
			"amount_tapes":		int(settings_list[0]),
			"amount_states":	int(settings_list[1]),
			"input_alphabet":	set(settings_list[2].split(",")),
			"tape_alphabet":	set(settings_list[3].split(",")),
			"blank_character":	settings_list[4],
			"accepted_states":	set(settings_list[5].split(";")[0].split(","))
		}

		for instruction in instructions:
			state, task = instruction.split(">")
			self.instructions[tuple(state.split(","))] = task.replace("\n", "").split(",")

		log("Settings:", self.settings)
		log("Instructions:", self.instructions)


	def get_general_state(self, tapes):
		"""
		Returns the current tape state combined with the readhead state,
		depending on the amount of tapes being used

		@param list tapes
		@return tuple tape state
		"""
		tape_states = []
		for tape in tapes:
			tape_states.append(list(tape.output))
			tape_states.append(tape.position)

		return tuple(tape_states + [self.state])


	def exec_TM(self, inputstrings):
		"""
		Executing the instruction previously parsed on the inputstring(s)

		@param str inputstrings separated with # for multiple tapes
		"""
		self._steps = []
		tapes = [Tape(inputstrings, self.settings)]
		for i in range(self.tape_amount-1):
			tapes.append(Tape("", self.settings))

		if any([tape.forbidden_characters() for tape in tapes]):
			raise Exception("Forbidden characters in tape:", [tape.forbidden_characters() for tape in tapes])

		# initial setup
		self.state = "q0"
		terminated = False

		while not terminated:

			for t in tapes:
				log("Tape:", t.output)

			# save old values for later comparison
			step = self.get_general_state(tapes)
			self._steps.append(step)
			instruction_key = tuple([self.state] + [t.read() for t in tapes])
			log("instruction_key", instruction_key)

			if instruction_key in self.instructions:
				if self.state[1:] in self.settings["accepted_states"]:
					log("Accepted state '{}' reached".format(self.state))
					terminated = True
				log("instruction", self.instructions[instruction_key])

				# perform tasks on all tapes
				instructions = list(self.instructions[instruction_key])
				self.state = instructions.pop(0)
				half = len(instructions)//2
				for i in range(half):
					log("instr", instructions[i], instructions[i+half])
					tapes[i].write(instructions[i])
					tapes[i].move(instructions[i+half])

				if step == self.get_general_state(tapes):
					log("Tape values, position and state hasn't changed")
					terminated = True
			else:
				log("Instruction not found for tape")
				terminated = True


		log("ALL TERMINATED!")
		for i, tape in enumerate(tapes):
			log("Summary:")
			log("Tape:    ", i)
			log("Input:   ", tape.input)
			log("Output:  ", tape.output)
			log("State:   ", self.state)
			log("Position ", tape.position)
			log("Character", tape.read())
			log("-"*20)


	def get_steps(self, i = 0):
		"""
		After the Turing Machine is executed, this function will return
		a list with all steps taken during the execution
		@return list self._steps with tuples (tape state, head position, head state)
		"""
		log("get_steps for tape", i)
		return self._steps


# Tests
if __name__ == '__main__':
	log = print

	tm = ExecuteTM()

	# tm._parse_file("tapes/Folgen.txt")
	# tm.exec_TM("1,1,0A1,0,1,0")
	#tm.exec_TM("1,0,1A0,1,0")
	# tm._parse_file("tapes/bsp.txt")
	# tm.exec_TM("1,1,1,1,1")
	# tm._parse_file("tapes/col.txt")
	# tm.exec_TM('1,1')

	tm._parse_file("tapes/col.txt")
	tm.exec_TM("1,1,1,1,1,1,1,1")

	# tm._parse_file("tapes/tmasch.txt")
	# tm.exec_TM("0")
	for i in range(tm.tape_amount):
		log(tm.get_steps(i))

	# tm._parse_file("tapes/finde_eins.txt")
	# tm.exec_TM("1,1,0,0,1,0,1,0,0,1,0,1,0,1,1,0,1,0,0,0,1,0,1,0,1")
	# log("Steps taken", tm.get_steps())
