import random
from Table import Table
from Dominoe import Dominoe
from HumanPlayer import HumanPlayer

class Game:
	def __init__(self):
		self.table = Table()
		self.ace_starts = True
		self.current_player = None

	def setup(self):
		self.players = self.generate_players() # Create Four Game Players and Two Teams
		self.dominoes = self.generate_dominoes() # Create Dominoe Tiles

	def setup_match(self):
		self.table.clear() # Reset the Table
		self.distribute_dominoes_to_players() # Distrubute dominoes to players

		print("Number of Dominoes Generated: ", len(self.dominoes))
		for player in self.players:
			print(player.name + '\'s hand has ' + str(len(player.hand)) + ' dominoes')
			for dominoe in player.hand:
				print('Dominoe: ' + str(dominoe.top_number) + ' , ' + str(dominoe.bottom_number))

			print('\n')

	def generate_players(self):
		player1 = HumanPlayer('PA1')
		player2 = HumanPlayer('PB1')
		player3 = HumanPlayer('PA2')
		player4 = HumanPlayer('PB2')

		players = [player1, player2, player3, player4]

		# Let's assume the teams are like this
		self.teamA = Team(player1, player3)
		self.teamB = Team(player2, player4)

		return players

	def generate_dominoes(self):
		dominoes = []
		for i in range(0, 7):
			for j in range(i,7):
				dominoe = Dominoe(i, j)
				dominoes.append(dominoe)

		self.shuffle_dominoes(dominoes)

		return dominoes

	def shuffle_dominoes(self, dominoes):
		random.shuffle(dominoes)

	def distribute_dominoes_to_players(self):
		if(not len(self.dominoes) == 28):
			print('Insuffecient Dominoes to Play')
			return False

		index = 0
		for player in self.players:
			player.hand = self.dominoes[index: index+7]
			index = index+7

	def play_match(self):
		game_ended = False

		# Decides who goes first
		if self.ace_starts: 
			# Player with ace starts
			pass
		else:
			# Partners pick who starts
			pass

		# While the game has not been won
		while(not game_ended):
			# Current Player plays
			game_ended, game_closed = self.current_player.play(self.table)

			if game_ended or game_closed:
				if not game_closed: 
					# Check if the player ended in a double
					# Check if the player lasquieneded
					# Depending on outcome get points to assign and if ace should start next
					pass

				else:
					# Find players with lowest hand
					# If multiple players, defending team wins
					# Depending on outcome get points to assign and if ace should start next
					pass

				# Increment Team score 

			else: 
				# Decide who should go next ie: the next current player
				names = [player.name for player in players]
				pos = self.names.index(self.current_player.name)

				if (pos + 1) == 4 :
					self.current_player = self.players[0]
				else:
					self.current_player = self.players[pos + 1]
				


	def play_dominoes(self):
		print('Let\'s play dominoes ! ')
		self.setup()
		team_win = False

		while not team_win:
			print('Let\'s start the game...')
			self.setup_match()

			if(self.teamA.stones == 5):
				team_win = True
				print 'Team A Wins !'

			elif(self.teamB.stones == 5):
				team_win = True
				print 'Team B Wins !'


if __name__ == '__main__':
	game = Game()
	game.play_dominoes()



