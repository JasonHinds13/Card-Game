from Deck import *
from random import choice
from CardType import CardType

class Participant:
	def __init__(self, name, health, defence, deck):
		self.name = name
		self.health = health
		self.defence = defence
		self.deck = deck
		self.hand = [deck.getRandomCard() for i in range(5)] # Hand should contain 5 cards
		self.powerBoost = 0 # attack boost
		self.cardsApplied = []

	def drawCards(self):
		# replace as many cards as was used up in the hand if cards remain in the deck
		# in case we can ever use multiple cards in one turn
		rep = 5 - len(self.hand)
		self.hand = self.hand + [self.deck.getRandomCard() for i in range(rep)]

	def pickCard(self, index=None):
		return

	def applyCard(self, card):
		if card.turns == 1:
			self.playCard(card)
		else:
			self.cardsApplied.append(card)
			cardsToRemove = []

			for ccard in self.cardsApplied:
				if ccard.turns > 1:
					self.playCard(ccard)
					ccard.turns = ccard.turns - 1
				else:
					cardsToRemove.append(ccard)

			for ccard in cardsToRemove:
				self.undoCardEffect(ccard)

	def playCard(self, card):
		if card.type == CardType.attack:
			self.health = self.health - card.effect
		elif card.type == CardType.defence:
			pass
		elif card.type == CardType.assist:
			self.powerBoost = card.effect
		elif card.type == CardType.heal:
			self.health = self.health + card.effect

	def undoCardEffect(self, card):
		if card.type == CardType.assist:
			self.powerBoost = 0
		elif card.type == CardType.defence:
			pass
		self.cardsApplied.remove(card)

class Player(Participant):
	def __init__(self, name, health, defence, deck):
		Participant.__init__(self, name, health, defence, deck)

class Opponent(Participant):
	def __init__(self, name, health, defence, deck):
		Participant.__init__(self, name, health, defence, deck)

	def pickCard(self, index=None):
		if index:
			card = self.hand[index]
		else:
			card = choice(self.hand)
		self.hand.remove(card)
		return card