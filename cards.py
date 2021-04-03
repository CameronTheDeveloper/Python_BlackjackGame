#!/usr/bin/env python3

def get_deck():
    deck = []
    ranks = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",            #Rank and Suit touples
            "Jack", "Queen", "King"}
    suits = {"Clubs", "Diamonds", "Hearts", "Spades"}
    for suit in suits:
        for rank in ranks:
            if rank == "Ace":
                value = 11
            elif rank == "Jack" or rank == "Queen" or rank == "King":
                value = 10
            else:
                value = int(rank)

            card = [rank, suit, value]
            deck.append(card)               #Adds cards to deck
    return deck

def shuffle(deck):
    import random
    random.shuffle(deck)

def deal_card(deck):
    card = deck.pop()       #Pops top card off deck.
    return card

def get_empty_hand():
    hand = []               #Hand = empty
    return hand

def add_card(hand, card):
    hand.append(card)       #Adds card to hand

def get_points(hand):       #Calculates ppoints per hand
    points = 0
    ace_count = 0
    for card in hand:
        if card[0] == "Ace":
            ace_count += 1
        points += card[2]           #2 since card = [rank, suit, value]

    if ace_count > 0 and points > 21:           #So ace equals 1 and 11
        points = points - (ace_count * 10)
    if ace_count > 1 and points <= 11:
        points += 10
    return points


#Testing
def main():
    deck = get_deck()
    shuffle(deck)
    for card in deck:
        print(card)
    print()

    hand = get_empty_hand()
    add_card(hand, deal_card(deck))
    add_card(hand, deal_card(deck))
    add_card(hand, deal_card(deck))     #3 cards added

    print("Hand:", hand)
    print("Points:", get_points(hand))


if __name__ == "__main__":
    main()
