class Table:
	def __init__(self):
		self.dominoes_root = None 
		self.visualized_tree = None
		self.top_end = None
		self.bottom_end = None

	def visualize_table(self):
		pass

	def validate_dominoe(self, dominoe):
		if dominoe.top_number == self.top_end or dominoe.bottom_number == self.top_end:
			return True, 0
		elif dominoe.top_number == self.bottom_end or dominoe.bottom_number == self.bottom_end:
			return True, 1
		else:
			return False, -1

	def add_dominoe(self, dominoe):
		# If the tree is empty
		if self.dominoes_root is None:
			self.dominoes_root = dominoe
			self.top_end = dominoe.top_number
			self.bottom_end = dominoe.bottom_number
			return True

		# If the top most dominoe is empty
		# if self.dominoes_top_most is None:


		# Check which side of the tree domnoe needs to go on
		else:
			isValid, side = validate_dominoe(dominoe)
			if isValid:
				if side == 0:
					pass
				elif side == 1:
					pass

				dominoeAdded = False
				neighbor = self.dominoes_root
				while not dominoeAdded:
					if side == 0:
						neighbor
						# Find top most dominoe with no neighbor
					elif side == 1:
						# bottom most dominoe with no neightbor
						pass
			else:
				return False


	def is_game_closed(self):
		pass