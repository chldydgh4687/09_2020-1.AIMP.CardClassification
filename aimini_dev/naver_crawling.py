import re
import requests
from bs4 import BeautifulSoup
import os


def getImage(list_file, output_f,keyword,no):

    BASE_DIR = './NAVER/' + list_file
    os.mkdir(BASE_DIR +'/'+ output_f)
    try:
        url="https://search.naver.com/search.naver?where=image&sm=tab_jum&query="+keyword
        html = requests.get(url)
        bs_html = BeautifulSoup(html.content,"html.parser")
        photowall = bs_html.find('div',{"class":"photowall"})
        img_list = photowall.find_all("img",{"class":"_img"})
    except:
        pass
    else:
        for i in range(no):
            try:
                img_link = re.findall('data-source="(.+?)"', str(img_list[i]))[0]
            except:
                i = i - 1
                continue
            img_con = requests.get(img_link).content
            file = open(BASE_DIR + '/' + output_f + '/' + keyword + str(i + 1) + ".jpg", "wb")
            file.write(img_con)
            file.close()
            print (str(i)+'/'+str(no)+' success\n')




