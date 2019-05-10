# _*_ coding:utf-8 _*_

import json
import pymongo
import redis

def process_item():
    # 创建redis数据库链接
    rediscli = redis.Redis(host='127.0.0.1', port=6379, db='0')
    # 创建MongoDB数据库链接
    mongodbcli = pymongo.MongoClient(host='127.0.0.1', port=27017)
    # 创建mongodb数据库名称
    dbname = mongodbcli['redis_mongodb']
    # 创建mongodb数据库表的名称
    sheetname = dbname['redis_mongodb_dgq']

    offset = 0

    while True:
        # redis 数据表名 和 数据
        source, data = rediscli.blpop("dongguanquestion:items")
        offset += 1
        # 将json对象转换为Python对象
        data = json.loads(data)
        # 将数据插入到sheetname表里
        sheetname.insert(data)
        print offset
if __name__ == "__main__":
    process_item()