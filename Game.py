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
		print("Opponent Health: %s" % (self.opponent.health))

		card = self.opponent.pickCard()
		if card.type == CardType.attack:
			card.effect = card.effect + self.opponent.powerBoost
			self.player.applyCard(card)
		else:
			self.opponent.applyCard(card)
		self.opponent.drawCards()

		print("Opponent Drew: %s -- %s\n" % (card.name, card.description))

	def playerTurn(self):
		print("Player Health: %s" % (self.player.health))

		for i in range(len(self.player.hand)):
			ccard = self.player.hand[i]
			print("[%s] %s -> %s" % (i, ccard.name, ccard.description))

		ch = int(input("WHich card do you choose? "))

		card = self.player.pickCard(ch)
		if card.type == CardType.attack:
			card.effect = card.effect + self.player.powerBoost
			self.opponent.applyCard(card)
		else:
			self.player.applyCard(card)
		self.player.drawCards()

		print("Player Drew: %s -- %s\n" %(card.name, card.description))

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
