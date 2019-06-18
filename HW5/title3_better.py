# 有更好的寫法 用dict表示花色
# 3.經由亂數發撲克牌(52張)，分為四組列印出來。不能發出同樣的牌。
def random_poker():
    four_suits = {'spade': 0, 'heart': 1, 'diamond': 2, 'club': 3}
    card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    list_poker = []
    list_pop = [[],[],[],[]]
    for i in range(1, 53):
        list_poker.append(i)

    for j in range(4):
        for k in range(13):
            pop1 = list_poker.pop()
            list_pop[j].append(pop1)
    # print(list_pop)
    return list_pop


def main():
    print(random_poker())

main()