#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author: Peng Chao

import json
from utils.public import PublicMethod
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson

pm = PublicMethod()
operJson=OperationJson()
excel = OperationExcel()


def statusCode(self, r):
	#封装返回状态码的断言信息
	self.assertEqual(r.json()['Status'], True)
	self.assertEqual(r.json()['ResponseCode'], 0)

def assertTrue(self, row, r):
	#封装返回结果与预期结果对比断言的信息
	self.assertTrue(self.p.isContent(row, r.text))

def getCategoryCode():
	#获取存到文件中的code，存的是str，读出来拆分成列表
	code =pm.getFile('data','login','CategoryCode')
	cs = code.split(',')
	return cs

def setCategoryCode(row,X=1):#x=1默认取第一个类目的code
	'''对json文件中的CategoryCode重新赋值'''
	dict1 = operJson.getRequestsData(row=row)
	dict1["CategoryCode"] = getCategoryCode()[X]
	#print(dict1)
	return dict1

#
# def isContent():
# 	s1 = "123456"
# 	s2 = "ABSE123456"
# 	flag = None
# 	'''st2中有excel.getExpect返回得内容就return回true，否则return回False'''
# 	if s1 in s2:
# 		flag = True
# 		print(flag)
# 	else:
# 		flag = False
# 		print(flag)
# 	#return flag
# isContent()



# s =[1083, 1082]
# print(s,type(s),','.join(s))
