import random
import time

class BlackjackGame:
    def __init__(self):
        # Initialize the game by creating a shuffled deck and initializing player and dealer hands.
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        # Create a standard deck of cards, each represented as a dictionary with rank and suit.
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
        random.shuffle(deck)
        return deck

    def deal_card(self, hand):
        # Deal a card from the deck and add it to the specified hand.
        card = self.deck.pop()
        hand.append(card)
        return card

    def calculate_hand_value(self, hand):
        # Calculate the value of a hand, considering Aces and their flexible values.
        value = 0
        num_aces = 0

        for card in hand:
            rank = card['rank']
            if rank == 'Ace':
                num_aces += 1
                value += 11
            elif rank in ['King', 'Queen', 'Jack']:
                value += 10
            else:
                value += int(rank)

        # Adjust for Aces if the total value exceeds 21.
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1

        return value

    def display_hand(self, hand, hide_first_card=False):
        # Display the cards in a hand, optionally hiding the first card.
        time.sleep(0.5)
        if hide_first_card:
            print(f"Hand: [{hand[1]['rank']} of {hand[1]['suit']}]")
        else:
            print(f"Hand: {[card['rank'] + ' of ' + card['suit'] for card in hand]}")
        time.sleep(0.5)
        print(f"Current Score: {self.calculate_hand_value(hand)}")

    def player_turn(self):
        # Allow the player to take their turn, prompting for hit or stand and handling the logic.
        while True:
            self.display_hand(self.player_hand)
            player_choice = input("Do you want to hit (h) or stand (s)? ").lower()

            time.sleep(0.5)
            if player_choice == 'h':
                # If the player chooses to hit, draw a card and handle Ace value if drawn.
                card = self.deal_card(self.player_hand)
                if card['rank'] == 'Ace':
                    ace_value = input("Do you want the value of Ace to be 1 or 11? ")
                    while ace_value not in ['1', '11']:
                        ace_value = input("Invalid choice. Choose 1 or 11: ")
                    card['value'] = int(ace_value)
                time.sleep(1)
                print(f"You drew the {card['rank']} of {card['suit']}.")
                player_value = self.calculate_hand_value(self.player_hand)

                time.sleep(0.5)
                # Check if the player busts, gets Blackjack, or continues playing.
                if player_value > 21:
                    print("Bust! You went over 21. You lose.")
                    return 'bust'
                elif player_value == 21:
                    print("You got Blackjack!")
                    return 'blackjack'
            elif player_choice == 's':
                # If the player chooses to stand, end their turn.
                return 'stand'
            else:
                print("Invalid choice. Please enter 'h' or 's'.")

    def dealer_turn(self):
        # Allow the dealer to take their turn, following a simple strategy for drawing cards.
        while self.calculate_hand_value(self.dealer_hand) < 17:
            card = self.deal_card(self.dealer_hand)
            if card['rank'] == 'Ace':
                # Choose the value for Ace based on a simple strategy.
                card['value'] = 11 if self.calculate_hand_value(self.dealer_hand) + 11 <= 21 else 1
            time.sleep(0.5)
            print(f"Dealer drew the {card['rank']} of {card['suit']}.")

        dealer_value = self.calculate_hand_value(self.dealer_hand)
        time.sleep(0.5)
        print(f"Dealer's hand: {[card['rank'] + ' of ' + card['suit'] for card in self.dealer_hand]}")
        time.sleep(0.5)
        print(f"Dealer's hand value: {dealer_value}")

        # Check if the dealer busts, gets Blackjack, or continues playing.
        if dealer_value > 21:
            print("Dealer busts! You win!")
            return 'dealer_bust'
        elif dealer_value == 21:
            print("Dealer got Blackjack!")
            return 'dealer_blackjack'
        else:
            return 'stand'

    def play_game(self):
        # Play the entire game, including initial dealing, player and dealer turns, and result comparison.
        # Initial deal
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)

        # Player's turn
        player_result = self.player_turn()

        time.sleep(0.5)
        if player_result == 'bust':
            return "Game over! Better luck next time"

        # Dealer's turn
        dealer_result = self.dealer_turn()

        time.sleep(0.5)
        if dealer_result == 'dealer_bust':
            return "You win! The house is bust"
        elif dealer_result == 'dealer_blackjack':
            return "You lose. The house got Blackjack."

        # Compare hands and determine the winner or if it's a tie.
        player_value = self.calculate_hand_value(self.player_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)

        time.sleep(0.5)
        if player_value > dealer_value:
            return "You win, good job"
        elif player_value < dealer_value:
            return "You lose, hard luck"
        else:
            return "It's a tie!"

# Example usage
if __name__ == "__main__":
    game = BlackjackGame()
    print('Welcome to Blackjack')
    result = game.play_game()
    print(result)
    print('Thanks for playing')
