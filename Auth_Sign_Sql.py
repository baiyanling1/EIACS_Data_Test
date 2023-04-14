import csv
import random
import time
import uuid
from random import randint
from eiacs_data_base import DB_BIZ
import openpyxl
import  id_num

#自己写的
def Insert_sign_user(filename):
    mysql_BIZ = DB_BIZ()
    mysql_BIZ.init()
    created_time = time.strftime('%Y-%m-%d %H:%M:%S')
    update_time = time.strftime('%Y-%m-%d %H:%M:%S')
    userValues_BIZ = []
    sql_BIZ_1 = "INSERT INTO user_signed_info(created_time, group_name, id_card, legal_user, msisdn,name,update_time) VALUE (%s,%s,%s,%s,%s,%s,%s)"

    workbook = openpyxl.load_workbook(filename)
    sheet = workbook['鉴权终端用户数据']
    # data = (psycopg2.Binary(b'1'),)
    # 遍历行
    for row in sheet.iter_rows(min_row=2):
        # 获取单元格数据
        name = row[0].value
        msisdn = row[1].value
        id_card = row[2].value
        group_name = row[3].value
        userValues_BIZ.append(
            (str(created_time), str(group_name), str(id_card), 1, str(msisdn), str(name), str(update_time)))
        if len(userValues_BIZ) == 1000:
            mysql_BIZ.insert_new_data(sql_BIZ_1, userValues_BIZ)
            userValues_BIZ = []

    mysql_BIZ.commit()

#gpt帮我优化的：将鉴权用户数据插入到已签约用户表中
def Insert_sign_user_new(filename):
    mysql_BIZ = DB_BIZ()
    mysql_BIZ.init()

    created_time = time.strftime('%Y-%m-%d %H:%M:%S')
    update_time = time.strftime('%Y-%m-%d %H:%M:%S')
    userValues_BIZ = []
    sql_BIZ_1 = "INSERT INTO user_signed_info(created_time, group_name, id_card, legal_user, msisdn,name,update_time) VALUES (%s,%s,%s,%s,%s,%s,%s)"

    workbook = openpyxl.load_workbook(filename)
    sheet = workbook['鉴权终端用户数据']

    # 遍历行
    for row in sheet.iter_rows(min_row=2):
        # 获取单元格数据
        name = row[0].value
        msisdn = row[1].value
        id_card = row[2].value
        group_name = row[3].value
        userValues_BIZ.append((created_time, group_name, id_card, 1, msisdn, name, update_time))

        # 如果userValues_BIZ列表长度达到1000，则批量插入到数据库中
        if len(userValues_BIZ) == 1000:
            mysql_BIZ.insert_new_data(sql_BIZ_1, userValues_BIZ)
            userValues_BIZ = []

    # 如果还有未插入的数据，则批量插入到数据库中
    if len(userValues_BIZ) > 0:
        mysql_BIZ.insert_new_data(sql_BIZ_1, userValues_BIZ)

    mysql_BIZ.commit()

#自己写的
def Delete_sign_user(filename):
    mysql_BIZ = DB_BIZ()
    mysql_BIZ.init()

    workbook = openpyxl.load_workbook(filename)
    sheet = workbook['鉴权终端用户数据']
    # 遍历行
    for row in sheet.iter_rows(min_row=2):
        # 获取单元格数据
        name = row[0].value
        msisdn = row[1].value
        id_card = row[2].value
        group_name = row[3].value
        mysql_BIZ.delete_data("DELETE FROM user_signed_info WHERE msisdn = "+str(msisdn))

    mysql_BIZ.commit()

#gpt帮我优化的
def Delete_sign_user_new(filename):
    mysql_BIZ = DB_BIZ()
    mysql_BIZ.init()

    workbook = openpyxl.load_workbook(filename)
    sheet = workbook['鉴权终端用户数据']
    # 获取所有用户数据的msisdn值，并拼接成一个逗号分隔的字符串
    msisdns = ",".join([str(row[1].value) for row in sheet.iter_rows(min_row=2)])

    # 执行单个SQL语句，批量删除所有用户数据
    mysql_BIZ.delete_data("DELETE FROM user_signed_info WHERE msisdn IN ({})".format(msisdns))

    mysql_BIZ.commit()
def Delete_common_user_new(filename):
    mysql_BIZ = DB_BIZ()
    mysql_BIZ.init()

    workbook = openpyxl.load_workbook(filename)
    sheet = workbook['企业用户数据']
    # 获取所有用户数据的msisdn值，并拼接成一个逗号分隔的字符串
    msisdns = ",".join([str(row[1].value) for row in sheet.iter_rows(min_row=2)])

    # 执行单个SQL语句，批量删除所有用户数据
    mysql_BIZ.delete_data("DELETE FROM biz_commons_user WHERE msisdn IN ({})".format(msisdns))

    mysql_BIZ.commit()

def Delete_common_user_auth_user(filename):
    mysql_BIZ = DB_BIZ()
    mysql_BIZ.init()

    workbook = openpyxl.load_workbook(filename)
    sheet = workbook['鉴权终端用户数据']
    # 获取所有用户数据的msisdn值，并拼接成一个逗号分隔的字符串
    msisdns = ",".join([str(row[1].value) for row in sheet.iter_rows(min_row=2)])

    # 执行单个SQL语句，批量删除所有用户数据
    mysql_BIZ.delete_data("DELETE FROM biz_commons_user WHERE msisdn IN ({})".format(msisdns))

    mysql_BIZ.commit()

if __name__ == '__main__':
    time_start = time.time()
    print("start time: ", time.strftime('%Y-%m-%d %H:%M:%S'))
    Insert_sign_user_new('/Users/hejian/Desktop/联通数科/性能测试数据/鉴权性能测试数据/user/auth-user-10000-20230403155805.xlsx')
    # Insert_sign_user('/Users/hejian/Desktop/联通数科/性能测试数据/鉴权性能测试数据/auth-user-10000-20230331115920.xlsx')
    # Delete_sign_user('/Users/hejian/Desktop/联通数科/性能测试数据/鉴权性能测试数据/auth-user-10000-20230331115920.xlsx')
    # Delete_sign_user_new('/Users/hejian/Desktop/联通数科/性能测试数据/鉴权性能测试数据/auth-user-10000-20230331115920.xlsx')
    # Delete_common_user_new('/Users/hejian/Desktop/联通数科/性能测试数据/签约性能测试数据/sign-50000-20230403153329.xlsx')
    # Delete_common_user_auth_user('/Users/hejian/Desktop/联通数科/性能测试数据/鉴权性能测试数据/user/auth-user-1000-20230403155839.xlsx')
    time_end = time.time()
    print("finish time: ", time.strftime('%Y-%m-%d %H:%M:%S'))
    print("cost time: ", time_end - time_start)