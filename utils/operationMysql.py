#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author: Peng Chao

import pymysql
from  config.getConfig import Config

con = Config()
def connMySQL():
	try:
		#链接mysql
		conn = pymysql.connect(
			host = con.getMysql()[0],
			user = con.getMysql()[1],
			passwd =con.getMysql()[2],
			db = con.getMysql()[3])
	except Exception as e:
		return e.args
	#链接成功直接执行else
	else:
		cur = conn.cursor()
		sql = 'select*from user where id=%s'
		params = 1,
		#单个语句的查询
		# cur.execute(sql, params)
		# data = cur.fetchone()
		# print(data)
		cur.execute('select * from user')
		data = cur.fetchall()
		db = [item for item in data]
		print([item for item in data])
	#else执行完成以后，关闭连接池
	finally:
		pass
		# cur.close()
		# conn.close()


def insertMySQL():
	try:
		#链接mysql
		conn = pymysql.connect(
			host=con.getMysql()[0],
			user=con.getMysql()[1],
			passwd=con.getMysql()[2],
			db=con.getMysql()[3])
	except Exception as e:
		return e.args
	#链接成功直接执行else
	else:
		cur = conn.cursor()
		sql='insert into user values (%s,%s,%s,%s)'
		params = [
			(4,'xiaochao',14,'chengdu'),
			(4,'xiaochao',18,'chengdu')
		]
		cur.executemany(sql,params)
		conn.commit()
	#else执行完成以后，关闭连接池
	finally:
		cur.close()
		conn.close()

def deleteMySQL():
	try:
		#链接mysql
		conn = pymysql.connect(
			host=con.getMysql()[0],
			user=con.getMysql()[1],
			passwd=con.getMysql()[2],
			db=con.getMysql()[3])
	except Exception as e:
		return e.args
	#链接成功直接执行else
	else:
		cur = conn.cursor()
		sql='delete from user where id = %s'
		params=(3,)
		cur.executemany(sql,params)
		conn.commit()
	#else执行完成以后，关闭连接池
	finally:
		cur.close()
		conn.close()

