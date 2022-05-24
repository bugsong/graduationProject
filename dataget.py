import requests
import json
import time


def get_tencent_data():
    """
    爬取腾讯疫情平台数据
    :return: 返回历史数据和当日详细数据
    """
    url = "https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?" \
          "modules=localCityNCOVDataList,diseaseh5Shelf," \
          "chinaDayList,chinaDayAddList,nowConfirmStatis,provinceCompare"
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
        history[ds] = {"confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead}
        # print(history[ds])  # 获取没有问题,问题应该出在了写入

    for t in data_all["data"]["chinaDayAddList"]:
        ds = "2022." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")
        ds = time.strftime("%Y-%m-%d", tup)  # 改变时间格式,以便插入数据库,datetime类型
        confirm = t["confirm"]
        suspect = t["suspect"]
        heal = t["heal"]
        dead = t["dead"]
        history[ds].update({"confirm_add": confirm, "suspect_add": suspect, "heal_add": heal, "dead_add": dead})

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


if __name__ == '__main__':
    for k, v in get_tencent_data()[0].items():
        print(k, v)
    # get_tencent_data()[0].keys()  # 经过人工排错,少了一个datetime或许history的keys就是datetime
