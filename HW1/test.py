# 4.輸入一西元年，如2015。判斷此年份是否為閏年。提示：每四年一閏，每百年不閏，每四百年一閏，每四千年不閏。
year = int(input("請輸入西元年:"))
if year % 4 == 0:
    if year % 4 == 0 and year % 100 == 0:
        if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
            if year % 4 == 0 and year % 100 == 0 and year % 400 == 0 and year % 4000 == 0:
                print(year, "不是閏年")
            else:
                print(year, "是閏年")
        else:
            print(year, "不是閏年")
    else:
        print(year, "是閏年")
else:
    print(year, "不是閏年")
