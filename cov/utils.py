import time
import pymysql

def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年","月","日")

def get_conn():
    # 建立连接
    conn = pymysql.connect(host="localhost", user="root", password="980715", db="cov", charset="utf8")
    # c创建游标A
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()

def query(sql,*args):
    """

    :param sql:
    :param args:
    :return:
    """
    conn,cursor = get_conn()
    cursor.execute(sql,args)
    res = cursor.fetchall()
    close_conn(conn,cursor)
    return res

def test():
    sql = "select * from details"
    res = query(sql)
    return res[0]

def get_c1_data():
    sql = "select sum(confirm)," \
          "(select suspect from history order by ds desc limit 1)," \
          "sum(heal),sum(dead) from details " \
          "where update_time=(select update_time from details order by update_time desc limit 1) "
    res = query(sql)
    return res[0]

def get_c2_data():
    sql = "select province,sum(confirm) from details " \
          "where update_time=(select update_time from details " \
          "order by update_time desc limit 1) " \
          "group by province"
    res = query(sql)
    return res

def get_l1_data():
    sql = "select ds,confirm,suspect,heal,dead from history"
    res = query(sql)
    return res

def get_l2_data():
    sql = "select ds,confirm_add,suspect_add from history"
    res = query(sql)
    return res

def get_r1_data():
    sql = 'select province, city, confirm from ' \
          '(select province, city, confirm from details ' \
          'where update_time=(select update_time from details order by update_time desc limit 1) ' \
          'and province not in ("湖北","北京","上海","天津","重庆") ' \
          'union all ' \
          'select province, city, confirm from details ' \
          'where update_time=(select update_time from details order by update_time desc limit 1) ' \
          'and province in ("北京","上海","天津","重庆")) as a ' \
          'order by confirm desc limit 5'
    res = query(sql)
    return res

def get_r2_data():
    sql = "select province, sum(confirm_add) as pp from details " \
          "where update_time=(select update_time from details " \
                            "order by update_time desc limit 1) " \
          "group by province order by pp desc limit 10" 
          
    res = query(sql)
    return res

if __name__ == "__main__":
    # res = []
    # #print(test())
    # for tup in get_r2_data():
    #     res.append({"name":tup[0], "value":int(tup[1]) })
    
    # print(res)

    print(get_c2_data())