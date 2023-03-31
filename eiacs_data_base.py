import pymysql

DB_IP = '10.18.40.25'
DB_PORT = 3306
DB_USER = "root"
DB_PWD = "PxX5ksKU801vOYBYj2CVsU1fP3"
DB_NAME_BIZ = 'db_eiacs_biz'
class DB_BIZ(object):
    def __init__(self):
        self.file = 0
        self.mysql = ''
        self.num = 0

    def init(self):
        self.mysql = pymysql.connect(
            host=DB_IP,  # 连接地址, 本地
            user=DB_USER,  # 用户
            password=DB_PWD,  # 数据库密码,记得修改为自己本机的密码
            port=DB_PORT,  # 端口,默认为3306
            charset='utf8',  # 编码
            database=DB_NAME_BIZ  # 选择数据库
        )
    def insert(self, biz_code, created_time, id_card, legal_user, msisdn,name,state,update_time):
        db = self.mysql.cursor()
        append = 'INSERT INTO signing_business_record (biz_code, created_time, id_card, legal_user, msisdn, name, state, update_time)  VALUES' + "(" + str(
            biz_code) + "," + "'" + created_time + "'" + "," + "'" + str(id_card) + "'" + "," + 'b' + "'" + "0"+ "'"+ "," + "'" + str(msisdn) + "'" + "," + "'" + str(name) + "'" + "," + "'" + str(
            state) + "'" + "," + "'" + created_time + "'" + ")"
        print(append)
        try:
            # db.executemany(append, data)
            db.execute(append)
        except Exception as e:
            print('操作失败', e)

    def insert_new(self, append):
        db = self.mysql.cursor()

        try:
            db.execute(append)
        except Exception as e:
            print('操作失败', e)

    def insert_new_data(self, append, data):
        db = self.mysql.cursor()
        try:
            db.executemany(append, data)
        except Exception as e:
            print('操作失败', e)
    def delete_data(self, append):
        db = self.mysql.cursor()
        try:
            db.execute(append)
        except Exception as e:
            print('操作失败', e)
    def commit(self):
        self.mysql.commit()
