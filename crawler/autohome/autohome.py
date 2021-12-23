#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : Liu Kun
# date   : 2021-09-19 23:39:01
import json
import re
import time
import requests

from bs4 import BeautifulSoup
from utils import kit_config, kit_mysql

# https://www.autohome.com.cn/Ashx/AjaxHeadArea.ashx?OperType=GetAreaInfo&VarName=areaData&CityId=440300
# https://carif.api.autohome.com.cn/car/SpecificConfig_GetListBySpecList.ashx?speclist=51557,51558,51559,51560,51561,51562,51565,51566,51563,51564,51567,51568&_callback=getspeccheping


def request_brand_list(s):
    # 请求页面
    url = 'https://www.autohome.com.cn/beijing/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/93.0.4577.82 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    print(response.content)
    # 使用BeautifulSoup加载页面
    soup = BeautifulSoup(response.content, features="lxml")
    # 按标签查找
    brand_list_1 = soup.find(attrs={'data-target': 'brand'})
    print(brand_list_1)
    # a_list = div_list.find_all("a")
    brand_list = list()
    # for a in a_list:
    #     href = a["href"]
    #     if not str(href).startswith('http'):
    #         href = chapter_url + href
    #     text = a.text.strip().replace("\n", "").replace("\r", "")
    #     chapter_list.append({'text': text, 'href': href, })
    return brand_list


def sss():
    url = 'https://car.autohome.com.cn/javascript/NewSpecCompare.js'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/93.0.4577.82 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    try:
        temp = str(response.content.decode('GBK'))
        index_start = temp.find('[')
        index_end = temp.rfind(']')
        obj = json.loads(temp[index_start:index_end+1])
    except Exception as e:
        print(e)
        print(response.content)
    pass


# def xxx():
#     url = 'https://car.autohome.com.cn/duibi/ashx/specComparehandler.ashx?type=1&seriesid=3895&format=json&_=1544411587605&callback=__jp0'
# https://car.autohome.com.cn/duibi/chexing/#carids=0&adids=0


if __name__ == '__main__':
    sss()
    pass
