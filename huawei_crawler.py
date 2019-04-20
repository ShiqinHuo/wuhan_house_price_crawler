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
    html_file = "temp_" + str(page) # + ".html"
    save_text(content, filename=html_file, path='temp')
    decode_html(content, page)

def decode_html(content, page):
    soup = BeautifulSoup(content,"lxml")

    # houses = soup.select("#body > div.container.body-content > div.main1200.clearfix > div.main945.floatl > div.shop_list.shop_list_4 ")

    decode_file = "fang_page_" + str(page)
    # save_text(str(speaker), filename=decode_file, path='download')
    res = []
    # print(houses)
    # for selector in houses:
    for index in range(3,63):
        if index < 10:
            index = "0" + str(index)
        else:
            index = str(index)

        # print index
        selector = '#kesfqbfylb_A01_01_' + index
        # print(selector ==  '#kesfqbfylb_A01_01_03')
        # print(type(index))
        # selector = '#kesfqbfylb_A01_01_03'
        # print(selector)
        house = soup.select(selector)
        # print(house)
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

        # txt = read_info(page)
        # print(type(txt))
        # html = etree.fromstring(txt)
        # prefix = '//*[@id="kesfqbfylb_A01_01_"'
        # title_xpath =  prefix + index + '"]/dd[1]/h4/a/span'
        # type_xpath = prefix + index + '"]/dd[1]/p[1]/text()[1]'
        # area_xpath = prefix + index + '"]/dd[1]/p[1]/text()[2]'
        # floor_xpath = prefix + index + '"]/dd[1]/p[1]/text()[3]'
        # direction_xpath = prefix + index + '"]/dd[1]/p[1]/text()[4]'
        # year_xpath = prefix + index + '"]/dd[1]/p[1]/text()[5]'
        # total_price_xpath = prefix + index + '"]/dd[2]/span[1]/b'
        # price_per_sqr_xpath = prefix + index + '"]/dd[2]/span[2]'
        # address_xpath =  prefix + index + '"]/dd[1]/p[2]/span'
        # community_xpath = prefix + index + '"]/dd[1]/p[2]/a/@title'

        # title = html.xpath(title_xpath)
        # types = html.xpath(type_xpath)
        # area = html.xpath(area_xpath)
        # floor = html.xpath(floor_xpath)
        # direction = html.xpath(direction_xpath)
        # year = html.xpath(year_xpath)
        # total_price = html.xpath(total_price_xpath)
        # price_per_sqr = html.xpath(price_per_sqr_xpath)
        # address = html.xpath(address_xpath)
        # community = html.xpath(community_xpath)

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

#kesfqbfylb_A01_01_03 > dd:nth-child(2) > h4 > a > span
#kesfqbfylb_A01_01_62 > dd:nth-child(2) > h4 > a > span

#kesfqbfylb_A01_01_62 > dd:nth-child(2) > h4 > a > span

# 标题 //*[@id="kesfqbfylb_A01_01_62"]/dd[1]/h4/a/span
#
# 户型 //*[@id="kesfqbfylb_A01_01_62"]/dd[1]/p[1]/text()[1]
#
# 面积 //*[@id="kesfqbfylb_A01_01_62"]/dd[1]/p[1]/text()[2]
#
# 楼层 //*[@id="kesfqbfylb_A01_01_62"]/dd[1]/p[1]/text()[3]
#
# 朝向 //*[@id="kesfqbfylb_A01_01_62"]/dd[1]/p[1]/text()[4]
#
# 年份 //*[@id="kesfqbfylb_A01_01_62"]/dd[1]/p[1]/text()[5]
#
# 总价 //*[@id="kesfqbfylb_A01_01_62"]/dd[2]/span[1]/b
#
# 单价 //*[@id="kesfqbfylb_A01_01_62"]/dd[2]/span[2]
#
# 地址 //*[@id="kesfqbfylb_A01_01_62"]/dd[1]/p[2]/span
#
# 小区 //*[@id="kesfqbfylb_A01_01_62"]/dd[1]/p[2]/a/@title

# 爬首页
# crawl("https://wuhan.esf.fang.com/house-a013126", "1")
#
# # 循环，把第2-100页全部爬下来
# page = 2
# while page < 101:
#     url = 'https://wuhan.esf.fang.com/house-a013126/i3'+str(page)
#     crawl(url, page)
#     page = page + 1
