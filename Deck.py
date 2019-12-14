from CardType import CardType
from Cards import *
from random import choice

attackCards = [ AttackCard("Fire Strike", 10, 1, "Hits enemy with fire for one turn."),
	AttackCard("Ice Strike", 10, 1, "Hits enemy with Ice Shards for one turn."),
	AttackCard("Wind Scythe", 15, 1, "Cuts enemy for one turn."),
	AttackCard("Burning Ash", 20, 1, "Cloud of ash burns enemy for one turn."),
	AttackCard("Fire Strike", 17, 1, "Hits enemy with fire for one turn."),
	AttackCard("Dance of the Fire God", 30, 1, "Demon Slayer Strike for one turn."),
	AttackCard("Flare", 10, 1, "Fire flares at enemy for one turn.")
]

defenceCards = [ DefenceCard("Useless", 0, 1, "Does Nothing right now."),
	DefenceCard("Useless", 0, 1, "Does Nothing right now."),
	DefenceCard("Useless", 0, 1, "Does Nothing right now."),
	DefenceCard("Useless", 0, 1, "Does Nothing right now."),
	DefenceCard("Useless", 0, 1, "Does Nothing right now.")
]

assistCards = [ AssistCard("Attack Boost 1", 5, 1, "Boosts attack by 5 for one turn."),
	AssistCard("Attack Boost 2", 10, 1, "Boosts attack by 10 for one turn."),
	AssistCard("Attack Boost 3", 15, 1, "Boosts attack by 15 for one turn."),
	AssistCard("Attack Boost 4", 10, 3, "Boosts attack by 10 for three turns."),
]

healCards = [ HealCard("Quick Heal", 10, 1, "Gives 10 quick healing for one turn."),
	HealCard("Regenerative Heal", 10, 3, "Gives 10 healing for three turns."),
	HealCard("Strong Heal", 20, 1, "Gives 20 healing for one turn.")
]

def getRandomAttackCard():
	return choice(attackCards)

def getRandomDefenceCard():
	return choice(defenceCards)

def getRandomAssistCard():
	return choice(assistCards)

def getRandomHealCard():
	return choice(healCards)

class Deck:
	def __init__(self):
		self.attackCards = [getRandomAttackCard() for i in range(7)]
		self.defenceCards = [getRandomDefenceCard() for i in range(2)]
		self.assistCards = [getRandomAssistCard() for i in range(3)]
		self.healCards = [getRandomHealCard() for i in range(3)]
		self.fulldeck = self.attackCards + self.defenceCards + self.assistCards + self.healCards

	def getRandomCard(self):
		return choice(self.fulldeck)