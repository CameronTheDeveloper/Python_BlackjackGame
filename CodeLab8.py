#!/usr/bin/env python3
#Header
import cards
import bal_file
FILENAME = "balSaved.txt"

import locale as lc
result = lc.setlocale(lc.LC_ALL, "")
if result[0] == "C":
    lc.setlocale(lc.LC_ALL, "en_US")


def header():
    #header
    print("lets Play BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()


def get_Bal():
    bal = bal_file.read_bal()
    return bal

def get_Bet(bal):
    while True:
        try:
            bet = input("Bet amount: ")
            bet = float(bet)

            while bet < 5 or bet > 1000 or bet > bal:
                if bet < 5:
                    bet = input("INVALID! Bet can't be lower than 5!\nBet amount: ")
                    bet = float(bet)
                elif bet > 1000:
                    bet = input("INVALID! Bet can't be higher than 1000!\nBet amount: ")
                    bet = float(bet)
                elif bet > bal:
                    bet = input("INVALID! Can't afford that bet amount!\nBet amount: ")
                    bet = float(bet)
                elif bet >= 5 and bet <= 1000:
                    break
            return bet
        except ValueError:
            print("INVALID amount. Try again.")


def buy_more_chips(bal):
    while True:
        try:
            amount = float(input("Amount: "))
            if 0 < amount <= 10000:
                bal += amount
                break
            else:
                print("Invalid amount! Needs to be from 0 - 10,000")
            return bal
        except ValueError:
            print("INVALID amount. Try again: ")

def playGame():
    bal = get_Bal()
    while True:
        if bal < 5:
            print("You are out of money!")
            buy_more = input("Would you like to buy chips? (y/n): ")
            if buy_more == "y":
                bal = buy_more_chips(bal)
                bal_file.write_bal(bal)
            else:
                break
        print()
        print("Balance: ", lc.currency(bal, grouping=True))
        bet = get_Bet(bal)
        print()
        deck = cards.get_deck()
        cards.shuffle(deck)
        dealer_hand = cards.get_empty_hand()
        player_hand = cards.get_empty_hand()

        cards.add_card(dealer_hand, cards.deal_card(deck))
        cards.add_card(player_hand, cards.deal_card(deck))
        cards.add_card(player_hand, cards.deal_card(deck))

        display_cards(dealer_hand, "DEALER'S HAND: ")
        print()
        display_cards(player_hand, "YOUR HAND: ")
        print()

        player_hand = play(deck, player_hand)

        while cards.get_points (dealer_hand) < 17:
            cards.add_card(dealer_hand, cards.deal_card(deck))
        display_cards(dealer_hand, "DEALER'S HAND: ")
        print()
        print("YOUR POINTS:     " + str(cards.get_points(player_hand)))
        print("DEALER'S POINTS: " + str(cards.get_points(dealer_hand)))

        print()
        player_points = cards.get_points(player_hand)
        dealer_points = cards.get_points(dealer_hand)

        if player_points > 21:
            print("YOU BUSTED! You LOSE!")
            bal -= bet
        elif dealer_points > 21:
            print("DEALER BUSTED! You WIN!")
            bal += bet
        else:
            if player_points == 21 and len(player_hand) == 2:
                if dealer_points == 21 and len(dealer_hand == 2):
                    print("You and the Dealer BOTH got BlackJack! PUSH!")
                else:
                    print("BLACKJACK! You win!")
                    bal += bet * 1.5
                    money = round(bal, 2)
            elif player_points > dealer_points:
                print("You WIN!!")
                bal += bet
            elif player_points < dealer_points:
                print("You LOSE!")
                bal -= bet
            elif player_points == dealer_points:
                print("PUSH!")
            else:
                print("Sorry! I don't know what happened. Error??")

        print("Money:", lc.currency(bal, grouping=True))
        print()
        bal_file.write_bal(bal)



        again = input("Would you like to play again? (y/n): ")
        if again.lower() != "y":
            print("Thanks for playing! Come again soon!")
            break




def display_cards(hand, title):
    print(title.upper())
    for card in hand:
        print(card[0], "of", card[1])       #Rank and Suit

def play(deck, player_hand):
    while True:
        choice = input("Hit or Stand? (h/s): ")
        print()
        if choice.lower() == "h":
            cards.add_card(player_hand, cards.deal_card(deck))
            display_cards(player_hand, "YOUR CARDS: ")
            print()
            if cards.get_points(player_hand) > 21:
                break
        elif choice.lower() == "s":
            display_cards(player_hand, "YOUR CARDS: ")
            print()
            break
        else:
            print("INVALID! Try again: ")

    return player_hand

#Main function
def main():
    header()
    playGame()


if __name__ == "__main__":
    main()


