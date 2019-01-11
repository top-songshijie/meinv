# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors

class MeinvPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='',  # 数据库地址
            port=3306,  # 数据库端口
            db='',  # 数据库名
            user='',  # 数据库用户名
            passwd='',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.cursor.execute(
            """insert into ssj_meinv(title,imgurl)
            value (%s, %s)""",  # 纯属python操作mysql知识，不熟悉请恶补
            (item['title'],  # item里面定义的字段和表字段对应
             item['imgurl']))
        # 提交sql语句
        self.connect.commit()
        return item  # 必须实现返回
