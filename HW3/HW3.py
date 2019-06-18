#
# # 1.函數的練習-power。寫一函數power(x, n)用來計算x的n次方。
# def power(x, n):
#     total = 1
#     for i in range(1, n+1):
#         total *= x
#     return total
#
# def main():
#     num1, num2 = eval(input("請輸入兩整數: "))
#     print("{}的{}次方為{}".format(num1, num2, power(num1, num2)))
#
# main()
#
# # 2.函數的練習-sigma。 寫一函數my_fun (x, n)
# def factorial(n):
#     total1 = 1
#     for i in range(1, n+1, 1):
#         total1 *= i
#     return total1
#
# def power(x, n):
#     total2 = 1
#     for i in range(1, n+1):
#         total2 *= x
#     return total2
#
# def my_fun(x, n):
#     total3 = 0
#     for i in range(1, n+1):
#         # print(power(x, i))
#         # print(factorial(i))
#         total3 += power(x, i)/factorial(i)
#     return total3
#
# def main():
#     num1, num2 = eval(input("請輸入兩整數: "))
#     print(my_fun(num1, num2))
#
# main()
#
# # 3.寫一函數is_prime(n)用來判斷n是否為質數。
# def is_prime(n):
#     count = 0
#     for i in range(1, n+1, 1):
#         if n % i == 0:
#             count += 1
#     if count == 2:
#         return True
#     else:
#         return False
#
# def main():
#     num = int(input("請輸入一正整數: "))
#     if is_prime(num) is True:
#         print(num, "為質數!")
#     else:
#         print(num, "不為質數!")
#
# main()
#
# # 4.寫一函數get_prime(n)用來找出第n個質數。
# def is_prime(n):
#     count = 0
#     for i in range(1, n+1, 1):
#         if n % i == 0:
#             count += 1
#     if count == 2:
#         return True
#     else:
#         return False
#
# def get_prime(num):
#     count = 0
#     i = 0
#     while i >= 0:
#         i += 1
#         if is_prime(i) is True:
#             count += 1
#         if count == num:
#             # print("i = ", i)
#             return i
#             break
#
# def main():
#     num = int(input("請輸入一正整數: "))
#     print(get_prime(num))
#
# main()
#
# # 5.寫一函數is_mersenne_prime(n)用來判斷n是否為Mersenne質數。撰寫一程式找出前5個Mersenne質數。
# # 提示：若質數滿足2^P-1=n (p為正整數)，則n為Mersenne Prime。
# # 說明：當p=3時，2^3-1=7，故7為Mersenne Prime。
# def is_prime(n):
#     count = 0
#     for i in range(1, n+1, 1):
#         if n % i == 0:
#             count += 1
#     if count == 2:
#         return True
#     else:
#         return False
#
# def is_mersenne_prime():
#     count = 0
#     i = 0
#     while i >= 0:
#         i += 1
#         if is_prime(2**i - 1) and count != 5:
#             count += 1
#             print(2**i - 1)
#
# def main():
#     is_mersenne_prime()
#
# main()
#
# # 6.寫一遞迴函數factorial(n)用來計算1*2*3*…*n的值。提示：factorial(n) = n * factorial(n-1)，factorial(1)=1
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)
#
# def main():
#     num = int(input("請輸入一正整數: "))
#     print(factorial(num))
#
# main()
#
# # 7.寫一遞迴函數sum (n)用來計算2+4+6…+2n的值。
# def factorial(n):
#     if n == 1:
#         return 1*2
#     else:
#         return 2*n + factorial(n-1)
#
# def main():
#     num = int(input("請輸入一正整數: "))
#     print(factorial(num))
#
# main()
#
# # 8.輸入一整數，寫兩個函數分別為to_binary(n)和to_hexadecimal(n)用來將n轉換成二進制和十六進制的值。(勿使用任何現成的函數)
# def to_binary(n):
#     total = 0
#     count = 0
#     while n > 0:
#         a = n // 2
#         mod = n % 2
#         n = a
#         total = total/10 + mod
#         count += 1
#     return round(total*(10**(count-1)))
#
# def to_hexadecimal(n):
#     total = ''
#     while n > 0:
#         if n % 16 == 10:
#             mod = 'A'
#         elif n % 16 == 11:
#             mod = 'B'
#         elif n % 16 == 12:
#             mod = 'C'
#         elif n % 16 == 13:
#             mod = 'D'
#         elif n % 16 == 14:
#             mod = 'E'
#         elif n % 16 == 15:
#             mod = 'F'
#         elif n % 16 < 10:
#             mod = str(n % 16)
#         n = n // 16
#         total = mod + str(total)
#
#     return total
#
# def main():
#     num = int(input("請輸入一正整數: "))
#     print("二進位為 = ", to_binary(num))
#     print("十六進位為 = ", to_hexadecimal(num))
#
# main()
# 9.將上述兩個函數改成遞迴函數。
# def to_binary2(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         to_binary2(n // 2)
