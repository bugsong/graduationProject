import string

from flask import Flask
from flask import render_template
from flask import jsonify  # 转字符串用的
import utils
from jieba.analyse import extract_tags  # 词云部分需要

app = Flask(__name__)


@app.route('/')  # 这里我是直接改写了跟路径的访问
def index():
    return render_template('main.html')


@app.route('/time')
def get_time():
    return utils.get_time()


@app.route('/center_top')
def get_center_top_data():
    tup = utils.get_connect(utils.link_config)
    data = utils.get_center_top_data(tup)
    json_ = {
        "confirm": data[0],
        "suspect": data[1],
        "heal": data[2],
        "dead": data[3]
    }
    return jsonify(json_)


@app.route('/center_bottom')
def get_center_bottom_data():
    tup = utils.get_connect(utils.link_config)
    data = utils.get_center_bottom_data(tup)
    res = []
    for tup_ in data:
        res.append({"name": tup_[0], "value": int(tup_[1])})
        # 处理成前端对应的格式
    return jsonify({"data": res})


@app.route('/left_top')
def get_left_top_data():
    tup = utils.get_connect(utils.link_config)
    data = utils.get_left_top_data(tup)
    day, confirm, suspect, heal, dead = [], [], [], [], []
    for d, c, s, h, de in data[25:]:  # 去掉公布的完的Null数据
        day.append(d.strftime("%m-%d"))  # d是datetime类型
        confirm.append(c)
        suspect.append(s)
        heal.append(h)
        dead.append(de)
        # 处理成前端对应的格式
    json_ = {
        "day": day,
        "confirm": confirm,
        "suspect": suspect,
        "heal": heal,
        "dead": dead,
    }
    return jsonify(json_)


@app.route('/left_bottom')
def get_left_bottom_data():
    tup = utils.get_connect(utils.link_config)
    data = utils.get_left_bottom_data(tup)
    day, confirm_add, suspect_add = [], [], []
    for d, c, s in data[25:]:
        day.append(d.strftime("%m-%d"))
        confirm_add.append(c)
        suspect_add.append(s)
        # 处理成前端对应的格式
    json_ = {
        "day": day,
        "confirm_add": confirm_add,
        "suspect_add": suspect_add,
    }
    return jsonify(json_)


@app.route('/right_top')
def get_right_top_data():
    tup = utils.get_connect(utils.link_config)
    data = utils.get_right_top_data(tup)
    city, confirm = [], []
    for k, v in data:
        city.append(k)
        confirm.append(v)
        # 处理成前端对应的格式
    json_ = {
        "city": city,
        "confirm": confirm,
    }
    return jsonify(json_)


@app.route('/right_bottom')
def get_right_bottom_data():
    tup = utils.get_connect(utils.link_config)
    data = utils.get_right_bottom_data(tup)
    d = []
    for i in data:
        k = i[0].rstrip(string.digits)  # 移除热搜数字
        v = i[0][len(k):]  # 获取热度数字
        ks = extract_tags(k)  # 使用jieba提取关键字
        for j in ks:
            if not j.isdigit():
                d.append({"name": j, "value": v})
        # 处理成前端对应的格式
    return jsonify({"kws": d})


if __name__ == '__main__':
    app.run()
