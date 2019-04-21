# -*- coding: utf-8 -*-
import os
import requests
from lxml import html, etree
from bs4 import BeautifulSoup

base = 'https://wuhan.esf.fang.com/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

def save_text(text, filename, path):
    fpath = os.path.join(path, filename)
    with open(fpath, 'w') as  f:
        print('output:', fpath)
        f.write(text)

def read_info(page):
    prefix = "./temp/temp_"
    filename = prefix + str(page)
    with open(filename, 'r') as f:
        res = f.read()
    return res


def crawl(url,page):
    resp = requests.get(url, headers=headers)
    content = resp.text
    # html_file = "temp_" + str(page) # + ".html"
    # save_text(content, filename=html_file, path='temp')
    decode_html(content, page)

def decode_html(content, page):
    soup = BeautifulSoup(content,"lxml")
    decode_file = "fang_page_" + str(page)
    res = []
    for index in range(3,63):
        if index < 10:
            index = "0" + str(index)
        else:
            index = str(index)

        selector = '#kesfqbfylb_A01_01_' + index
        house = soup.select(selector)
        if len(house) != 0:
            html = etree.fromstring(str(house[0]))

            title = html.xpath("//dd[1]/h4/a/span/text()")
            types = html.xpath("//dd[1]/p[1]/text()[1]")
            area = html.xpath("//dd[1]/p[1]/text()[2]")
            floor = html.xpath("//dd[1]/p[1]/text()[3]")
            direction = html.xpath("//dd[1]/p[1]/text()[4]")
            year = html.xpath("//dd[1]/p[1]/text()[5]")
            total_price = html.xpath("//dd[2]/span[1]/b/text()")
            price_per_sqr = html.xpath("//dd[2]/span[2]/text()")
            address = html.xpath("//dd[1]/p[2]/span/text()")
            community = html.xpath("//dd[1]/p[2]/a/@title")

            result = {
                "标题" : title,
                "户型" : types,
                "面积" : area,
                "楼层" : floor,
                "朝向": direction,
                "年份": year,
                "总价": total_price,
                "单价": price_per_sqr,
                "地址": address,
                "小区": community
            }
            res.append(result)
    fang_info = "fang_page_" + str(page)
    save_text(str(res), filename=fang_info, path='download')

# # 爬首页
# crawl("https://wuhan.esf.fang.com/house-a0492-b01534", "1")
#
# # 循环，把第2-28页全部爬下来
# #
# page = 2
# while page < 29:
#     url = 'https://wuhan.esf.fang.com/house-a0492-b01534/i3'+str(page)
#     crawl(url, page)
#     page = page + 1
