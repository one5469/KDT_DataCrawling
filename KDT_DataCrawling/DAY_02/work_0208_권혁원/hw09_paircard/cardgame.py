from card import Card
from gamedealer import GameDealer
from player import Player

def cardgame():
    step = 1
    dealer = GameDealer()
    player1 = Player('흥부')
    player2 = Player('놀부')

    dealer.make_deck()
    dealer.shuffle_deck()

    print(f'[{step}]단계: 다음 단계 진행을 위해 Enter 키를 누르세요!')
    dealer.give_card(10,player1, player2)
    player1.print_info()
    print()
    print('============================================================')
    player2.print_info()
    step += 1
    input("Enter").strip()
    print()

    print(f'[{step}]단계: 다음 단계 진행을 위해 Enter 키를 누르세요!')
    print('============================================================')
    player1.check_one_pair_card()
    print('============================================================')
    player2.check_one_pair_card()
    step += 1
    input("Enter").strip()
    print()

    while not dealer.deckisEmpty():
        print(f'[{step}]단계: 다음 단계 진행을 위해 Enter 키를 누르세요!')
        print()
        print('============================================================')
        dealer.give_card(4, player1, player2)
        print('============================================================')
        player1.check_one_pair_card()
        print('============================================================')
        player2.check_one_pair_card()
        step += 1
        answer = input("Enter").strip()
        print('입력 : ', answer)
        print()

    print("게임 끝")

cardgame()