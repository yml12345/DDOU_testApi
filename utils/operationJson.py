#！/user/bin/env python
#-*- coding:utf-8 -*-
#Author: xiaochao

import json
from utils.public import PublicMethod
from utils.operationExcel import OperationExcel


class OperationJson:
	def __init__(self):
		self.excel = OperationExcel()
		self.pm = PublicMethod()

	def getReadJson(self,ensure_ascii=False):
		'''读取到json文件中的内容'''
		with open(self.pm.data_dir('data','jsonData.json'),encoding='utf-8')as f:
			data = json.load(f)
			return data

	def getRequestsData(self,row,ensure_ascii=False):
		'''获取请求参数'''
		return self.getReadJson()[self.excel.get_Params(row=row)]

if __name__ == '__main__':
	os = OperationJson()
	print(os.getRequestsData(1))