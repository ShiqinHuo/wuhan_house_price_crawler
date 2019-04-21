import qiaokou_crawler as qc
def read_info():
    info = "["
    prefix = "download/fang_page_"
    for page in range(1,29):
        filename = prefix + str(page)
        with open(filename, 'r') as f:
            res = f.read()
            res = res[1:-1] # remove []
            # print(type(res))
            if page != 1:
                info = info + ", " + res
            else:
                info = info +res
            if page == 28:
                info += "]"
    qc.save_text(info, filename="all_hanzheng_info", path='hanzheng_all')
    return info
read_info()
