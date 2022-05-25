from flask import Flask
from flask import request  # 用来获取浏览器传过来的请求参数
from flask import render_template

app = Flask(__name__)


@app.route('/')  # 这里我是直接改写了跟路径的访问
def index():
    return render_template('index.html')


@app.route('/ajax', methods=["get", "post"])
def ajax_():
    name = request.values.get("name")
    score = request.values.get("score")
    print(f"name:{name},score:{score}")
    return "10000"


# @app.route('/login')  # 注册一个函数
# def login():
#     name = request.values.get("name")
#     pwd = request.values.get("pwd")
#     return f"""
#         name={name},pwd={pwd}
#     """


# @app.route('/')
# def hello_world():  # put application's code here
#     id = request.values.get("id")
#     # 那么在输入时,可以在地址栏使用get传参方式,使之获取到数据
#     return f"""
#     <form action="/login">
#         帐号:<input name="name" value="{id}"/><br/>
#         密码:<input name="pwd" />
#         <input type="submit">
#     </form>
#     """


if __name__ == '__main__':
    app.run()
