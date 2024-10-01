from lxml import etree
import requests
import csv

url = "https://prts.wiki/w/%E6%8E%A2%E7%B4%A2%E8%80%85%E7%9A%84%E9%93%B6%E5%87%87%E6%AD%A2%E5%A2%83/%E4%BB%AA%E5%BC%8F%E7%94%A8%E5%93%81%E7%B4%A2%E5%BC%95"
html = requests.get(url).text
# print(html)
tree = etree.HTML(html)
print(tree)

# 去除字符串的开头和结尾的空白字符
def clean_space(elements_list):
    element = [element.strip() for element in elements_list if '\n' not in element]
    return element


No_list = tree.xpath('//table[@class="wikitable logo"]/tbody/tr[1]/th[1]/text()')
# print(len(No_list))
# print(No_list)
Name_element_list = tree.xpath('//table[@class="wikitable logo"]/tbody/tr[1]/th[2]')
Name_list = [etree.tostring(Name, method='text', encoding='unicode').strip() for Name in Name_element_list]
# print(len(Name_list))
# print(Name_list)
# price_list = tree.xpath('//table[@class="wikitable logo"]/tbody/tr[3]/td/div//span[1]/text()')#220~228 238~241无价
# print(len(price_list))
# print(price_list)
text_list = tree.xpath('//table[@class="wikitable logo"]/tbody/tr[3]/td/b')
text_list = [element.text for element in text_list]
print(len(text_list))
print(text_list)

data = [
    No_list
    ,Name_list
    ,text_list
]
data = list(zip(*data))

with open("./data.csv","w",newline="") as f:
    f = csv.writer(f)
    f.writerows(data)




    