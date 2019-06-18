# 1.有一小公司，其人事薪資的制度如下：
# 公司每個員工皆有姓名、性別、到職日、電話和住址等基本資料。
# 一般職員只有本薪；一級主管則另有本薪、午餐津貼、交通津貼和職務加給；二級主管則有本薪、午餐津貼和職務加給。午餐津貼為1800元，交通津貼為2000元，職務加給一級主管為5000元，二級主管為3000元。
# 每個員工皆有可能加班，加班費為本薪除以240乘以1.5倍再乘以加班時數。
# 在main()中產生六個實例分別為一級主管、二級主管及一般職員且分有加班及無加班兩種(資料直接透過建構子hard code在程式中)，並列印其基本資料及當月薪資。
class Employee:
    def __init__(self, name, gender, hiredate, tel, address):
        self.name = name
        self.gender = gender
        self.hiredate = hiredate
        self.tel = tel
        self.address = address

class NormalEmployee(Employee):
    def __init__(self, name, gender, take_date, tel, address, salary):
        super(NormalEmployee, self).__init__(name, gender, take_date, tel, address)
        self.salary = salary

    def overtime(self):
        ot_hours = eval(input("請輸入加班時數:"))
        ot_salary = self.salary / 240 * 1.5 * ot_hours
        return ot_salary

    def total_salary(self):
        return self.salary + self.overtime()

    def __str__(self):
        return "姓名:{}, 性別:{}, 到職日:{}, 電話:{}, 地址:{}, 本薪:{}元, 本月薪資:{}元".format(self.name, self.gender, self.hiredate, self.tel, self.address, self.salary, self.total_salary())

class SecondarySupervisor(NormalEmployee):
    def __init__(self, name, gender, take_date, tel, address, salary, lunch=1800, allowance=3000):
        super(SecondarySupervisor, self).__init__(name, gender, take_date, tel, address, salary)
        self.lunch = lunch
        self.allowance = allowance

    def total_salary(self):
        return super(SecondarySupervisor, self).total_salary() + self.lunch + self.allowance

    def __str__(self):
        return super(SecondarySupervisor, self).__str__() + ", 午餐津貼:{}, 職務加給:{}".format(self.lunch, self.allowance)

class FirstSupervisor(SecondarySupervisor):
    def __init__(self, name, gender, take_date, tel, address, salary, lunch=1800, allowance=5000, traffic=2000):
        super(FirstSupervisor, self).__init__(name, gender, take_date, tel, address, salary, lunch, allowance)
        self.traffic = traffic

    def total_salary(self):
        return super(FirstSupervisor, self).total_salary() + self.traffic

    def __str__(self):
        return super(FirstSupervisor, self).__str__() + ", 交通津貼:{}".format(self.traffic)

# def main():
#     tom = FirstSupervisor('Tom', 'male','2019-05-23', '0932316326', '新北市', 87000)               # 一級主管
#     tina = SecondarySupervisor('Tina', 'female', '2018-01-01', '0932111222', '桃園市', 50000)      # 二級主管
#     eric = NormalEmployee('Eric', 'male', '2018-09-01', '0932777888', '高雄市', 30000)             # 一般職員
#     print(tom)
#     print(tina)
#     print(eric)
#
# main()