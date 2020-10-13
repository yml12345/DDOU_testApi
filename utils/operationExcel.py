#！/user/bin/env python
#-*- coding:utf-8 -*-
#Author: xiaochao

import xlrd
from xlutils.copy import copy
from utils.public import PublicMethod
from utils.excelData import ExcelVaribles

class OperationExcel:
	def __init__(self):
		self.pm = PublicMethod()
		self.ex = ExcelVaribles()

	def getExcel(self):
		'''打开要操作的文件'''
		db = xlrd.open_workbook(self.pm.data_dir('data','data.xls'))
		'''找到要操作的第几个sheet，索引从0开始'''
		sheet = db.sheet_by_index(0)
		return sheet

	def get_rows(self):
		'''获取excel的行数'''
		return self.getExcel().nrows

	def get_row_cel(self,row,col):
		'''获取单元格的内容'''
		return self.getExcel().cell_value(row,col)

	def get_CaseID(self,row):
		'''获取用例ID'''
		return self.get_row_cel(row,self.ex.getCaseID())

	def get_Url(self,row):
		'''获取请求地址'''
		return self.get_row_cel(row,self.ex.getUrl())
	def get_CasePre(self,row):
		#获取前置条件
		return self.get_row_cel(row,self.ex.getCasePre())
	def get_Method(self,row):
		#获取请求方法
		return self.get_row_cel(row,self.ex.getMethod())
	def get_ParamsType(self,row):
		#获取请求参数类型
		return self.get_row_cel(row,self.ex.getParamsType())
	def get_Referer(self,row):
		#获取请求引用链接
		return self.get_row_cel(row,self.ex.getReferer())
	def get_Params(self,row):
		'''获取请求参数'''
		return self.get_row_cel(row,self.ex.getParams())

	def get_Expect(self,row):
		'''获取期望结果'''
		return self.get_row_cel(row,self.ex.getExpect())

	def get_IsRun(self,row):
		'''获取是否运行'''
		return self.get_row_cel(row,self.ex.getIsRun())


if __name__ == '__main__':
	print(OperationExcel().get_Url(1))
	print(OperationExcel().get_Url(2))
	# def writeResult(self,row,content):
	# 	'''测试结果写到文件中'''
	# 	#获取实际结果的列
	# 	col=getResult()
	# 	#打开要写入的文件
	# 	work =xlrd.open_workbook(self.pm.data_dir(file='data',fileName='data.xls'))
	# 	old_content = copy(work)
	# 	ws = old_content.get_sheet(0)
	# 	ws.write(row,col,content)
	# 	old_content.save(self.pm.data_dir('data','data.xls'))
	#
	#
	# def run_success_result(self):
	# 	'''获取执行成功的用例数'''
	# 	#将result为pass内容的数量写入到这个列表
	# 	pass_count=[]
	# 	#执行失败的为fail_count
	# 	fail_count=None
	# 	#range(1,self.get_rows())索引是从0开始，第0行是title，所以从1开始循环读取
	# 	for i in range(1,self.get_rows()):
	# 		#i代表行
	# 		if self.getResult(i)=='pass':
	# 			pass_count.append(i)
	# 	return int(len(pass_count))
	#
	# def run_fail_result(self):
	# 	'''获取执行失败的用例数，用例总数-执行成功的数'''
	# 	return int((self.get_rows()-1)-self.run_success_result())
	#
	# def run_pass_rate(self):
	# 	'''测试结果通过率'''
	# 	rate=''
	# 	if self.run_fail_result()==0:
	# 		rate='100%'
	# 	elif self.run_fail_result()!=0:
	# 		rate=str(int(self.run_success_result()/int(self.get_rows()-1)*100))+'%'
	# 	return rate

# print(OperationExcel().getExpect(1))