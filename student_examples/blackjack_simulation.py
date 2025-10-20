# @Author - Connor

import random

# BLACKJACK (21)

# Variables
money = 500

# Functions

# Welcomes players to table
def table_welcome():
    global money
    print("Welcome to the Blackjack table") # Providing the user with feedback
    print("You have : $", money) # Providing the user with feedback
    print("A bet of 0 means you quit!") # Providing the user with feedback
    print("How much do you want to bet? Each win doubles your money!") # Providing the user with feedback


# Draws a card
def card_draw(cards):
    print("Shuffling deck") # Provides feeback to user
    print("Drawing your card") # Provides feeback to user
    card = random.choice(cards) # Chooses a random card
    print("You drew a", card) # Provides feeback to user
    cards.remove(card) # Removes the card from the deck
    card = face_card_value(card) # Calls the function that determines the value of the face cards
    return card # Returns the card


def face_card_value(card):
    if card == "A": # If the card is an Ace
        print("Do you want it to be 11 or 1") # Asking the user what they want their ace to be
        try: # Try to do this unless the user enters something that isn't an option
            ace = input() # Taking the input of the user
            if ace == "11": # If the user picks 11 the card's value becomes 11
                card = 11
                return card
            else: # Else the card's value becomes 1
                card = 1
                return card
        except ValueError:
            print("Please only type an 11 or a 1") # Providing the user with feedback
    elif card == "J" or card == "Q" or card == "K": # If the card is a Jack, Queen, or King the card's value becomes 10
        card = 10
        return card
    else: # Else just return the card that already is a number
        return card
       

def dealer_play_draw(dealer_card_total, cards):
    card = random.choice(cards) # Dealer draws a card
    cards.remove(card) # Remove card from deck
    card = dealer_face_card_value(card, dealer_card_total) # Determines the value of the face cards
    return card # Returns the card


def dealer_face_card_value(card, dealer_card_total):
    if card == "A": # If the card is an Ace
        if dealer_card_total <=10: # If the total value of the cards are less than or equal to ten 
            card = 11 # The card is worth 11
            return card # Returns the card
        else: # Else the Ace is worth 1
            card = 1
            return card # Returns the card
    elif card == "J" or card == "Q" or card == "K": # If the card is a Jack, Queen, or King the card's value becomes 10
        card = 10
        return card # Returns the card
    else:
        return card # Returns the card if it's not a face card


def bet_system(money):  
    bet = int(input()) # Takes the user's input
    if bet > money: # If the bet is greater than the players money, change it to the max they can bet
        print("You cannot bet that much, changing it to your max bet instead!") # Providing user feedback
        bet = money 
        print ("You bet: $", bet) # Providing user feedback
        return bet # Returns the bet
    else: # Else just return the bet the play entered
        print ("You bet: $", bet) # Providing user feedback
        return bet # Returns the bet


def game_main(card_value_total, hit, cards):
    while True:
        play = True
        failure = False
        dealer_card_total = 0
        if card_value_total == 21: # If the player reaches 21, the dealer plays
            print("The Dealer will play now") # Providing the user with feedback
            win = dealer_play_main(dealer_card_total, card_value_total, cards) # Dealer plays
            return win
        elif card_value_total < 21: # If the player has cards that add up to less than 21, continue playing
            card = card_draw(cards) # Draws a card
            card_value_total = card_value_total + card # Adds the card to the total
            print("Your cards add up to", card_value_total) # Providing the user with feedback
            if hit == True and card_value_total >= 21: # if the play has hit and the total is less than or equal to 21
                win = dealer_play_main(dealer_card_total, card_value_total, cards) # The dealer plays
                return win
            else:
                print("Choose one:") # Providing the user with a choice
                print("1. Hit")
                print("2. Stand")
                while failure == True or play == True: # While the player has failed or While play == True, continue with the loop
                    try: # Try this unless a ValueError occurs
                        choice = int(input()) # The player can choose 1 or 2
                        print("You chose", choice) # Providing the user with feedback
                        if 0 < choice < 3: # If the choice is 1 or 2
                            if choice == 1: # If the choice is 1
                                    hit = True 
                                    break
                            else: # When the choice is 2
                                win = dealer_play_main(dealer_card_total, card_value_total, cards) # The dealer plays
                                return win
                        else: # If the player picks a number other than 1 or 2
                            print("Choose 1 or 2 only!") # Providing the user with feedback
                            failure = True
                    except ValueError:
                        print("Please enter a 1 or a 2 only!") # Providing the user with feedback
                        failure = True
        else: # If the player goes above 21, THEY LOSE!
            print("You lose!")
            break     


def dealer_play_main(dealer_card_total, card_value_total, cards):
            print("The Dealer will play now") # Providing the user with feedback
            dealer_card = 0
            while True: # Determines if the player has won or lost when compared with the dealer, else the dealer continues drawing cards
                dealer_card_total = dealer_card_total + dealer_card 
                print("Dealer total:", dealer_card_total) # Providing the user with feedback
                if dealer_card_total > 21 and card_value_total <= 21:
                    print("You win!") # Providing the user with feedback
                    win = 1
                    return win
                elif dealer_card_total == 21 and card_value_total == 21:
                    print("Draw! You get your money back") # Providing the user with feedback
                    win = 2
                    return win
                elif dealer_card_total > card_value_total and dealer_card_total <= 21 and card_value_total <= 21:
                    print("You lose!") # Providing the user with feedback
                    win = 3
                    return win
                elif dealer_card_total > 21 and card_value_total > 21:
                    print("Draw! You get your money back") # Providing the user with feedback
                    win = 2
                    return win    
                else:
                    dealer_card = dealer_play_draw(dealer_card_total, cards)
                    print("Dealer draws a", dealer_card) # Providing the user with feedback


def money_reward(win, bet):
    if win == 1: # If the player won, double the bet
        reward = bet * 2
        return reward
    elif win == 2: # If the player draws with the dealer, they get their bet back
        reward = bet
        return reward
  

# GAME
while True:
    # Resetting card list
    cards = ["A", "A", "A", "A", 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K"]
    
    win = 0 # The player hasn't won, lost, or drawed
    hit = False # The player hasn't hit yet
    card_value_total = 0 #  The player has no cards, so no total!
    table_welcome() # Welcomes the player
    try: 
        bet = int(bet_system(money)) # The player enters a bet
        money = money - bet # Removes the bet from the money
        if bet > 0: # If the bet is greater than 0
            while True:
                win = game_main(card_value_total, hit, cards) # Plays the game to determine if they won
                if win == 1 or win == 2: # If they win or draw, they get a reward and the game resets
                    money = money + money_reward(win, bet) # Determines the reward and adds it to the money
                    break
                else: # If the player loses, reset the game
                    break
        else: # Else the player is kicked out of the game
            print("You played enough? THEN GET OUT!!!") # Providing the user with feedback
            break
    except ValueError:
        print("Please enter a number in digits") # Providing the user with feedback