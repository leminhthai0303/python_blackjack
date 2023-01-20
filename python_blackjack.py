import random

suits = ['Diamond','Club','Spade','Heart']
values = ['Ace', 2,3,4,5,6,7,8,9,10,'J','Q','K']


def create_a_deck():
    deck = []
    for s in suits:
        for v in values:
            deck.append(f"{v}_{s}")
    return deck

def deal(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

def point(card, n):
    value,_ = card.split("_")
    if value == 'J' or value == 'Q' or value == 'K':
        return 10
    elif value == 'Ace' and n == 2:
        return [10, 11]
    elif value == 'Ace' and n == 3:
        return [10, 1]
    elif value == 'Ace' and (n == 4 or n == 5):
        return 1
    else:
        return int(value)

def player_hand(deck):
    #Init default hand values
    hand = []
    n = 2
    p = 0

    #Add 2 card to the hand
    hand.append(deal(deck))
    hand.append(deal(deck))


    #print points and cards on the hand 
    for c in hand:
        if type(point(c,n)) != list:
            p += point(c,n)
            print(f"{c} || {p}")
        else:
            d_p = point(c,n)
            p1 = d_p[0] + p
            p2 = d_p[1] + p
            print(f"{c} || {p1}/{p2}")
    #Hit or Stand
    while len(hand) < 5:
        ans = input("HIT or STAND?:(H/S) ").upper()
        if ans != 'H' or ans != 'S':
            pass
        if ans == 'H' and p < 21:
            c = deal(deck)
            hand.append(c)
            n += 1
            if type(point(c,n)) != list:
                p += point(c,n)
                print(p)
            else:
                d_p = point(c,n)
                p1 = d_p[0] + p
                p2 = d_p[1] + p
                print(f"{p1}/{p2}")      
        else:
            break
    return hand
    

def main():
    deck = create_a_deck()
    player_hand(deck)

main()