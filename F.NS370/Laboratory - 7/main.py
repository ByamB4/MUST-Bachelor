from lxml import html 
import requests 
from tabulate import tabulate

TARGET = 'https://ikon.mn/xrates'

page = requests.get(TARGET) 

tree = html.fromstring(page.content)

# /div/div[1]/h4[1]/text()

idename = tree.xpath('//div[@id="idailyexchange"]/ul/li/div[@class="idename"]/a/text()') 
idevalue = tree.xpath('//div[@id="idailyexchange"]/ul/li/div[@class="idevalue"]/a/text()') 
print(tabulate([idevalue], headers=idename))

