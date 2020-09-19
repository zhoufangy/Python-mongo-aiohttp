from pymongo import MongoClient
from config.setting import config

mongo_config = config["mongo"]


class Mongo(object):

    @staticmethod
    async def get_db():
        conn = MongoClient(mongo_config["host"], mongo_config["port"])
        db = conn.demo_db
        db.authenticate(mongo_config["mechanism"], mongo_config["authobject"])
        return db


# client = MongoClient('127.0.0.1' ,27017)
# demo = client.demo_db
# demo.authenticate("dev","Aa123456")
# addr = demo.address
# # res = addr.find()
# # for row in res :
# #     print(row)
# x = addr.find_one()
# y = x['address']
# print(y)