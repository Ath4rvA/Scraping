# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from mysql import connector
import os

class QuotetutorialPipeline:

    def __init__(self):
        self.create_table()

    def create_table(self):
        self.db = connector.connect(host="localhost", user=os.environ.get('DB_UNAME'),
                                    passwd=os.environ.get('DB_PWORD'), database='classwork')
        cursor = self.db.cursor()
        cursor.execute('drop table if exists crawl_test')
        cursor.execute(
            'create table crawl_test (quote text, author varchar(50), tag varchar(50))')
        self.db.commit()
        cursor.close()

    def store(self, item):

        cursor = self.db.cursor()
        query = """insert into crawl_test values (%s,%s,%s)"""
        tag = 'NA'
        try:
            tag = item['tags'][0]
        except:
            pass
        data = (item['quote'], item['author'], tag)
        cursor.execute(query, data)
        self.db.commit()
        cursor.close()

    def process_item(self, item, spider):
        self.store(item)
        # return item
