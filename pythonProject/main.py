import requests as req
import numpy as np

import pandas as pd
from pandas import Series, DataFrame

from bs4 import BeautifulSoup

url = "https://ru.wikipedia.org/wiki/All_Things_Must_Pass"
resp = req.get(url)


soup = BeautifulSoup(resp.text, "lxml")


tags = soup.find_all("a")
#tags = soup.find_all(attrs=["title"])

print(tags)

#for iter in tags:
    #print(iter.text, iter.attrs["href"])

    #url_object = "https://www.rabota.ru" + iter.attrs["href"]
    #url_object = "https://hh.ru" + iter.attrs["href"]
    #resp_object = req.get(url_object)

    #soup_object = BeautifulSoup(resp_object.text, "lxml")
    #tag_price = soup_object.find(attrs={"itemprop":"baseSalary"}).text

    #.find(attrs={"class": "vacancy-card__salary"})

    #print(tag_price)

    #break