from card import Card
import random

class GameDealer:
    def __init__(self):
        self.deck = []
        self.suit_number = 13

    def print_deck(self):
        print('------------------------------------------------------------')
        cnt = 0
        print('[GameDealer] 딜러가 가진 카드 수:', len(self.deck))
        for card in self.deck:
            print(card, end=' ')
            cnt += 1
            if cnt % 13 == 0:
                print()
        if cnt % 13 != 0:
            print()

    def make_deck(self):
        card_suits = ["♠", "♥", "♣", "◆"]
        card_numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        print('[GameDealer] 초기 카드 생성')
        for suit in card_suits:
            for num in card_numbers:
                self.deck.append(Card(suit, num))
        self.print_deck()

    def shuffle_deck(self):
        print('[GameDealer] 카드 랜덤하게 섞기')
        random.shuffle(self.deck)

        self.print_deck()

    def give_card(self, limit, *players):
        print(f'카드 나누어 주기: {limit}장')
        for n in range(limit):
            for p in players:
                p.take_card(self.deck.pop())

        self.print_deck()

    def deckisEmpty(self):
        if len(self.deck) == 0:
            return True
        else:
            return False