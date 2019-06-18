# 1.寫一函數is_id (_id)用來判斷_id是否為正確身份証字號。
# def is_id(_id):
#     list_code = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'T', 'U', 'V', 'W', 'X', 'Z']
#     list_int = [10, 11, 12, 13, 14, 15, 16, 17, 34, 18, 19, 21, 22, 35, 23, 24, 27, 28, 29, 32, 30, 33]
#     list_id = list(_id)
#     x = list_code.index(list_id[0])
#     if list_id[0] in list_code and list_id[1] in (1, 2):
#         a = list_int[x] // 10
#         b = list_int[x] % 10
#         result = a*1 + b*9 + int(list_id[1])*8 + int(list_id[2])*7 + int(list_id[3])*6 + int(list_id[4])*5 + int(list_id[5])*4 + int(list_id[6])*3 + int(list_id[7])*2 + int(list_id[8])*1 + int(list_id[9])*1
#         # print(result)
#         #
#         if result % 10 == 0:
#             return True
#         else:
#             return False
#     else:
#         return False
#
# def main():
#     idno = input("請輸入身分證字號:")
#     # print(idno)
#     if is_id(idno) is True:
#         print("此為有效身分證字號!")
#     else:
#         print("不是正確的身分證字號!")
#
# main()
# 2.輸入地區和性別，經由亂數產生一個身份証字號。
# import random
# def random_id(area, gender):
#     list_code = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'T', 'U', 'V', 'W', 'X', 'Z']
#     list_int = [10, 11, 12, 13, 14, 15, 16, 17, 34, 18, 19, 21, 22, 35, 23, 24, 27, 28, 29, 32, 30, 33]
#     list_area = ['臺北市','臺中市','基隆市','臺南市','高雄市','新北市','宜蘭縣','桃園市','嘉義市','新竹縣','苗栗縣','南投縣','彰化縣','新竹市','雲林縣','嘉義縣','屏東縣']
#
#     try:
#         list_id = []
#         if area in list_area:
#             area_index = list_area.index(area)
#             int_index = list_int[area_index]
#             # print("area_index = ", area_index)
#             # print("int_index = ", int_index)
#             # print("list_code = ", list_code[area_index])
#             list_id.append(int_index // 10)
#             list_id.append(int_index % 10)
#         else:
#             raise ValueError
#         if gender == '男':
#             list_id.append(1)
#         elif gender == '女':
#             list_id.append(2)
#         else:
#             raise ValueError
#
#         for i in range(7):
# #             list_id.append(random.randint(1, 9))
#         # print("list_id2 = ", list_id)     # 除了最後一碼驗證碼以外
#
#         result = int(list_id[0]) * 1 + int(list_id[1]) * 9 + int(list_id[2]) * 8 + int(list_id[3]) * 7 + int(list_id[4]) * 6 + int(
#             list_id[5]) * 5 + int(list_id[6]) * 4 + int(list_id[7]) * 3 + int(list_id[8]) * 2 + int(
#             list_id[9]) * 1
#         # print(result)
#         if result % 10 == 0:
#             list_id.append(0)
#         else:
#             list_id.append(10 - (result % 10))
#         # print(list_id)
#         # print(list_id[2:])    # 擷取除了開頭字母以外的部分
#         str1 = (list(list_code[area_index]) + list_id[2:])
#         # print("str1 = ", str1)
#         str2 = '%s' * len(str1) % tuple(str1)
#         return str2
#     except ValueError:
#         print("你是住在外太空還是變性人嗎!")
#
# def main():
#     area = input("請輸入縣市:")
#     gender = input("請輸入性別:")
#     print(random_id(area, gender))
#
# main()
# 3.經由亂數發撲克牌(52張)，分為四組列印出來。不能發出同樣的牌。
# import random
# def random_poker():
#     list_poker = []
#     list_pop = [[],[],[],[]]
#     for i in range(1, 53):
#         list_poker.append(i)
#
#     for j in range(4):
#         for k in range(13):
#             pop1 = list_poker.pop(random.randint(0, len(list_poker)-1))
#             list_pop[j].append(four_suits(pop1))
#     # print(list_pop)
#     return list_pop
#
# def four_suits(card):
#     str1 = ''
#     if 1 <= card <= 13:
#         str1 = '黑桃' + str(card)
#     elif 14 <= card <= 26:
#         str1 = '紅心' + str(card-13)
#     elif 27 <= card <= 39:
#         str1 = '方塊' + str(card-26)
#     elif 40 <= card <= 52:
#         str1 = '梅花' + str(card-39)
#
#     return str1
#
# def main():
#     print(random_poker())
#
# main()
# 4. 可怕的萬年曆