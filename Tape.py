class Tape:

	def __init__(self, inputstring, settings):
		"""
		Sets up the initial state of tape
		"""
		self.padding_amount = 1
		self.settings = settings
		inputlist = self.parse_inputstring(inputstring)
		self.input = inputlist
		self.output = inputlist
		self.position = self.first_nonblank()


	def parse_inputstring(self, inputstring):
		"""
		Parsing the comma separated input string and
		adds padding to both sides
		"""
		inputlist = inputstring.split(",")
		if inputlist == [""]:
			inputlist = []
		padding = [self.settings["blank_character"]]*self.padding_amount
		return padding + inputlist + padding

	def to_set(self):
		"""
		Returns the input string as a set
		"""
		return set(self.input)


	def first_nonblank(self):
		"""
		Finds the first character in tape (from left) that isn't blank
		"""
		return self.padding_amount
		# for position, char in enumerate(self.input):
		# 	if char in self.settings["input_alphabet"]:
		# 		return position


	def forbidden_characters(self):
		"""
		Returns a set of forbidden characters
		"""
		return (self.to_set() - self.settings["tape_alphabet"]) - set([''])


	def write(self, character):
		"""
		Writes the input character at current position on tape
		"""
		self.output[self.position] = character

	def read(self):
		"""
		Returns the character from current tape position
		"""
		return self.output[self.position]


	def move(self, direction):
		"""
		Moves tape left/right
		"""
		if direction is "R":
			self.position += 1
		elif direction is "L":
			self.position -= 1

		if self.position < 0:
			self.output = [self.settings["blank_character"]] + self.output
			self.position = 0
		elif self.position > len(self.output) - 1:
			self.output += [self.settings["blank_character"]]
			self.position = len(self.output) - 1
