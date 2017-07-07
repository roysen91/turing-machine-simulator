class Tape:

	def __init__(self, inputstring, settings):
		"""
		Sets up the initial state of tape
		"""
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
		padding = [self.settings["blank_character"]]*50
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
		for position, char in enumerate(self.input):
			if char in self.settings["input_alphabet"]:
				return position


	def forbidden_characters(self):
		"""
		Returns a set of forbidden characters
		"""
		return self.to_set() - self.settings["tape_alphabet"]


	def write(self, character):
		"""
		Writes the input character at current position on tape
		"""
		self.output[self.position] = character

	def read(self):
		"""
		Returns the character from current tape position
		"""
		print("position", self.position, self.output)
		return self.output[self.position]


	def move(self, direction):
		"""
		Moves tape left/right
		"""
		if direction is "R":
			self.position += 1
		elif direction is "L":
			self.position -= 1