# 改寫employee作業，將hard code在程式裡的資料，改由檔案輸入。
# 提示：
# a.import employee
# b.每一列資料代表一個員工所有的資料
# c.檔案裡的每一列資料沒有特定順序
# d.在檔案裡可增加一個職位別來表示不同的職位
# e.使用split()將字串切成tokens
# with open('employee.txt', 'w', encoding='utf-8') as f:
#     f.write("'James', 'male', '2018-07-07', '0955544432','新竹市', 30000, '一般職員\n'")
#     f.write("'Andy', 'male', '2018-06-06', '0977744432','新竹市', 50000, '二級主管\n'")
#     f.write("'Mary', 'female', '2018-08-08', '0955544487','新竹市', 87000, '一級主管\n'")
from HW6 import HW6_1
with open('employee.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    while line != '':
        list1 = line.split(',')
        if list1[6] == '一般職員\n':
            emp1 = HW6_1.NormalEmployee(list1[0], list1[1], list1[2], list1[3], list1[4], int(list1[5]))
            print(emp1)
        elif list1[6] == '二級主管\n':
            emp1 = HW6_1.SecondarySupervisor(list1[0], list1[1], list1[2], list1[3], list1[4], int(list1[5]))
            print(emp1)
        elif list1[6] == '一級主管\n':
            emp1 = HW6_1.FirstSupervisor(list1[0], list1[1], list1[2], list1[3], list1[4], int(list1[5]))
            print(emp1)
        line = f.readline()