def get_change(n):
    if (1000-n) // 500 >= 1:
        print("500, {}".format((1000-n) // 500), end='; ')
    if ((1000-n)%500) // 100 >= 1:
        print("100, {}".format(((1000-n)%500) // 100), end='; ')
    if ((1000-n)%100) // 50 >= 1:
        print("50, {}".format(((1000-n)%100) // 50), end='; ')
    if ((1000-n)%50) // 10 >= 1:
        print("10, {}".format(((1000-n)%50) // 10), end='; ')
    if ((1000-n)%10) // 5 >= 1:
        print("5, {}".format(((1000-n)%10) // 5), end='; ')
    if ((1000-n)%5) // 1 >= 1:
        print("1, {}".format(((1000-n)%5) // 1), end='; ')
    print(end='\b')
    print(end='\b')

def main():
    a = int(input("請輸入1~999之間的消費金額:"))
    get_change(a)

main()