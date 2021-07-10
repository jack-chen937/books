from pymysql import connect


class Book(object):
    def __init__(self):  # 创建对象的同时执行代码
        self.conn = connect(
            host='47.98.53.127',
            port=3306,
            user='cx',
            database='cx',
            password='cx15770615665'
        )
        print('123')
        self.cursor = self.conn.cursor()

    def __del__(self):  # 释放对象的同时执行代码
        self.cursor.close()
        self.conn.close()

    def get_data(self):
        sql = 'select * from 徐大sao limit 1'
        self.cursor.execute(sql)
        data = []
        for item in self.cursor.fetchall():
            data.append(item)
        return data
