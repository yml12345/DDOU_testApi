#！/user/bin/env python
#-*- coding:utf-8 -*-
#Author: xiaochao
class ExcelVaribles:
	#用例id
	CaseID = 0
	#请求地址
	CaseUrl = 3
	#前置条件
	CasePre = 4
	#请求方法
	Method = 5
	#请求参数类型
	ParamsType = 6
	#引用链接
	Referer = 7
	#请求参数
	Params = 8
	#期望结果
	Expect = 9
	#是否运行
	IsRun = 10

	def getCaseID(self):
	#获取用例ID
		return ExcelVaribles.CaseID

	def getUrl(self):
		#获取请求地址
		return ExcelVaribles.CaseUrl
	def getCasePre(self):
		#获取前置条件
		return ExcelVaribles.CasePre
	def getMethod(self):
		#获取请求方法
		return ExcelVaribles.Method
	def getParamsType(self):
		#获取请求参数类型
		return ExcelVaribles.ParamsType
	def getReferer(self):
		#获取引用链接
		return ExcelVaribles.Referer
	def getParams(self):
		#获取请求参数
		return ExcelVaribles.Params
	def getExpect(self):
		#获取期望结果
		return ExcelVaribles.Expect
	def getIsRun(self):
		#获取是否运行
		return ExcelVaribles.IsRun


