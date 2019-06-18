# 1.輸入月份1~12月，判斷相對應的季節春、夏、秋、冬並印出。若不在此範圍則印出”輸入錯誤”。\
year = int(input("請輸入月份: "))
if year in (1, 2, 3):
    print("春啦")
elif year in (4, 5, 6):
    print("夏啦")
elif year in (7, 8, 9):
    print("秋啦")
elif year in (10, 11, 12):
    print("冬啦")
else:
    print("輸入錯誤")

# 2.輸入便利商店工讀生的工作時數，並計算其薪資。
#   60小時以內，時薪120元。
#   61~80小時，以時薪1.25倍計算。
#   81小時以上，以時薪1.5倍計算。
#   說明：薪資以累計方式計算。若工時為90小時，則薪資為60*120 + 20*120*1.25 + 10*120*1.5元。
workhour = int(input("請輸入你的工作時數: "))
if workhour <= 60:
    print("薪資 = ", 120*workhour, "元")
elif workhour in range(61, 80):
    print("薪資 = ", 120*60 + 120*1.25*(workhour - 60), "元")
elif workhour >= 81:
    print("薪資 = ", 120*60 + 120*1.25*20 + 120*1.5*(workhour - 80), "元")

# 3.輸入何種用電和度數，計算出需繳之電費。電力公司使用累計方式來計算電費，分工業用電及家庭用電。
elec = input("請輸入用電種類: ")
kwh = eval(input("請輸入使用度數: "))  # 理論上要排掉負數
if kwh < 0:
    print("請輸入正數")
else:
    print("請稍後")
if elec == "家庭用電":
    if kwh <= 240:
        print("用電共", 0.15*kwh, "度")
    elif kwh in range(241, 540):
        print("用電共", 0.15*240 + 0.25*(kwh - 240), "度")
    elif kwh > 540:
        print("用電共", 0.15 * 240 + 0.25 * 300 + 0.45*(kwh - 540), "度")
elif elec == "工業用電":
    if kwh <= 240:
        print("用電共", 0.45*kwh, "度")
    elif kwh in range(241, 540):
        print("用電共", 0.45*kwh, "度")
    elif kwh > 540:
        print("用電共", 0.45*kwh, "度")
else:
    print("用電種類輸入錯誤!")

# 4.輸入一西元年，如2015。判斷此年份是否為閏年。提示：每四年一閏，每百年不閏，每四百年一閏，每四千年不閏。
year = int(input("請輸入西元年:"))
if year % 4000 == 0:
    print(year, "不是閏年")
elif year % 400 == 0:
    print(year, "是閏年")
elif year % 100 == 0:
    print(year, "不是閏年")
elif year % 4 == 0:
    print(year, "是閏年")
else:
    print("你是外星人吧")

# 5.輸入在某商店購物應付金額與實付金額。實付金額小於應付金額，則印出”金額不足”。實付金額等於應付金額，則印出”不必找錢”。實付金額大於應付金額，則輸出找回金額最少的鈔票數和錢幣數。
payable = int(input("請輸入應付金額:"))
pay = int(input("請輸入實付金額:"))
if pay < payable:
    print("金額不足")
elif pay == payable:
    print("不必找錢")
else:
    print("應找回")
    if (pay - payable) >= 500:
        print((pay - payable) // 500, "張500元")
    if (pay - payable) % 500 >= 100:
        print(((pay - payable) % 500) // 100, "張100元")
    if (pay - payable) % 100 >= 50:
        print(((pay - payable) % 100) // 50, "個50元硬幣")
    if (pay - payable) % 50 >= 10:
        print(((pay - payable) % 50) // 10, "個10元硬幣")
    if (pay - payable) % 10 >= 5:
        print(((pay - payable) % 10) // 5, "個5元硬幣")
    if (pay - payable) % 5 >= 1:
        print(((pay - payable) % 5) // 1, "個1元硬幣")
# 不確定是否要加else狀況

# 6.一元二次方程式ax2+bx+c=0。輸入a, b, c三值，並計算方程式的根。b2-4ac > 0，有兩個不相等的實根。b2-4ac = 0，有兩個不相等的實根。b2-4ac < 0，則印出”沒有實根"。
import math
a = eval(input("請輸入a的值: "))
b = eval(input("請輸入b的值: "))
c = eval(input("請輸入c的值: "))
if (b**2) - (4*a*c) > 0:
    print("有兩個不相等的實根")
    print("x = ", -b + math.sqrt((b**2) - (4*a*c))/(2*a))
    print("x = ",  -b - math.sqrt((b**2) - (4*a*c))/(2*a))
elif (b**2) - (4*a*c) == 0:
    print("有兩個相等的實根")
    print("x = ", -b/(2*a))
elif (b**2) - (4*a*c) < 0:
    print("沒有實根")