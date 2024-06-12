import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for rank in range(2, 11):
                self.cards.append(Card(suit, str(rank)))
            for rank in ['Jack', 'Queen', 'King', 'Ace']:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        ace_count = 0
        for card in self.cards:
            if card.rank.isdigit():
                value += int(card.rank)
            elif card.rank in ['Jack', 'Queen', 'King']:
                value += 10
            else:
                ace_count += 1
                value += 11
        while value > 21 and ace_count:
            value -= 10
            ace_count -= 1
        return value

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

def play_blackjack():
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    print("Player's Hand:", player_hand)
    print("Dealer's Hand:", dealer_hand.cards[0], "and [Hidden]")

    while True:
        player_value = player_hand.get_value()
        if player_value > 21:
            print("Player busts! Dealer wins.")
            break

        action = input("Do you want to hit or stand? (h/s): ").lower()
        if action == 'h':
            player_hand.add_card(deck.deal_card())
            print("Player's Hand:", player_hand)
        elif action == 's':
            break

    if player_value <= 21:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        print("Dealer's Hand:", dealer_hand)
        dealer_value = dealer_hand.get_value()
        if dealer_value > 21 or dealer_value < player_value:
            print("Player wins!")
        elif dealer_value > player_value:
            print("Dealer wins!")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    play_blackjack()
