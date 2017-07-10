
class Turmite:

	def __init__(self, tape):
		print("Initialized a {}-by-{} Turmite tape".format(len(tape[0]), len(tape)))
		self.tape = tape

	def __str__(self):
		return "".join([" ".join([str(i) for i in row]) + "\n" for row in self.tape])

	def rotate_right(self):
		print("Rotate right")
		self.tape = [list(row)[::-1] for row in list(zip(*self.tape))]

	def rotate_left(self):
		print("Rotate left")
		self.tape = [list(row) for row in list(zip(*self.tape))[::-1]]


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

