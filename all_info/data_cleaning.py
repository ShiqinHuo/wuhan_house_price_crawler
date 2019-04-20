# info = 文件all_fang_info的内容
# 需要安装pandas

import pandas as pd
def data_clean():
    clean = []
    for item in info:
        new = {}
        if len(item['标题']) != 0:
            new['标题'] = item['标题'][0].strip()
            new['户型'] = item['户型'][0].strip()
            new['面积'] = item['面积'][0].strip()
            new['楼层'] = item['楼层'][0].strip()
            new['朝向'] = item['朝向'][0].strip()
            new['年份'] = item['年份'][0].strip()
            new['总价'] = item['总价'][0].strip()
            new['单价'] = item['单价'][0].strip()
            new['地址'] = item['地址'][0].strip()
            new['小区'] = item['小区'][0].strip()
        clean.append(new)
    df = pd.DataFrame(clean)
    return df

# df = data_clean()
# df.to_csv("东湖高新二手房信息汇总.csv",encoding="utf_8_sig")
