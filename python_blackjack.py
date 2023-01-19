import random

suits = ['Diamond','Club','Spade','Heart']
values = ['Ace', 2,3,4,5,6,7,8,9,10,'J','Q','K']


def create_a_deck():
    hand = []
    for s in suits:
        for v in values:
            hand.append(f"{v}_{s}")
    return hand

def deal(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

def player_hand(deck):
    hand = []
    hand.append(deal(deck))
    hand.append(deal(deck))
    print(hand)
    while len(hand) < 5:
        ans = input("HIT or STAND?: H/S").upper()
        if ans != 'H' or ans != 'S':
            pass
        if ans == 'H':
            hand.append(deal(deck))
            print(hand)
        else:
            break
    return hand
    

def main():
    deck = create_a_deck()
    player_hand(deck)

main()