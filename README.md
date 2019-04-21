# wuhan_house_price_crawler
武汉东湖高新片区房价爬虫。data source: 房天下

### Aim

可能要回国就业, 考虑到武汉的互联网大厂集中在东湖高新大光谷片区, 通勤不是很方便(村), 应该会产生就近购房的需求, 提前写了一个简单的爬虫, 数据来源是[房天下](https://wuhan.esf.fang.com/house-a013126)

### Report

* [东湖高新二手房信息汇总_Double.csv](https://github.com/ShiqinHuo/wuhan_house_price_crawler/blob/master/all_info/%E4%B8%9C%E6%B9%96%E9%AB%98%E6%96%B0%E4%BA%8C%E6%89%8B%E6%88%BF%E4%BF%A1%E6%81%AF%E6%B1%87%E6%80%BB_Double.csv)
  * 总共爬取100页数据共计6000条, 其中有效数据5877条
* [东湖高新公寓汇总_Double.csv](https://github.com/ShiqinHuo/wuhan_house_price_crawler/blob/master/all_info/%E4%B8%9C%E6%B9%96%E9%AB%98%E6%96%B0%E5%85%AC%E5%AF%93%E6%B1%87%E6%80%BB_Double.csv)
  * 有效数据5877条中有5614条均为公寓
* [东湖高新别墅汇总_Double.csv](https://github.com/ShiqinHuo/wuhan_house_price_crawler/blob/master/all_info/%E4%B8%9C%E6%B9%96%E9%AB%98%E6%96%B0%E5%88%AB%E5%A2%85%E6%B1%87%E6%80%BB_Double.csv) 
  * 仅有263条别墅记录 
* 可视化分析报告后续会更进

![小区中位单价条形图1](https://github.com/ShiqinHuo/wuhan_house_price_crawler/blob/master/community_bar/%E5%B0%8F%E5%8C%BA%E4%B8%AD%E4%BD%8D%E5%8D%95%E4%BB%B7%E6%9D%A1%E5%BD%A2%E5%9B%BE1.png | width=500)

![小区中位单价条形图2](https://github.com/ShiqinHuo/wuhan_house_price_crawler/blob/master/community_bar/%E5%B0%8F%E5%8C%BA%E4%B8%AD%E4%BD%8D%E5%8D%95%E4%BB%B7%E6%9D%A1%E5%BD%A2%E5%9B%BE2.png | width=500)


![小区中位单价条形图3](https://github.com/ShiqinHuo/wuhan_house_price_crawler/blob/master/community_bar/%E5%B0%8F%E5%8C%BA%E4%B8%AD%E4%BD%8D%E5%8D%95%E4%BB%B7%E6%9D%A1%E5%BD%A2%E5%9B%BE3.png | width=500)


![小区中位单价条形图4](https://github.com/ShiqinHuo/wuhan_house_price_crawler/blob/master/community_bar/%E5%B0%8F%E5%8C%BA%E4%B8%AD%E4%BD%8D%E5%8D%95%E4%BB%B7%E6%9D%A1%E5%BD%A2%E5%9B%BE4.png | width=500)


![小区中位单价条形图5](https://github.com/ShiqinHuo/wuhan_house_price_crawler/blob/master/community_bar/%E5%B0%8F%E5%8C%BA%E4%B8%AD%E4%BD%8D%E5%8D%95%E4%BB%B7%E6%9D%A1%E5%BD%A2%E5%9B%BE5.png | width=500)


![小区中位单价条形图6](https://github.com/ShiqinHuo/wuhan_house_price_crawler/blob/master/community_bar/%E5%B0%8F%E5%8C%BA%E4%B8%AD%E4%BD%8D%E5%8D%95%E4%BB%B7%E6%9D%A1%E5%BD%A2%E5%9B%BE6.png | width=500)


![小区中位单价条形图7](https://github.com/ShiqinHuo/wuhan_house_price_crawler/blob/master/community_bar/%E5%B0%8F%E5%8C%BA%E4%B8%AD%E4%BD%8D%E5%8D%95%E4%BB%B7%E6%9D%A1%E5%BD%A2%E5%9B%BE7.png | width=500)


![小区中位单价条形图8](https://github.com/ShiqinHuo/wuhan_house_price_crawler/blob/master/community_bar/%E5%B0%8F%E5%8C%BA%E4%B8%AD%E4%BD%8D%E5%8D%95%E4%BB%B7%E6%9D%A1%E5%BD%A2%E5%9B%BE8.png | width=500)




### Requirements

```python
import os
import requests
from lxml import html, etree
from bs4 import BeautifulSoup
import pandas # for data cleaning
```
### project structure

<div class="highlight-none notranslate"><div class="highlight"><pre><span></span>root/
├── all_info/
│   ├── all_fang_info
│   ├── data_cleaning.ipynb
│   ├── data_cleaning.py
│   ├── 东湖高新二手房信息汇总_Double.csv
├── huawei_crawler.py
├── read_fang.py
├── picture/
├── temp/
│   ├── temp_1
│   ├── temp_100
├── downloads/
│   ├── fang_page_1
│   ├── fang_page_100
</pre></div>
</div>


### XPath解析HTML
```python
# 标题 //*[@id="kesfqbfylb_A01_01_62"]/dd[1]/h4/a/span
# 户型 //*[@id="kesfqbfylb_A01_01_62"]/dd[1]/p[1]/text()[1]
# 面积 //*[@id="kesfqbfylb_A01_01_62"]/dd[1]/p[1]/text()[2]
# 楼层 //*[@id="kesfqbfylb_A01_01_62"]/dd[1]/p[1]/text()[3]
# 朝向 //*[@id="kesfqbfylb_A01_01_62"]/dd[1]/p[1]/text()[4]
# 年份 //*[@id="kesfqbfylb_A01_01_62"]/dd[1]/p[1]/text()[5]
# 总价 //*[@id="kesfqbfylb_A01_01_62"]/dd[2]/span[1]/b
# 单价 //*[@id="kesfqbfylb_A01_01_62"]/dd[2]/span[2]
# 地址 //*[@id="kesfqbfylb_A01_01_62"]/dd[1]/p[2]/span
# 小区 //*[@id="kesfqbfylb_A01_01_62"]/dd[1]/p[2]/a/@title
```
