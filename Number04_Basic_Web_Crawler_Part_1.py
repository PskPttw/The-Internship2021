# Editor: 박민지

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def sortFirst(val):
    return val[0]

print("4.1. Extract Data from Source HTML")

html = urlopen('https://theinternship.io')
bs = BeautifulSoup(html, 'html.parser')
image = bs.find_all("img", "center-logos")
description = bs.select("[class~=list-company]")
text_collector = [[0 for i in range(2)] for j in range(len(description))]

count_for_des = 0
for des in description:
    temp = des.get_text()
    str_des = str(temp)
    len_des = len(str_des)
    text_collector[count_for_des][0] = len_des
    count_for_des += 1

count_for_img = 0
for img in image:
    temp = img['src']
    str_img = str(temp)
    text_collector[count_for_img][1] = str_img
    count_for_img += 1

text_collector.sort(key=sortFirst)
for i in range(len(text_collector)):
    print(str(text_collector[i][1]))

