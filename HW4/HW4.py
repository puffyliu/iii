# 1.事先將10個數字置於串列中，分別找出10個數字中最大的值和最小的值。(勿使用現成的函數)
# list1 = [30, 3, 69, 6, 7, 9, 1, 5, 55, 11]
# max = list1[0]
# for i in range(0, len(list1)-1):
#     if max > list1[i+1]:
#         max = max
#     else:
#         max = list1[i+1]
# print("最大的值: ", max)
#
# min = list1[0]
# for i in range(0, len(list1)-1):
#     if min < list1[i+1]:
#         min = min
#     else:
#         min = list1[i+1]
# print("最小的值: ", min)

# 2.a~d各小題皆以一函數來處理：為練習串列的參數傳遞，陣列需定義為main()的區域變數，事先將12個數字置於一3 x 4的二維串列中，列印各函數的結果。
# a.計算所有數字的平均值
# b.找出12個數字中最大的值
# c.找出12個數字中最小的值
# d.計算每組內4個數字的平均值
# list1 = [[4, 90, 41, 59], [18, 94, 51, 59], [2, 93, 3, 15]]
# def list_avg():
#     sum = 0
#     for i in range(len(list1)):
#         for j in range(len(list1[i])):
#             # print(list1[i][j])
#             sum += list1[i][j]
#     return sum / 12
#
# def list_max():
#     max = list1[0][0]
#     for i in range(len(list1)):
#         for j in range(len(list1[i])):
#             if max > list1[i][j]:
#                 max = max
#             else:
#                 max = list1[i][j]
#     return max
#
# def list_min():
#     min = list1[0][0]
#     for i in range(len(list1)):
#         for j in range(len(list1[i])):
#             # print("list1[i][j] = ", list1[i][j], end='  ')
#             if min < list1[i][j]:
#                 min = min
#             else:
#                 min = list1[i][j]
#             # print("i = {} j = {} min = {}".format(i, j, min))
#     return min
#
# def list_ravg():
#     list2 = []
#     for i in range(len(list1)):
#         rsum = 0
#         for j in range(len(list1[i])):
#             # print(list1[i][j])
#             rsum += list1[i][j]
#         ravg = rsum / len(list1[i])
#         list2.append(ravg)
#         # print("rsum = ", rsum)
#     # print("ravg = ", list2)
#     return list2
#
# def main():
#     print("avg = ", list_avg())
#     print("max = ", list_max())
#     print("min = ", list_min())
#     print("ravg = ", list_ravg())
# main()

# 3.某一公司有五種產品A、B、C、D與E，其單價分別為12、16、10、14與15元；而該公司共有三位銷售員，他們在某月份的銷售數量如下所示
#
# 銷售員	產品A	產品B	產品C	產品D	產品E
# Jean	    33	    32	    56	    45	    33
# Tom	    77	    33	    68	    45	    23
# Tina	    43	    55	    43	    67	    65
# 試計算：
# a.	每一個銷售員的銷售總金額
# b.	有最好業績（銷售總金額最多者）的銷售員
# c.	每一項產品的銷售總金額
# d.	銷售總金額最多的產品
# list1 = [[33, 32, 56, 45, 33], [77, 33, 68, 45, 23], [43, 55, 43, 67, 65]]
# salesman = ['Jean', 'Tom', 'Tina']
# product = ['A', 'B', 'C', 'D', 'E']
# price = [12, 16, 10, 14, 15]
# # a.
# def sales_sum():
#     for i in range(len(list1)):
#         list_sum = []
#         row_sum = 0
#         for j in range(len(list1[i])):
#             # print(list1[i][j], end=' ')
#             # print("price = ", price[j])
#             row_sum += price[j] * list1[i][j]
#         list_sum.append(row_sum)
#         print("{}的銷售總金額為{}元".format(salesman[i], list_sum[0]))
# # 有機會看能不能改成給名字印出銷售金額
# # b.
# def get_max_salesman():
#     list_sum = []
#     for i in range(len(list1)):
#         row_sum = 0
#         for j in range(len(list1[i])):
#             row_sum += price[j] * list1[i][j]
#         list_sum.append(row_sum)
#
#     max_sum = list_sum[0]
#     sales = 0
#     for i in range(0, len(list_sum) - 1):
#         if max_sum > list_sum[i+1]:
#             max_sum = max_sum
#         else:
#             max_sum = list_sum[i+1]
#             sales = i+1
#     # print("最大的值: ", max_sum)
#     # print("sales = ", salesman[sales])
#     return salesman[sales]
# # c.
# def product_sum(n):
#     row_sum = 0
#     for i in range(len(list1)):
#         row_sum += price[n] * list1[i][n]
#     return row_sum
#
# # d.
# def get_max_product():
#     list_sum = []
#     a = len(list1)
#     for i in range(len(list1[0])):
#         col_sum = 0
#         for j in range(a):
#             col_sum += price[i] * list1[j][i]
#         list_sum.append(col_sum)
#     # print(list_sum)
#
#     max_sum = list_sum[0]
#     prod = 0
#     for i in range(0, len(list_sum) - 1):
#         if max_sum > list_sum[i+1]:
#             max_sum = max_sum
#         else:
#             max_sum = list_sum[i+1]
#             prod = i+1
#     return product[prod]
#
# def main():
#     sales_sum()
#     print("銷售額最高的是", get_max_salesman())
#     num = int(input("請輸入產品編號(A為0，B為1，C為2，D為3，E為4): "))
#     print("產品{}的銷售總金額為{}元".format(product[num], product_sum(num)))
#     print("銷售總金額最多的產品為:", get_max_product())
# main()

