from CardType import CardType
from Cards import *
from enum import Enum

class Turn(Enum):
	player = 1
	opponent = 2

class Game:

	def __init__(self, player1, player2):
		self.gameplay = True
		self.player = player1
		self.opponent = player2
		self.turn = Turn.player

	def switchTurn(self):
		if self.turn == Turn.player:
			self.turn = Turn.opponent
		elif self.turn == Turn.opponent:
			self.turn = Turn.player

	def opponentTurn(self):
		card = self.opponent.pickCard()
		print("Opponent Drew: %s -- %s" % (card.name, card.description))
		if card.type == CardType.attack:
			card.effect = card.effect + self.opponent.powerBoost
			self.player.applyCard(card)
		else:
			self.opponent.applyCard(card)
		self.opponent.drawCards()

	def playerTurn(self):
		card = self.player.pickCard()
		print("Player Drew: %s -- %s" %(card.name, card.description))
		if card.type == CardType.attack:
			card.effect = card.effect + self.player.powerBoost
			self.opponent.applyCard(card)
		else:
			self.player.applyCard(card)
		self.player.drawCards()

	def announceWinner(self):
		if self.player.health <= 0:
			print("Opponent Wins with %s health" % self.opponent.health)
		elif self.opponent.health <=0:
			print("Player Wins with %s health" % self.player.health)

	def gameLoop(self):
		while self.gameplay:
			if self.turn == Turn.player:
				self.playerTurn()
			else:
				self.opponentTurn()

			if self.player.health <= 0 or self.opponent.health <= 0:
				self.gameplay = False

			self.switchTurn()
		self.announceWinner()
