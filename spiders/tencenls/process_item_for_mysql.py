# _*_ coding:utf-8 _*_

import json
import pymongo
import redis
import MySQLdb

def process_item():
    # 创建redis数据库链接
    rediscli = redis.Redis(host='127.0.0.1', port=6379, db='0')
    # 创建Mysql数据库链接
    mysqlcli = MySQLdb.connect(host='127.0.0.1', port=3306,user="lanboo",passwd="lanboo",db="youyuan")

    offset = 0

    while True:

        #将数据从redis 里pop出来
        source,data = rediscli.blpop("yy:items")

        #json 转换一下
        item = json.loads(data)

        #创建mysql 操作游标对象 ,可以执行mysql语句
        cursor = mysqlcli.cursor()

        cursor.execute("insert into bejing_18_25_mm (username,age,header_url,imgaes_url,content,palce_from,education,hobby,source_url,source,time,spidername) values  \
                        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" %\
                        (item['username'],item['age'],item['header_url'],item['imgaes_url'],item['content'],item['palce_from'],item['education'],item['hobby'],item['source_url'],item['source'],item['time'],item['spidername']))

        #提交事物
        mysqlcli.commit()
        #关闭游标
        cursor.close()

        offset += 1
        print offset


if __name__ == "__main__":
    process_item()