import huawei_crawler as hc
def read_info():
    info = "["
    prefix = "download/fang_page_"
    for page in range(1,101):
        filename = prefix + str(page)
        with open(filename, 'r') as f:
            res = f.read()
            res = res[1:-1] # remove []
            # print(type(res))
            if page != 1:
                info = info + ", " + res
            else:
                info = info +res
            if page == 100:
                info += "]"
    hc.save_text(info, filename="all_fang_info", path='all_info')
    return info
read_info()
