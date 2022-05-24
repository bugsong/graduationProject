import time
import traceback
import pymysql
from dataget import *


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


def update_details(get_tencent_data, get_connect_ret, close_conn):
    """
    更新最新数据
    :param get_tencent_data: 从腾讯疫情获取的数据
    :param get_connect_ret: 获取链接和游标
    :param close_conn: 关闭游标和链接
    :return:
    """
    cursor = None
    connect = None
    try:
        li = get_tencent_data()[1]  # 0是历史数据字典,1是最新详细数据列表
        connect, cursor = get_connect_ret
        sql = "insert into details(update_time,province,city,confirm,confirm_add,heal,dead) values(%s,%s,%s,%s,%s,%s,%s)"
        sql_query = 'select %s=(select update_time from details order by id desc limit 1)'  # 对比当前最大时间戳
        cursor.execute(sql_query, li[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()}开始更新最新数据")
            for item in li:
                cursor.execute(sql, item)
            connect.commit()  # 提交事物,update delete insert操作
            print(f"{time.asctime()}更新最新数据完毕")
        else:
            print(f"{time.asctime()}已是最新数据!")
    except:
        traceback.print_exc()
    finally:
        close_conn(connect, cursor)


def insert_details(get_tencent_data, get_connect_ret, close_conn):
    """
    插入最新疫情数据
    :param get_tencent_data: 从腾讯疫情获取的数据
    :param get_connect_ret: 获取链接和游标
    :param close_conn: 关闭游标和链接
    :return:none
    """
    cursor = None
    connect = None
    try:
        dic = get_tencent_data()[0]  # 读取历史数据字典
        print(f"{time.asctime()}开始插入历史数据")
        connect, cursor = get_connect_ret  # 此处接收的是函数的返回值,为一个元组
        sql = "insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"  # 9个
        for k, v in dic.items():
            # item 格式 {'2022-01-03':{'confirm':41,'suspect':0,'heal':0,'dead':1}}
            cursor.execute(sql, [k, v.get("confirm"), v.get("confirm_add"), v.get("suspect"), v.get("suspect_add"),
                                 v.get("heal"), v.get("heal_add"), v.get("dead"), v.get("dead_add")])
        connect.commit()  # 只要不是单纯查询都得提交事务
        print(f"{time.asctime()}插入历史数据完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(connect, cursor)


def insert_history(get_tencent_data, get_connect_ret, close_conn):
    """
    初次插入历史数据
    :param get_tencent_data: 从腾讯疫情获取的数据
    :param get_connect_ret: 获取链接和游标
    :param close_conn: 关闭游标和链接
    :return:none
    """
    cursor = None
    conn = None
    try:
        dic = get_tencent_data()[0]
        print(f"{time.asctime()}开始插入历史数据")
        conn, cursor = get_connect_ret
        sql = "insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for k, v in dic.items():
            cursor.execute(sql, [k, v.get("confirm"), v.get("confirm_add"), v.get("suspect"), v.get("suspect_add"),
                                 v.get("heal"), v.get("heal_add"), v.get("dead"), v.get("dead_add")])
        conn.commit()  # 插入后提交
        print(f"{time.asctime()}插入历史数据完毕!")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def update_history(get_tencent_data, get_connect_ret, close_conn):
    """
    更新历史数据
    :param get_tencent_data: 从腾讯疫情获取的数据
    :param get_connect_ret: 获取链接和游标
    :param close_conn: 关闭游标和链接
    :return:none
    """
    cursor = None
    conn = None
    try:
        dic = get_tencent_data()[0]  # 历史字典数据
        print(f"{time.asctime()}开始更新历史数据")
        conn, cursor = get_connect_ret  # 返回值元组
        sql = "insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"  # 9个
        sql_query = "select confirm from history where ds=%s"
        for k, v in dic.items():
            if not cursor.execute(sql_query, k):
                cursor.execute(sql, [k, v.get("confirm"), v.get("confirm_add"), v.get("suspect"), v.get("suspect_add"),
                                     v.get("heal"), v.get("heal_add"), v.get("dead"), v.get("dead_add")])
        conn.commit()  # 提交事务
        print(f"{time.asctime()}历史数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


if __name__ == '__main__':
    # 链接配置
    link_config = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "mariaBugsong",
        "db": "bugsong",
        "charset": "utf8mb4"
    }
    connect_ret = get_connect(link_config)  # 这个直接集成在各个函数的参数里了考虑要不要分离出来,分离出来其他函数就能去掉个参数
    # insert_history(get_tencent_data, connect_ret, close_connect)  # 初次插入历史数据
    # update_history(get_tencent_data, connect_ret, close_connect)  # 要理解为什么写函数名
    # insert_details(get_tencent_data, connect_ret, close_connect)
    update_details(get_tencent_data, connect_ret, close_connect)  # 忘了,第一遍应该先插入
    # 以上四个均不能一起开,因为每个函数执行完会关闭链接和游标
