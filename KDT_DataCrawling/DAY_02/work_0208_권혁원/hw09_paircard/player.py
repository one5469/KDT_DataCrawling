from card import Card
from copy import deepcopy as dp

class Player:
    def __init__(self, name):
        self.name = name
        self.holding_card_list = []
        self.open_card_list = []

    def take_card(self, card):
        self.holding_card_list.append(card)

    def print_info(self):
        print(f'[{self.name}] Open card list: {len(self.open_card_list)}')
        self.print_card_list(self.open_card_list)
        print(f'[{self.name}] Holding card list: {len(self.holding_card_list)}')
        self.print_card_list(self.holding_card_list)

    def print_card_list(self, card_list):
        if len(card_list) == 0:
            print()
        else:
            for card in card_list:
                print(card, end=' ')
            print()

    def check_one_pair_card(self):
        print(f'[{self.name}: 숫자가 같은 한쌍의 카드 검사]')
        print('============================================================')
        sorted_holding = self.mergeSort(self.holding_card_list[:len(self.holding_card_list)//2],
                                          self.holding_card_list[len(self.holding_card_list)//2:])

        step = 0
        while step+1 < len(sorted_holding):
            if sorted_holding[step].number == sorted_holding[step+1].number:
                self.open_card_list.append(sorted_holding[step])
                self.open_card_list.append(sorted_holding[step+1])
                if sorted_holding[step] in self.holding_card_list and sorted_holding[step+1] in self.holding_card_list:
                    self.holding_card_list.remove(sorted_holding[step])
                    self.holding_card_list.remove(sorted_holding[step+1])
            step += 1

        self.print_info()

    def mergeSort(self, part1, part2):
        result = []
        if len(part1) > 1:
            part1 = self.mergeSort(part1[:len(part1)//2], part1[len(part1)//2:])
        if len(part2) > 1:
            part2 = self.mergeSort(part2[:len(part2)//2], part2[len(part2)//2:])

        idx1, idx2 = 0, 0

        while idx1 < len(part1) and idx2 < len(part2):
            if part1[idx1].number < part2[idx2].number:
                result.append(part1[idx1])
                idx1 += 1
            elif part1[idx1].number > part2[idx2].number:
                result.append(part2[idx2])
                idx2 += 1
            else:
                result.append(part1[idx1])
                idx1 += 1
                result.append(part2[idx2])
                idx2 += 1

        if idx1 < len(part1):
            result.extend(part1[idx1:])
        if idx2 < len(part2):
            result.extend(part2[idx2:])

        return result

