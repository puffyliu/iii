def to_hexadecimal(n):
    total = ''
    hexdict = {'10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}
    while n > 0:
        if str(n % 16) in hexdict.keys():
            mod = hexdict.get(str(n % 16))
        elif n % 16 < 10:
            mod = str(n % 16)
        n = n // 16
        total = mod + str(total)
    return total

def main():
    num = int(input("請輸入一正整數: "))
    print("十六進位為 = ", to_hexadecimal(num))

main()
