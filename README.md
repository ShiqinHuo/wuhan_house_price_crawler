# wuhan_house_price_crawler
武汉东湖高新片区房价爬虫。data source: 房天下

### Aim

可能要回国就业, 考虑到武汉的互联网大厂集中在东湖高新大光谷片区, 通勤不是很方便(村), 应该会产生就近购房的需求, 提前写了一个简单的爬虫, 数据来源是[房天下](https://wuhan.esf.fang.com/house-a013126)

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
