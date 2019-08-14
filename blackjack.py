from deck import Table, get_deck, random
from dealer import Dealer
from player import Player, hit_or_stand
from Players_Name_list import NameList


def show_table(player, name):
    item_in_name_list = 0
    for cards in player.players_card:
        print(name.name_list[item_in_name_list] + ' cards: {}'.format(cards))
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
        print('\n' * 2)
        print('Current Player: ', end='')
        print(name.name_list[item_in_name_list])
        print('Cards: ', end='')
        print(cards)
        players_choice = hit_or_stand()

        while players_choice == 'h':
            total_sum_in_hand = get_score(deck, cards)
            if total_sum_in_hand > 21:
                print(name.name_list[item_in_name_list] + ' you are busted')
                print('\n' * 2)
                copy_players_card.remove(cards)
                break

            players_choice = hit_or_stand()
        item_in_name_list = item_in_name_list + 1
    player.players_card = copy_players_card.copy()


def blackjack(cards_list):
    count_for_blackjack = 0

    if 'J' in cards_list or 'Q' in cards_list or 'K' in cards_list:
        count_for_blackjack = count_for_blackjack + 1

    if 'A' in cards_list:
        count_for_blackjack = count_for_blackjack + 1

    if count_for_blackjack == 2:
        return True


def who_wins(player, dealer, name):
    print('Dealers hole card value is: ', end='')
    dealer.show_hole_card()
    print('\n' * 2)
    sum_in_dealer_hands = get_sum_of_cards(dealer.dealer_cards)

    if not len(player.players_card):
        print('Dealer ' + dealer.dealer_name + ' wins')
        print('\n' * 2)

    elif sum_in_dealer_hands < 17:
        print('Dealer making hit')

        while sum_in_dealer_hands < 17:
            sum_in_dealer_hands = get_score(deck, dealer.dealer_cards)

        print(dealer.dealer_cards)

    if sum_in_dealer_hands > 21:
        print('Dealer gets BUSTED')
        item_in_name_list = 0
        for cards in player.players_card:
            print(name.name_list[item_in_name_list] + ' wins against ' +
                  dealer.dealer_name + ' the dealer')
            print('\n' * 2)
            item_in_name_list = item_in_name_list + 1

    else:
        item_in_name_list = 0
        for cards in player.players_card:
            sum_in_players_hand = get_sum_of_cards(cards)
            if sum_in_dealer_hands > sum_in_players_hand:
                print('Dealer ' + dealer.dealer_name + ' wins')
                print('\n' * 2)

            elif sum_in_dealer_hands < sum_in_players_hand:
                print(name.name_list[item_in_name_list] + ' wins against ' +
                      dealer.dealer_name + ' the dealer')
                print('\n' * 2)

            elif sum_in_dealer_hands == sum_in_players_hand:
                if blackjack(Dealer.dealer_cards) and not blackjack(cards):
                    print('Dealer ' + dealer.dealer_name + ' wins')
                    print('\n' * 2)

                elif not blackjack(Dealer.dealer_cards) and not blackjack(cards):
                    print(name.name_list[item_in_name_list] + ' wins against ' +
                          dealer.dealer_name + ' the dealer')
                    print('\n' * 2)

                else:
                    print('Its a push')
                    print('\n' * 2)

            item_in_name_list = item_in_name_list + 1


jack = Table()
deck = get_deck(int(input('Enter number of decks needed min:1 and max:8 : ', )))
dealer = Dealer(deck)
player = Player()
number_of_players = int(input('Enter number of players min:1 and max:8 : ', ))
player.hand_for_each_player(number_of_players, deck)
name = NameList(number_of_players)
name.generate_player_list()
dealer.show_initial_cards()
players_chance(deck, player, name)
who_wins(player, dealer, name)