import re

import requests
import json
import time
import datetime


def get_tencent_data():
    """
    爬取腾讯疫情平台数据
    :return: 返回历史数据和当日详细数据
    """
    url = "https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?" \
          "modules=diseaseh5Shelf,chinaDayList,chinaDayAddList,provinceCompare"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0", }
    response = requests.post(url=url, headers=headers)
    data_all = json.loads(response.text)  # json字符串转换为字典

    history = {}  # 承接历史数据
    for i in data_all["data"]["chinaDayList"]:
        ds = "2022." + i["date"]  # 网站数据类型为05.24  所以用来拼接成日期
        tup = time.strptime(ds, "%Y.%m.%d")
        ds = time.strftime("%Y-%m-%d", tup)  # 改变时间格式,以便插入数据库,datetime类型
        confirm = i["confirm"]
        suspect = i["suspect"]
        heal = i["heal"]
        dead = i["dead"]
        # print(f"no add {ds}")
        history[ds] = {"confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead}
        # print(history[ds])  # 字典的拼接出现了一点问题
    flag = True
    for dct in data_all["data"]["chinaDayAddList"]:
        if flag:
            flag = False
            continue  # 使之开始统计日期与上边同步
        ds = "2022." + dct["date"]  # 惊天大bug,整了半天就一条数据,是因为日期没有指定更新
        tup = time.strptime(ds, "%Y.%m.%d")  # 获取的时间出了问题
        ds = time.strftime("%Y-%m-%d", tup)  # 改变时间格式,以便插入数据库,datetime类型
        #  修正时间
        # dt = datetime.datetime.strptime(ds, "%Y-%m-%d")
        # ds = (dt + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        # 修了半天,发现存在位移现象,还得修改尾巴,那么直接做切片使之对等好了
        confirm_add = dct['localConfirmadd']  # 更新部分,获取数据方法变更
        # print(confirm_add)
        suspect_add = dct["suspect"]
        heal_add = dct["heal"]
        dead_add = dct["dead"]
        # print(f"add {ds}")  # 新增统计在后一天统计,所以需要给新增统计加1天
        history[ds].update(
            {"confirm_add": confirm_add, "suspect_add": suspect_add, "heal_add": heal_add, "dead_add": dead_add})
        # print(history[ds])  # 输出到最后,也只保留到了最后一行,又研究一番,发现是时间的问题

    details = []  # 当日详细数据
    update_time = data_all["data"]["diseaseh5Shelf"]["lastUpdateTime"]
    data_country = data_all["data"]["diseaseh5Shelf"]["areaTree"]  # 各个国家数据
    data_province = data_country[0]["children"]  # 中国各省

    for pro_infos in data_province:
        province = pro_infos["name"]  # 省名fixed
        for city_infos in pro_infos["children"]:
            city = city_infos["name"]  # fixed
            confirm = city_infos["total"]["confirm"]
            confirm_add = city_infos["today"]["confirm"]
            heal = city_infos["total"]["heal"]
            dead = city_infos["total"]["dead"]
            details.append([update_time, province, city, confirm, confirm_add, heal, dead])
    return history, details


def get_baidu_data():
    url = "https://top.baidu.com/board"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0",
    }
    params = {
        "tab": "realtime",
    }
    response = requests.get(url=url, headers=headers, params=params)
    obj_title = re.compile(r'<div class="c-single-text-ellipsis">(?P<title>.*?)</div>'
                           r'.*?<div class="hot-index_1Bl1a">(?P<number>.*?)</div>', re.S)
    titles = obj_title.finditer(response.text)
    lst = []
    for title in titles:
        data = title.group("title") + title.group("number")
        lst.append(data.replace(' ', ''))
    response.close()
    return lst


if __name__ == '__main__':
    # for k, v in get_tencent_data()[0].items():
    #     print(k, v)
    # get_tencent_data()[0].keys()  # 经过人工排错,少了一个datetime或许history的keys就是datetime
    for v in get_tencent_data()[0].values():
        print(v)
        pass
    # lst = get_baidu_data()
    # print(lst)
