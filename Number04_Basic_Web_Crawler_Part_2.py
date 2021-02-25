# Editor: 박민지

from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import Flask, jsonify, make_response
import json

def sortFirst(val):
    return val[0]


app = Flask(__name__)
@app.route("/", methods=["GET"])
def getImg():
    html = urlopen('https://theinternship.io/')
    bs = BeautifulSoup(html, 'html.parser')
    image = bs.find_all("img", "center-logos")
    for i in image:
        print(i)
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

    img_address = {"companies": []}
    count_for_address = 0
    for img in text_collector:
        img_address["companies"].append({"logo": html + img[count_for_address][1]})
        count_for_address += 1

    json_temp = json.dumps(img_address, sort_keys=True, indent=4)
    json_file = jsonify(json_temp)
    return make_response(json_file, 200)


if __name__ == "__main__":
    app.run(port=8000)
