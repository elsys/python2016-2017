import unittest

from cards import Card, Deck, Hand



class CartTest(unittest.TestCase):

	def testLessThan(self):
		c1 = Card(0, 0)
		c2 = Card(1, 1)
		
		self.assertTrue(c1<c2)

	def testGreaterThan(self):
		c1 = Card(0, 0)
		c2 = Card(1, 1)
		
		self.assertTrue(c2 > c1)
		
	def testLessOrEqual(self):
		c1 = Card(0, 0)
		c2 = Card(1, 1)
		
		self.assertTrue(c1<=c2)

	def testEquals(self):
		c1 = Card(0, 0)
		c2 = Card(0, 0)
		
		self.assertTrue(c1==c2)
		

class DeckTest(unittest.TestCase):

	def testDeckSize(self):
		d = Deck()
		self.assertEqual(52, len(d.cards))

	def testShuffle(self):
		d = Deck()
		first_card = d.cards[0]
		self.assertEqual(0, first_card.rank)
		self.assertEqual(0, first_card.suit)
		
		last_card = d.cards[-1]
		self.assertEqual(12, last_card.rank)
		self.assertEqual(3, last_card.suit)

		d.shuffle()
		first_card = d.cards[0]
		self.assertTrue(0!=first_card.rank or 0!=first_card.suit)
	
	def testPopCard(self):
		d = Deck()
		card = d.pop_card()
		
		self.assertEqual(12, card.rank)
		self.assertEqual(3, card.suit)
		self.assertEqual(51, len(d.cards))
	
	def testAddCard(self):
		d = Deck()
		card = d.pop_card()
		self.assertEqual(51, len(d.cards))

		d.add_card(card)
		self.assertEqual(52, len(d.cards))
				

class HandTest(unittest.TestCase):

	def testEmptyHand(self):
		h = Hand("test player")
		self.assertTrue(h.is_empty())


unittest.main()


