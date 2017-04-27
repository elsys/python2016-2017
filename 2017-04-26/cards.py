import random



class Card:

	suit_names = ["Clubs", "Diamonds", "Heart", "Spades"]
	rank_names = ["2","3", "4", "5", "6", "7", "8", "9", "10", 
		"Jack", "Queen", "King", "Ace"]

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank	

	def print_card(self):
		print(self.suit_names[self.suit], self.rank_names[self.rank])

	def __str__(self):
		return "%s of %s" % (Card.rank_names[self.rank], 
				Card.suit_names[self.suit])


	def __lt__(self, other):
		if self.rank < other.rank:
			return True
		elif self.suit < other.suit:
			return True
		return False

	def __le__(self, other):
		if self.rank <= other.rank:
			return True
		elif self.suit <= other.suit:
			return True
		return False
	
	def __eq__(self, other):
		if self.rank == other.rank and self.suit == other.suit:
			return True
		return False




class Deck:

	def __init__(self):
		self.cards = []
		
		for suit in range(4):
			for rank in range(13):
				c = Card(suit, rank)
				self.cards.append(c)
	
	def print_deck(self):
		for c in self.cards:
			print(c)

	def __str__(self):
		res = [str(c) for c in self.cards]
		return ",\n".join(res)

	def shuffle(self):
		random.shuffle(self.cards)

	def pop_card(self):
		return self.cards.pop()

	def add_card(self, card):
		return self.cards.append(card)
		

if __name__ == "__main__":
	print(__name__)
	d = Deck()
	# d.print_deck()

	print(d)
	








