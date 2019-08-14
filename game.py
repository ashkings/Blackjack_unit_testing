from deck import Table
from dealer import Dealer
from player import Player
from Players_Name_list import NameList
import random


def show_table(player, name):
    item_in_name_list = 0
    for cards in player.players_card:
        print(name.name_list[item_in_name_list] + ' cards: {}' .format(cards))
        item_in_name_list = item_in_name_list + 1


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

    for card in cards_list:
        card_value = get_card_value(card)
        if card_value == 11:
            count_number_ace += 1
        sum_in_hand = sum_in_hand + card_value

    if sum_in_hand > 21 and count_number_ace >= 2:
        sum_in_hand -= 10 * (count_number_ace - 1)

    return sum_in_hand


def get_score(deck, cards):
    random.shuffle(deck)
    new_card = deck.pop()
    new_card = get_card_value(new_card)

    if new_card == 11:
        new_card = 'A'
    cards.append(new_card)
    print(cards)

    total_sum_in_hand = get_sum_of_cards(cards)

    if total_sum_in_hand > 21 and 'A' in cards:
        total_sum_in_hand -= 10

    return total_sum_in_hand


def players_chance(deck, player, name):
    show_table(player, name)

    copy_players_card = player.players_card.copy()

    item_in_name_list = 0

    for cards in player.players_card:
        print('Current Player: ', end='')
        print(name.name_list[item_in_name_list])
        print('Cards: ', end='')
        print(cards)
        players_choice = player.hit_or_stand()

        while players_choice == 'h':
            total_sum_in_hand = get_score(deck, cards)
            if total_sum_in_hand > 21:
                print(name.name_list[item] + ' you are busted')
                copy_players_card.remove(cards)
                break

            players_choice = player.hit_or_stand()
        item_in_name_list = item_in_name_list + 1
    player.players_card = copy_players_card.copy()


def blackjack(cards_list):
    count_for_blackjack = 0

    for card in cards_list:
        if card == 'J' or card == 'Q' or card == 'K' or card == 'A':
            count_for_blackjack += 1

    if count_for_blackjack <= 1:
        count_for_blackjack = 0
    else:
        count_for_blackjack = 1

    return count_for_blackjack


def who_wins(player, dealer, name):
    print('Dealers hole card value is: ', end='')
    dealer.show_hole_card()

    sum_in_dealer_hands = get_sum_of_cards(dealer.dealer_cards)
    if sum_in_dealer_hands >= 21:
        item_in_name_list = 0
        for cards in player.players_card:
            print(name.name_list[item_in_name_list] + ' wins against ' + dealer.dealer_name)
            item_in_name_list = item_in_name_list + 1
    else:
        item_in_name_list = 0
        for cards in player.players_card:
            sum_in_players_hand = get_sum_of_cards(cards)
            if sum_in_dealer_hands > sum_in_players_hand:
                print('Dealer ' + dealer.dealer_name + ' wins')

            elif sum_in_dealer_hands < sum_in_players_hand:
                print(name.name_list[item_in_name_list] + ' wins against ' + dealer.dealer_name)

            elif sum_in_dealer_hands == sum_in_players_hand:
                if blackjack(Dealer.dealer_cards) and not blackjack(person):
                    print('Dealer ' + dealer.dealer_name + ' wins')

                elif not blackjack(Dealer.dealer_cards) and not blackjack(cards):
                    print(name.name_list[item_in_name_list] + ' wins against ' + dealer.dealer_name)

                else:
                    print('Its a push')

            item_in_name_list = item_in_name_list + 1


jack = Table()
deck = jack.get_deck(int(input('Enter number of decks needed min:1 and max:8 : ', )))
dealer = Dealer(deck)
player = Player()
number_of_players = int(input('Enter number of players min:1 and max:8 : ', ))
player.hand_for_each_player(number_of_players, deck)
name = NameList(number_of_players)
name.generate_player_list()
dealer.show_initial_cards()
players_chance(deck, player, name)
who_wins(player, dealer, name)
