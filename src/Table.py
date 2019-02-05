class Table:
	def __init__(self):
		self.dominoes = [] 
		self.visualized_tree = None

	def visualize_table(self):
		dominoe_string = ""
		for dominoe in self.dominoes:
			dominoe_string += dominoe

		print dominoe_string

	def add_dominoe(self, dominoe, to_left):
		# If the tree is empty
		if len(self.dominoes) == 0:
			self.dominoes += [dominoe]
		
		# If we are adding to the left we prepend the array
		if to_left:
			table_left_number = self.dominoes[0].get_left_number()
			if table_left_number == dominoe.right_number:
				self.dominoes = [dominoe] + self.dominoes
				return True
			elif table_left_number == dominoe.left_number:
				dominoe.rotated = True
				self.dominoes = [dominoe] + self.dominoes
				return True

		else:
			index_of_last_dominoe = len(self.dominoes) - 1
			if dominoe.can_connect_and_rotate(self.dominoes[index_of_last_dominoe]):
				self.dominoes = self.dominoes + [dominoe]

		# If we got to here the mating failed
		print("Failed to mate dominoes")
		return False

	def is_game_closed(self):
		pass