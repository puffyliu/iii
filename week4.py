# c 單位進貨成本 1~100
# r 單位零售價格 1~100 但比c大
# # N 需求的可能個數 為8(範圍是0~8)
# #  q 訂貨量
# 第5列~第13列是機率
import math
from decimal import *
def paper_benefit(c, r, n, q):
    profit = 0
    rest = 0
    demand = {}
    for i in range(9):
        probability = float(input("請輸入賣出{}份報紙的機率:".format(i)))
        demand[str(i)] = probability

    for i in range(q+1):
        if i == q:
            profit += Decimal(str(i*r-c*q)) * Decimal(str(1 - rest))
        else:
            profit += Decimal(str(i*r-c*q)) * Decimal(str(demand.get(str(i))))
        rest += Decimal(str(demand.get(str(i))))
    return math.floor(profit)

def main():
    cost = int(input("請輸入單位進貨成本:"))
    price = int(input("請輸入單位零售價格:"))
    number = int(input("請輸入需求的可能個數:"))
    quantity = int(input("請輸入訂貨量:"))
    print("預期利潤為:", paper_benefit(cost, price, number, quantity))

main()