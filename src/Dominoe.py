class Dominoe:
	def __init__(self, top_number, bottom_number):
		self.top_number = top_number
		self.bottom_number = bottom_number

		self.rotated = False
	
	def __str__(self):
		if self.rotated:
			print "|" + str(self.bottom_number) + "-" + str(self.top_number) + "|"
		else:
			print "|" + str(self.top_number) + "-" + str(self.bottom_number) + "|"


