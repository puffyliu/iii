# 9.將上述兩個函數改成遞迴函數。
list1 = []
def recursive_binary(n):

    if n % 2 == 1:
        mod = '1'
    else:
        mod = '0'
    list1.insert(0, mod)
    while n > 1:
        n = n // 2
        recursive_binary(n)
        break

    str1 = "".join(list1)
    return str1

def main():
    num = int(input("請輸入一正整數: "))
    print("二進位為 = ", recursive_binary(num))

main()

# 更高竿的寫法
# def recursive_binary(n):
#
#     if n // 2 == 0:     # 當n = 0 or 1
#         n = str(n)
#         return n
#     else:
#         x = n % 2
#         n = n // 2
#         s = str(x)
#         return recursive_binary(n)+s
#
# def main():
#     num = int(input("請輸入一正整數: "))
#     print("二進位為 = ", recursive_binary(num))
#
# main()
