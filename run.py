from Game import *
from Deck import *
from Participants import *


if __name__ == '__main__':
	p1 = Opponent("Player", 100, 0, Deck())
	p2 = Opponent("Enemy",100, 0, Deck())
	game = Game(p1,p2)
	game.gameLoop()