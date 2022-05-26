# 这里是定义了一个工具
import time
import pymysql

link_config = {  # 还没做统一化,请必要时修改
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "mariaBugsong",
    "db": "bugsong",
    "charset": "utf8mb4"
}


def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X", )
    return time_str.format("年", "月", "日")


def get_connect(link_conf):
    """
    传入用户的数据库配置,返回一个链接和游标
    :param link_conf:
    :return: [链接,游标]
    """

    # 创建链接
    connect = pymysql.connect(host=link_conf["host"],
                              port=link_conf["port"],
                              user=link_conf["user"],
                              password=link_conf["password"],
                              db=link_conf["db"],
                              charset=link_conf["charset"])
    # 创建游标
    cursor = connect.cursor()
    return connect, cursor


def close_connect(conn, csr):
    """
    传入将链接和游标进行顺序关闭
    :param conn: 链接
    :param csr: 游标
    :return: none
    """
    if csr:
        csr.close()
    if conn:
        conn.close()


def query(sql, get_conn_tup, *args):
    """
    查询数据,查完就关闭啦
    :param sql:sql语句
    :param get_conn_tup:获取链接和游标
    :param close_conn:关闭链接和游标
    :param args:另外参数
    :return:
    """
    conn = None
    cursor = None
    conn, cursor = get_conn_tup
    cursor.execute(sql, args)
    res = cursor.fetchall()
    # close_conn(conn, cursor)
    return res


def get_center_top_data(get_conn_tup):
    _tup = get_conn_tup
    sql = "select sum(confirm)," \
          "(select suspect from history order by ds desc limit 1)," \
          "sum(heal)," \
          "sum(dead) " \
          "from details " \
          "where update_time=(select update_time from details order by update_time desc limit 1)"
    res = query(sql=sql, get_conn_tup=_tup)
    return res[0]


def get_center_bottom_data(get_conn_tup):
    _tup = get_conn_tup
    sql = "select province,sum(confirm) from details " \
          "where update_time=(select update_time from details " \
          "order by update_time desc limit 1) " \
          "group by province"
    res = query(sql=sql, get_conn_tup=_tup)
    return res


def get_left_top_data(get_conn_tup):
    _tup = get_conn_tup
    sql = "select ds,confirm,suspect,heal,dead from history"
    res = query(sql=sql, get_conn_tup=_tup)
    return res


def get_left_bottom_data(get_conn_tup):
    _tup = get_conn_tup
    sql = "select ds,confirm_add,suspect_add from history"
    res = query(sql=sql, get_conn_tup=_tup)
    return res


if __name__ == '__main__':
    print(get_time())
    # 以下在网站调用时需要
    tup = get_connect(link_config)
    # 以上在网站调用时需要

    # print(get_center_top_data(tup))
    # print(get_center_bottom_data(tup))
    print(get_left_top_data(tup))
    print(get_left_bottom_data(tup))
    close_connect(tup[0], tup[1])
    # 需要独自设计关闭操作
