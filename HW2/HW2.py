# 1.利用for迴圏計算1^2-2^2+3^2-4^2+…+49^2-50^2的值。
total1 = 0
total2 = 0
for i in range(1, 50, 2):
    total1 += i**2
print(total1)
for i in range(2, 51, 2):
    total2 += i**2
print(total2)
print("結果為: ", total1 - total2)
# 數學上可以直接算出來是-1 * (1 + 2 + 3 +.....+50)

# 2.輸入一正整數，求其所有的因數。說明：36的因數為1, 2, 3, 4, 6, 9, 12, 18, 36。
num = int(input("請輸入一正整數: "))
print(num, "的因數為", end='')
for i in range(1, num+1, 1):
    if num % i == 0:
        print(i, end=' ')

# 3.一個數字若等於其所有因數的總和，則此數為perfect number。找出100以內所有的完美數。說明：6的因數為1, 2, 3，6=1+2+3，故6為完美數。
for i in range(1, 101, 1):
    total = 0
    for j in range(1, i, 1):
        if i % j == 0:
            # print("{0}是{1}的因數".format(j, i))
            total += j
    # print("因數的總和是: ", total)
    if total == i:
        print(i, "是完美數!")

# 4.Amstrong數是指一個三位數的整數，其各位數之立方和等於該數本身。找出所有的Amstrong數。說明：15^3=1^3+5^3+3^3，故153為Amstrong數。
for i in range(100, 1000, 1):
    hundred = i // 100
    ten = (i % 100) // 10
    unit = i % 10
    # print(hundred, end=' ')
    # print(ten, end=' ')
    # print(unit)
    if hundred**3 + ten**3 + unit**3 == i:
        print(i, "為阿姆斯壯數!")

# 5.輸入一正整數，找出所有小於或等於的質數。
num = int(input("請輸入一正整數: "))
# print(num, "的因數為", end='')
for i in range(1, num+1, 1):
    count = 0
    for j in range(1, i+1, 1):
        if i % j == 0:
            count += 1      # 因為質數就只有兩個因數(1跟自己)
        # print(i, "因數個數為:", count)
    if count == 2:
        print(i, "為質數!")

# 6.若有一條繩子長3000公尺，每天剪去一半的長度，需多少天繩子的長度會短於5公尺。
rope = 3000
day = 0
while rope >= 5:
    rope /= 2
    day += 1
print(day, "天")

# 7.老王養了一群兔子，若三隻三隻一數，剩餘一隻；若五隻五隻一數，剩餘三隻；若七隻七隻一數，剩餘二隻。試問兔子最少有幾隻。
rabbit = 1
while rabbit % 3 != 1 or rabbit % 5 != 3 or rabbit % 7 != 2:
    rabbit += 1
print("兔子有{}隻".format(rabbit))

# 8.出現”請輸入密碼”的提示，使用者有最多三次輸入的機會。
# 若輸入正確，則印出”密碼輸入正確，歡迎使用本系統！”。
# 若輸入不正確，再次出現”請輸入密碼”的提示。
# 若三次輸入不正確，則印出”密碼輸入超過三次！”，並結束程式的執行。
error = 0
while input("請輸入密碼: ") != '123':
    error += 1
    if error == 3:
        print("密碼輸入超過三次！")
        break
else:
    print("密碼輸入正確，歡迎使用本系統！")

# 9.畫出下列三種排列的星星圖形。
#
#  (1)	*         (2)   * * * * *    (3)  	 *
#       * *               * * * *           *  *
#       * * *               * * *          *  *  *
#       * * * *               * *         *  *  *  *
#       * * * * *               *        *  *  *  *  *
# (1)
for i in range(1, 6, 1):
    for j in range(1, i, 1):
        print("*", end=' ')
    print("*")
# (2)
for i in range(6, 0, -1):
    for j in range(1, i, 1):
        print("*", end=' ')
    print("")
# (3)
for i in range(1, 6, 1):
    print(" " * (5 - i), end='')
    for j in range(1, i+1, 1):
        print("*", end=' ')
    print("")

# 10.印出下列九九乘法表：
#    		|	1	2	3	4	5	6	7	8	9
#     -----------------------------------------------------------------
#      9	|	9	18	27	36	45	54	63	72	81
#      8	|	8	16	24	32	40	48	56	64
#      7	|	7	14	21	28	35	42	49
#      6	|	6	12	18	24	30	36
#      5	|	5	10	15	20	25
#      4	|	4	8	12	16
#      3	|	3	6	9
#      2	|	2	4
#      1	| 	1
print("   |   ", end=' ')
for k in range(1, 10, 1):
    print(k, end='\t')
print("")
print("-------------------------------------------------")
for i in range(9, 0, -1):
    print(i, ' | ', end='\t')
    for j in range(1, i+1, 1):
        print(i*j, end='\t')
    print("")

# 11.錢精打以10%單利投資100000元，郝細算則以5%複利投資100000元。計算多少年後郝細算的投資可以超過錢精打，並將此時兩人錢數印出。(27年後)
# 提示：單利公式：P(1+r*n)    複利公式：P(1+r)n  P：本金，r：利率，n：多少年
n = 1
while 100000*(1 + 0.1 * n) >= 100000*(1.05 ** n):
    n += 1
    sumA = 100000 * (1 + 0.1 * n)
    sumB = 100000 * (1.05 ** n)
print(n, "年")
print("錢精打的投資金額: ", sumA)
print("錢精打的投資金額: ", sumB)

# 12.錢不精以100000元分別向銀行、當鋪和地下錢莊借貸。
# 若銀行的年利率為20%，當鋪月利率為10%和地下錢莊日利率為1%。以月為單位，計算一個月後至一年後每個月該歸還多少錢。以單利來算
for i in range(1, 13):
    print("第{}個月".format(i), end='\t')
    print("銀行 = ", round(100000*(1 + 0.2 * i / 12), 3), end='\t')
    print("當鋪 = ", round(100000*(1 + 0.1 * i), 3), end='\t')
    print("地下錢莊 = ", round(100000*(1 + 0.01 * i * 30), 3), end='\t')
    print("")

