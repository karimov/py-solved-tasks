class CardGame:
      def __init__(self):
      	  self.deck = Deck()
      	  self.deck.shuffle_v2




class Deck:
      def __init__(self):
      	  self.cards = []
      	  for suit in range(4):
      	      for rank in range(1,14):
      	      	  self.cards.append(Card(suit, rank))
      def print_deck(self):
     	 for card in self.cards:
     	     print(card)
      def __str__(self):
     	  s = ""
     	  for i in range(len(self.cards)):
     	      s= s + " "*i + str(self.cards[i]) + "\n"
     	  return s
      def shuffle_v1(self):
      	  import random
      	  rng = random.Random()
      	  num_cards = len(self.cards)
      	  for i in range(num_cards):
      	      j = rng.randrange(i, num_cards)
      	      (self.cards[i], self.cards[j]) = (self.cards[j], self.cards[i])
      def shuffle_v2(self):
     	  import random
     	  rng = random.Random()
     	  rng.shuffle(self.cards)
      def remove(self, card):
      	  if card in self.cards:
      	     self.cards.remove(card)
      	     return True
      	  else:
      	     return False
      def pop(self):
      	  return self.cards.pop()
      def is_empty(self):
      	  return self.cards == []
      def deal(self, hands, num_cards = 999):
      	  num_hands = len(hands)
      	  for i in range(num_cards):
              if self.is_empty():
                 break                    # Break if out of cards
              card = self.pop()            # Take the top card
              hand = hands[i % num_hands]  # Whose turn is next?
              hand.add(card)               # Add the card to the hand
      	  
class Hand(Deck):
      def __init__(self, name=''):
      	  self.cards = []
      	  self.name = name
      def add(self, card):
      	  self.cards.append(card)
      def __str__(self):
          s = "Hand " + self.name
          if self.is_empty():
            s += " is empty\n"
          else:
            s += " contains\n"
          return s + Deck.__str__(self)
