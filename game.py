from deck import Table
from dealer import Dealer
from player import Player
import random


def get_card_value(card):
    if card == 'J' or card == 'K' or card == 'Q':
        return 10
    if card == 'A':
        return 11
    else:
        return card


def get_sum_of_cards(cards_list):
    sum_in_hand = 0
    count_number_ace = 0
    card_value = 0
    for item in cards_list:
        card_value = get_card_value(item)
        if card_value == 11:
            count_number_ace += 1
        sum_in_hand = sum_in_hand + card_value

    if sum_in_hand > 21 and count_number_ace >= 2:
        sum_in_hand -= 10 * (count_number_ace - 1)

    return sum_in_hand


def get_score(deck, person):
    random.shuffle(deck)
    new_card = deck.pop()
    new_card = get_card_value(new_card)

    if new_card == 11:
        new_card = 'A'
    player.players[person].append(new_card)
    print(player.players[person])

    total_sum_in_hand = get_sum_of_cards(player.players[person])

    if total_sum_in_hand > 21 and 'A' in player.players[person]:
        total_sum_in_hand -= 10

    return total_sum_in_hand


def players_chance(deck, player):
    copy_players = player.players.copy()
    for person in player.players:
        print(person + 's turn')
        players_choice = player.hit_or_stand()

        sum_before_new_card = get_sum_of_cards(player.players[person])

        while players_choice == 'h':
            total_sum_in_hand = get_score(deck, person)
            if total_sum_in_hand > 21:
                print(person + ' you are busted')
                del copy_players[person]
                break

            players_choice = player.hit_or_stand()

    player.players = copy_players


def blackjack(cards_list):
    count_for_blackjack = 0

    for item in cards_list:
        if item == 'J' or item == 'Q' or item == 'K' or item == 'A':
            count_for_blackjack += 1

    if count_for_blackjack <= 1:
        count_for_blackjack = 0
    else:
        count_for_blackjack = 1

    return count_for_blackjack


def who_wins(player):
    print('Dealers hole card value is: ', end='')
    Dealer.show_hole_card(dealer)

    sum_in_dealer_hands = get_sum_of_cards(Dealer.dealer_cards)
    if sum_in_dealer_hands >= 21:
        for person in player.players:
            print(person + ' wins against dealer')
    else:
        for person in player.players:
            sum_in_players_hand = get_sum_of_cards(player.players[person])
            if sum_in_dealer_hands > sum_in_players_hand:
                print('Dealer ' + Dealer.dealer_name + ' wins')

            elif sum_in_dealer_hands < sum_in_players_hand:
                print(person + ' wins against dealer')

            elif sum_in_dealer_hands == sum_in_players_hand:
                if blackjack(Dealer.dealer_cards) and not blackjack(player.players[person]):
                    print('Dealer ' + Dealer.dealer_name + ' wins')

                elif not blackjack(Dealer.dealer_cards) and not blackjack(player.players[person]):
                    print(person + ' wins against dealer')

                else:
                    print('Draw')


jack = Table()
deck = jack.get_deck(int(input('Enter number of decks needed min:1 and max:8 : ', )))
dealer = Dealer(deck)
player = Player()
player.hand_for_each_player(int(input('Enter number of players min:1 and max:8 : ', )), deck)
dealer.show_first_card()
player.show_cards()
players_chance(deck, player)
who_wins(player)
