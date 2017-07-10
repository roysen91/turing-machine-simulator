
class Turmite:

	def __init__(self, tape):
		print("Initialized a {}-by-{} Turmite tape".format(len(tape[0]), len(tape)))
		self.state = "q0"
		self.tape = tape
		self.position = (0,0)

	def __str__(self):
		return "".join([" ".join([str(i) for i in row]) + "\n" for row in self.tape])

	def rotate_right(self):
		print("Rotate right")
		self.tape = [list(row)[::-1] for row in list(zip(*self.tape))]

	def rotate_left(self):
		print("Rotate left")
		self.tape = [list(row) for row in list(zip(*self.tape))[::-1]]

	def read(self):
		y, x = self.position
		return self.tape[y][x]

	def write(self, value):
		y, x = self.position
		self.tape[y][x] = value

	def move(self, new_x, new_y):
		y, x = self.position
		if new_x != "N": x += 1 if new_x == "L" else -1
		if new_y != "N": y += 1 if new_y == "D" else -1
		self.position = (y,x)

	def set_state(self, new_state):
		self.state = new_state



if __name__ == '__main__':

	# TESTING
	turmite = Turmite([
	[1,2,3],
	[4,5,6],
	[7,8,9]
	])

	# Rotate
	for rotate in [turmite.rotate_right, turmite.rotate_left]:
		for i in range(4):
			rotate()
			print(turmite)


	turmite = Turmite([
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12],
	[12,14,15,16]
	])

	for rotate in [turmite.rotate_right, turmite.rotate_left]:
		for i in range(4):
			rotate()
			print(turmite)

