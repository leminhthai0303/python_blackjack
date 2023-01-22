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

def point(p, card):
    value,_ = card.split("_")
    if value == 'J' or value == 'Q' or value == 'K':
        return p + 10
    elif value == 'Ace' and p <= 11:
        return p + 11
    elif value == 'Ace' and p > 11:
        return p + 1
    else:
        return p + int(value)

def is_blackjack(hand):
    first_card = hand[0]
    value1,_ = first_card.split("_")
    second_card = hand[1]
    value2,_ = second_card.split("_")
    if 'Ace' in first_card:
        if 'J' in second_card or 'Q' in second_card or 'K' in second_card or int(value2) == 10:
            return True
    elif 'Ace' in second_card:
        if 'J' in first_card or 'Q' in first_card or 'K' in first_card or int(value1) == 10:
            return True
    elif 'Ace' in first_card and 'Ace' in second_card:
        return True
    else:
        return False


def player_hand(deck):
    #Init default hand values
    hand = []
    n = 2
    p = 0

    #Add 2 card to the hand
    hand.append(deal(deck))
    hand.append(deal(deck))


    if is_blackjack(hand):
        for c in hand:
            print(c)
        return True
    else:
    #print points and cards on the hand 
        for c in hand:
            p = point(p,c)
            print(f"{c} || {p}")
        #Hit or Stand
        while p < 21:
            ans = input("HIT or STAND?:(H/S) ").upper()
            if ans != 'H' or ans != 'S':
                pass
            if ans == 'H':
                c = deal(deck)
                hand.append(c)
                p = point(p, c)
                print(f"{c} || {p}")
            else:
                break
            if p > 21:
                print("You are BUSTED")
        return p
    

def dealer_hand(deck, player):
    #Init default hand values
    hand = []
    p = 0

    #Add 2 card to the hand
    hand.append(deal(deck))
    hand.append(deal(deck))

    if is_blackjack(hand):
        for c in hand:
            print(c)
        return True
    else:
        #print points and cards on the hand 
        for c in hand:
            p = point(p,c)
            print(f"{c} || {p}")
        #Hit or Stand
        while p < 21:
            if (p <= 16 and player < 22) or (player > 21 and p <= 16):
                c = deal(deck)
                hand.append(c)
                p = point(p, c)
                print(f"{c} || {p}")
            else:
                break
            if p > 21:
                print("Dealer is BUSTED")
        return p

def main():
    deck = create_a_deck()
    player = player_hand(deck)
    print("==============================================PLAYER TURN ENDED==============================================")
    dealer = dealer_hand(deck, player)
    print("==============================================DEALER TURN ENDED==============================================")
    if player != True and dealer != True:
        if player <= 21 and dealer <= 21:
            if player > dealer:
                print("You WIN!!!")
            elif player == dealer:
                print("Draw")
            else:
                print("You LOSE!!!")
        elif player > 21 and dealer <= 21:
            print("You LOSE!!!")
        elif player <= 21 and dealer > 21:
            print("You win")
        elif player > 21 and dealer > 21:
            print("Draw")
    elif player != True and dealer == True:
        print('THE DEALER GOT BLACKJACK!!! YOU LOSE!!!')
    elif player == True and dealer != True:
        print('BLACKJACK!!! YOU WIN!!!')

if __name__ == '__main__':
    main()