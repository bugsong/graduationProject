from flask import Flask
from flask import request  # 用来获取浏览器传过来的请求参数
from flask import render_template
from flask import jsonify  # 转字符串用的
import utils

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
    for d, c, s, h, de in data[7:]:  # 去掉公布的完的Null数据
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
    print(data)
    res = []
    for tup_ in data:
        res.append({"name": tup_[0], "value": int(tup_[1])})
        # 处理成前端对应的格式
    return jsonify({"data": res})


if __name__ == '__main__':
    app.run()
