from Table import Table

class HumanPlayer:
	def __init__(self, name):
		self.name = name
		self.mode = 'Human'
		self.hand = []
		self.team = None

	def visualize_hand(self, hand, enumerate_hand = False):
		index = 1
		for dominoe in hand:
			if enumerate_hand:
				print(str(index) + '.) Dominoe: ' + str(dominoe.top_number) + ' , ' + str(dominoe.bottom_number))
				index += 1
			else:
				print('Dominoe: ' + str(dominoe.top_number) + ' , ' + str(dominoe.bottom_number))

	def remove_dominoe_from_hand(chosen_dominoe):
		for dominoe in hand:
			if dominoe.is_equal(chosen_domine):
				pass
				

	def play(self, table):
		# Show the player the table
		print('This is the table')
		self.table.visualize_table()

		# Show the player his hand
		print('This is your hand')
		visualize_hand(self.hand)

		# Check that the player has a valid dominoe to play
		valid_dominoes = []
		for dominoe in hand:
			if table.validate_dominoe(dominoe):
				valid_dominoes.append(dominoe)


		# The player has no valid dominoes
		if len(valid_dominoes) == 0:
			print('You have no valid dominoes to play. You pass.')
			return False, False

		# Show valid_dominoes
		print('These are your valid dominoes')
		visualize_hand(valid_dominoes)

		# Ask player which dominoe they would like to play
		print('Which valid dominoe would you like to play ?')
		#### Wait for response

		# Add valid dominoe to the table
		table.add_dominoe(chosen_dominoe)

		# Remove chosen dominoe from players hand
		remove_dominoe_from_hand(chosen_dominoe)

		# Check if the player is out of dominoes
		game_ended = len(self.hand) == 0

		# Check if the player has closed the game
		game_closed = table.is_game_closed()

		return game_ended, game_closed

