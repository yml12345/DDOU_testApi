#！/user/bin/env python
#-*- coding:utf-8 -*-
#Author: xiaochao
import os
import datetime
import time
import json
import requests

class PublicMethod:
	'''现在'''
	timer=time.strftime("%a,%d %b %Y %H:%M:%S %z")
	timers = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
	nowTime = datetime.datetime.now().strftime('%Y-%m-%d')
	nowTimeHMS = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	'''明天'''
	tomorrowTime = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
	tomorrowTimes = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
	# 过去一小时时间
	pastTime = (datetime.datetime.now() - datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
	# 后天
	afterTomorrowTime = (datetime.datetime.now() + datetime.timedelta(days=3)).strftime('%Y-%m-%d')

	def data_dirFile(self,file):
		'''
		查找文件目录
		:param file:
		:return:
		'''
		return os.path.join(os.path.dirname(os.path.dirname(__file__)), file)

	def data_dir(self,file = None,fileName = None):
		'''
		查找文件目录的路径
		:param file: 文件夹的名称
		:param fileName: 文件的名称
		:return:
		'''
		return os.path.join(os.path.dirname(os.path.dirname(__file__)),file,fileName)

	def data_dirs(self,file = None,file1 = None,fileName = None):
		'''
		查找文件目录的路径
		:param file: 文件夹的名称
		:param file1: 文件夹下面文件夹的名称
		:param fileName: 文件的名称
		:return:
		'''
		return os.path.join(os.path.dirname(os.path.dirname(__file__)),file,file1,fileName)

	def writeFile(self,file, fileName, name, content):
		'''
		把模块的code写到文件中
		:param file: 文件夹的名称
		:param fileName: 文件夹下面的文件夹名称
		:param name: 文件的名称
		:param content: 写入的内容
		:return:
		'''
		with open(self.data_dirs(file, fileName, name), 'w')as f:
			f.write(content)

	def getFile(self,file, fileName, name):
		'''
		获取写入token文件中的内容
		:param file: 文件夹的名称
		:param fileName: 文件夹下面的文件夹名称
		:param name: 文件的名称
		:return:
		'''
		with open(self.data_dirs(file, fileName, name), 'r',encoding='UTF-8')as f:
			#return json.loads(f.read())
			return f.read()



