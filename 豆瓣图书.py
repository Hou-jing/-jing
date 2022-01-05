import selenium
from selenium import webdriver
import openpyxl
from openpyxl import workbook
webdriver=webdriver.Chrome('C:\\Program Files (x86)\\Google\\Update\\1.3.36.112\\chromedriver.exe')
webdriver.get('https://book.douban.com/top250?icn=index-book250-all')
#爬取名称、连接、图书评分
item=webdriver.find_elements_by_class_name('item')
items=[]
for i in item:
    pl2=i.find_element_by_class_name('pl2').find_element('a')
    print(pl2,pl2.text)
    link=pl2['href']
    name=pl2.text
    score=i.find_element_by_class_name('rating_nums').text
    text=[link,name,score]
    items.append(text)
wb=openpyxl.Workbook()
sheet=wb.active
for data in items:
    sheet.append(data)
wb.save('豆瓣图书.xlsx')