# 4.輸入一字串，字串為”all” 表示計算60個月的總平均降雨量，”year”、”season”和”month”分別表示計算某年、某季或某月的平均降雨量。若為後三者，再輸入一個正整數表示那一年、那一季或那一月。
# 說明：5年12個月的降雨量以三維陣列形式事先給好60個浮點數
# 需做誤錯處理：
# a.	輸入除了”all”、”year”、”season”和”month”以外的字串
# b.	若輸入”year”，而正整數輸入1至5以外的數字
# c.	若輸入”season”，而正整數輸入1至4以外的數字
# d.	若輸入”month”，而正整數輸入1至12以外的數字
list2 = [[[88.97, 55.34, 22.42], [41.68, 46.72, 34.74], [7.29, 35.24, 15.83], [34.61, 43.51, 51.87]],   # 478.22
         [[4.73, 7.17, 14.37], [33.66, 63.22, 73.55], [3.84, 38.6, 27.76], [44.51, 87.45, 22.0]],
         [[52.15, 25.65, 97.24], [73.32, 52.65, 86.08], [77.92, 90.8, 92.16], [29.17, 87.51, 58.0]],
         [[9.23, 80.75, 31.92], [51.73, 91.44, 21.45], [24.88, 6.85, 4.99], [60.05, 24.92, 17.51]],
         [[76.03, 55.63, 4.03], [41.71, 21.75, 33.68], [21.71, 42.75, 53.68], [13.54, 88.6, 77.76]]]

def rainfull(str, n=0):
    if str == 'all':
        sum_all = 0
        for i in range(len(list2)):
            for j in range(len(list2[i])):
                for k in range(len(list2[i][j])):
                    # print("list2[{}][{}] = {}".format(i,j,list2[i][j]))
                    sum_all += list2[i][j][k]
        print("sum_all = ", round(sum_all, 2))
        print("avg = ", round(sum_all/60, 4))
    elif str == 'year':
        sum_year = 0
        for j in range(len(list2[n])):
            for k in range(len(list2[n][j])):
                sum_year += list2[n][j][k]
        print("第{}年的總降雨量為{}".format(n+1, round(sum_year, 2)))
    elif str == 'season':
        sum_season = 0
        for i in range(len(list2)):
            for k in range(len(list2[i][n])):
                sum_season += list2[i][n][k]
        print("sum_season = ", round(sum_season, 2))
    elif str == 'month':
        sum_month = 0
        if 0 <= n <= 2:
            for i in range(len(list2)):
                # print("list2 = ", list2[i][0][n])
                sum_month += list2[i][0][n]
            print("sum_month = ", sum_month)
        if 3 <= n <= 5:
            for i in range(len(list2)):
                sum_month += list2[i][1][n-3]
            print("sum_month = ", sum_month)
        if 6 <= n <= 8:
            for i in range(len(list2)):
                sum_month += list2[i][2][n-6]
            print("sum_month = ", sum_month)
        if 9 <= n <= 11:
            for i in range(len(list2)):
                sum_month += list2[i][3][n-9]
            print("sum_month = ", sum_month)


def main():
    try:
        string = str(input("請輸入: "))
        if string not in ('all', 'year', 'season', 'month'):
            raise TypeError
        if string in ('year', 'season', 'month'):
            num = int(input("請輸入: "))
        if string == 'year' and num not in (1, 2, 3, 4, 5):
            raise ValueError
        elif string == 'season' and num not in (1, 2, 3, 4):
            raise ValueError
        elif string == 'month' and (num > 12 or num < 1):
            raise ValueError
    except ValueError:
        print("請輸入正確範圍!")
    except TypeError:
        print("請輸入正確的字串!")
    else:
        if string == 'all':
            rainfull(string)    # 懶得改成print
        else:
            rainfull(string, num - 1)   # 懶得改成print

main()

