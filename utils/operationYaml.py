#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:PC

import yaml
from utils.public import *

class OperationYaml:
	def __init__(self):
		self.dir = PublicMethod()
	'''循环读取yaml文件，针对单个api'''
	def readYaml(self):
		with open(self.dir.data_dir(file='data',fileName='log.yaml'),'r',encoding='utf-8')as f:
			return list(yaml.safe_load_all(f))

	def dictYaml(self,fileDir='data',fileName='login001.yaml'):
		with open(self.dir.data_dir(file=fileDir,fileName=fileName),'r',encoding='utf-8')as  f:
			return yaml.safe_load(f)

if __name__ == '__main__':
	obj = OperationYaml()
	print(obj.readYaml())
	print(type(obj.readYaml()))
	#print(obj.dictYaml())

	# for item in obj.readYaml():
	# 	print(item)