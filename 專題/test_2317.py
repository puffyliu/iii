from selenium.webdriver import Chrome
import time
import os

from selenium.webdriver.support.select import Select

driver = Chrome("./chromedriver")

driver.get("https://www.cnyes.com/twstock/ps_historyprice/2317.htm")
driver.find_element_by_id("ctl00_ContentPlaceHolder1_startText").clear()
time.sleep(5)
select_year = Select(driver.find_element_by_class_name('datepicker_newYear'))
select_year.select_by_visible_text(u"2010")
time.sleep(5)
select_month = Select(driver.find_element_by_class_name('datepicker_newMonth'))
select_month.select_by_visible_text(u"September")
time.sleep(5)
table1 = driver.find_element_by_class_name('datepicker')
table_rows = table1.find_elements_by_tag_name('tr')
row1_col2 = table_rows[1].find_elements_by_tag_name('td')[4].text   # 取第一列第4個元素(空的也算)，問題:不可能事先知道每個月的空格位置，還有怎麼點這一塊
print(row1_col2)

