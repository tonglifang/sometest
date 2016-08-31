#!/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *
from datetime import date

# 新建数据库 db


#表格模型 Person：这是一个Model的概念
db = MySQLDatabase(
    database = 'castle',# string
    passwd = '', # string
    user = 'root', # string
    host = 'localhost', # string
    port = 3306, # int, 可不写
)
class BaseModel(Model):
    class Meta:
        database = db  

class Person(BaseModel):
    #CharField 为抽象数据类型 相当于 varchar
    id = int
    name = CharField()
    #DateField 相当于 date
    birthday = DateField()
    #BooleanField 相当于 bool
    is_relative = BooleanField()
    class Meta:
        db_table = 'Person'

    

#表格模型 Pet
class Pet(BaseModel):
    #外连接的声明(和Person关联)
    owner = ForeignKeyField(Person,db_column='owner', related_name='pets')
    name = CharField()
    animal_type = CharField()
    class Meta:
        db_table = 'Pet'


class User(BaseModel):
	name = CharField()

   
#连接数据库db
def create_tables():
	db.connect();
	# per = Person()
	# per.name = 'hahah'
	# per.birthday = '2012-1-11'
	# per.is_relative = False
	# per.save()
	# per.create()
	# db.create_tables([Person, Pet])
	# data = Person.select().get()#.where(Person.id ==1).get()
	# for d in data:
	# 	print d.id
	try:
		pet = Pet()
		pet.owner =5
		pet.name = 'heheh'
		pet.animal_type = '狗'
		pet.save()
		pass
	except Exception, e:
		print '数据插入失败'
		raise
	else:
		pass
	finally:
		pass
	
	pass

if __name__ == "__main__":
	create_tables()