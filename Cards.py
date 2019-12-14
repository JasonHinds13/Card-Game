from CardType import CardType

# Rather than applying defence and assist cards to cards apply to players for # of turns

class Card:
	def __init__(self, name, effect, turns, description):
		self.name = name
		self.effect = effect
		self.turns = turns
		self.description = description

class AttackCard(Card):
	def __init__(self, name, effect, turns, description):
		Card.__init__(self, name, effect, turns, description)
		self.type = CardType.attack

class HealCard(Card):
	def __init__(self, name, effect, turns, description):
		Card.__init__(self, name, effect, turns, description)
		self.type = CardType.heal

class AssistCard(Card):
	def __init__(self, name, effect, turns, description):
		Card.__init__(self, name, effect, turns, description)
		self.type = CardType.assist

class DefenceCard(Card):
	def __init__(self, name, effect, turns, description):
		Card.__init__(self, name, effect, turns, description)
		self.type = CardType.defence