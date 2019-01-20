class Dominoe:
	def __init__(self, top_number, bottom_number):
		self.top_number = top_number
		self.bottom_number = bottom_number

		self.top_neighbor = None
		self.bottom_neighbor = None

	def is_equal(self, dominoe):
		if self.top_number == dominoe.top_number:
			if self.bottom_number == dominoe.bottom_number:
				return True

		elif self.top_number == dominoe.bottom_number:
			if self.bottom_number == dominoe.top_number:
				return True

		return False