#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author: Peng Chao

import os
import configparser
from utils.public import PublicMethod

class Config:
	def __init__(self):
		self.pm = PublicMethod()

	def getHost(self,fileName = 'host'):
		#获取host
		list1 = []
		config = configparser.ConfigParser()
		config.read(self.pm.data_dir(file='config',fileName = 'config.ini'),encoding='UTF-8')
		host = config.get(fileName,'host')
		list1.append([host])
		return list1[0]
	def getLogin(self,fileName = 'login'):
		'''读取配置文件中登陆的数据'''
		list1 = []
		config = configparser.ConfigParser()
		config.read(self.pm.data_dir(file='config',fileName='config.ini'),encoding='UTF-8')
		phone = config.get(fileName,'phone')
		passWord = config.get(fileName, 'Password')
		list1.append([phone,passWord])
		return list1[0]

	def getEmail(self,fileName = 'email'):
		'''读取配置文件中邮箱的数据'''
		list1 = []
		config = configparser.ConfigParser()
		config.read(self.pm.data_dir(file='config',fileName='config.ini'),encoding='UTF-8')
		user = config.get(fileName,'user')
		passWord = config.get(fileName, 'password')
		list1.append([user,passWord])
		return list1[0]

	def getMysql(self,fileName = 'SQL Service'):
		'''读取配置文件中链接数据库的数据'''
		list1 = []
		config = configparser.ConfigParser()
		config.read(self.pm.data_dir(file='config',fileName='config.ini'),encoding='UTF-8')
		host = config.get(fileName,'host')
		user = config.get(fileName,'user')
		passwd = config.get(fileName, 'passwd')
		db = config.get(fileName,'db')
		list1.append([host,user,passwd,db])
		return list1[0]

	def getUrl(self,fileName = 'url'):
		'''读取配置文件中URL'''
		url = None
		config = configparser.ConfigParser()
		config.read(self.pm.data_dir(file='config',fileName='config.ini'),encoding='UTF-8')
		url = config.get(fileName,'url')
		url = url
		return url

	def getAuth(self,fileName = 'AppAuth'):
		'''读取配置文件中地址的信息'''
		list1 = []
		config = configparser.ConfigParser()
		config.read(self.pm.data_dir(file='config',fileName='config.ini'),encoding='UTF-8')
		Auth = config.get(fileName,'Auth')
		list1.append([Auth])
		return list1[0]

if __name__ == '__main__':
	import json
	print(Config().getLogin(),type(Config().getLogin()))
	print(Config().getUrl())
	print(Config().getLogin()[0],Config().getLogin()[1])
	lg = json.dumps(Config().getLogin()[0])
	print(lg, type(lg))