#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author: Peng Chao

import datetime
import requests
import json
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson
from utils.public import PublicMethod
from config.getConfig import Config

class WebMethon(PublicMethod):
	def __init__(self):
		self.config = Config()
		self.excel = OperationExcel()
		self.public = PublicMethod()
		self.json = OperationJson()

#=================封装请求头，s=0，未登录的请求头。s=1，已登陆的请求头==============================
	def getHeadersInfo(self,row,):
				'''已登录的请求头'''
				headers = {
					'Host':self.config.getHost(),
					#'Content-Type': self.excel.get_ParamsType(row=row),
					'Accept-Encoding': 'gzip, deflate',
					'Cookie':'Hm_lvt_950d894867df0a55fbb3239fba8837ea=1588758701,1588774347,1588833146,1588856383',
					'Accept': '*/*',
					'User-Agent': 'DDOU/1.0.3 (iPhone; iOS 13.3.1; Scale/3.00)',
					'Authorization' :self.public.getFile('data','login','token'),
					#'Referer': self.config.getUrl()[0]+self.excel.get_Referer(row=row)
				}
				return headers

	def post(self,s,row,**kwargs):

		'''
		请求参数是json格式的post，这里读取的是excel+json文件中的数据
		s=1:json格式的参数
		s=2：data格式的参数
		'''
		if s == 1:
			try:
				r = requests.post(
					url=self.config.getUrl()[0]+self.excel.get_Url(row=row),
					json=self.json.getRequestsData(row=row),
					headers=self.getHeadersInfo(row=row),
					timeout=5
				)
				return r
			except Exception as e:
				raise RuntimeError('接口请求法生未知的错误')
		elif s == 2:
			'''请求方法是data格式的post，这里读取得是excel文件中的数据'''
			try:
				r = requests.post(
					url=self.excel.get_Url(row=row),
					data=self.excel.get_Params(row=row),
					headers=self.getHeadersInfo(row=row),
					timeout=5
				)
				return r
			except Exception as e:
				raise RuntimeError('接口请求法生未知的错误')
		else:
			print('Eorr:请检查请求参数!')

	def get(self,url,params=None):
		'''对get请求进行二次封装'''
		r = requests.get(url=url,params=params,headers=self.getHeadersInfo(),timeout=5)
		return r



#=========判断返回数据中包不包含excel预取结果的数据，如果包含就返回True，如果不包含就返回False======================================================================
class IsContent:
	def __init__(self):
		'''对OperationExcel类实例化'''
		self.excel = OperationExcel()

	def isContent(self,row,str2):
		flag = None
		'''st2中有excel.getExpect返回的内容就return回true，否则return回False'''
		if json.dumps(json.dumps(self.excel.get_Expect(row=row)) in str2):
		#if self.excel.getExpect(row=row) in str2:
			flag = True
		else:
			flag = False
		return flag






# class AppMethon(WebMethon):
# 	def __init__(self):
# 		self.operationJson = OperationJson()
# 		self.excel = OperationExcel()
# 		self.pm = PublicMethod()
# 		self.config = Config()
# #=========封装未登录的post请求post。s=1，请求格式为json格式的post；s=2，请求格式为data的post，对请求数据重新赋值的post===========================================================
# 	#未登录情况下的post请求
# 	def post(self,s,row,data=None):
# 		'''请求参数是json格式的post，这里读取的是excel+json文件中的数据'''
# 		headers = {
# 			'Agent-AppAuth': self.config.getAuth()[0],
# 			'Content-Type': self.excel.getContentType(row=row),
# 			'User-Agent': 'okhttp/3.12.0'
# 		}
#
# 		if s == 1:
# 			try:
# 				r = requests.post(
# 					url=self.config.getUrl()[0]+self.excel.get_url(row=row),
# 					json=self.operationJson.getRequestsData(row=row),
# 					headers=headers,
# 					timeout=5
# 				)
# 				#print("url:",self.config.getUrl()[0]+self.excel.get_url(row=row),"json:",self.operationJson.getRequestsData(row=row),"headers:",self.postHeadersValue(row=row))
# 				return r
# 			except Exception as e:
# 				raise RuntimeError('接口请求法生未知的错误')
# 		elif s == 2:
# 			'''请求方法是data格式的post，这里读取得是excel文件中的数据'''
# 			try:
# 				r = requests.post(
# 					url=self.config.getUrl()[0]+self.excel.get_url(row=row),
# 					data=self.excel.get_request_data(row=row),
# 					headers=headers,
# 					timeout=5
# 				)
# 				return r
# 			except Exception as e:
# 				raise RuntimeError('接口请求法生未知的错误')
# 		elif s ==3:
# 			try:
# 				r = requests.post(
# 					url=self.config.getUrl()[0]+self.excel.get_url(row=row),
# 					json=data,
# 					headers=headers,
# 					timeout=5
# 				)
# 				return r
# 			except Exception as e:
# 				raise RuntimeError('接口请求法生未知的错误')
#
# 		else:
# 			print('Eorr:请检查请求参数!')
# #=========封装已登录的post请求post2。s=1，请求格式为json格式的post；s=2，请求格式为data的post，对请求数据重新赋值的post==================
# 	# 成功登陆后的post请求
# 	def post2(self, s, row, data=None):
#
# 		headers = {
# 			'Agent-AppAuth': self.pm.getFile('data', 'login', 'Token'),
# 			'Content-Type': self.excel.getContentType(row=row),
# 			'User-Agent': 'okhttp/3.12.0'
# 		}
#
# 		if s == 1:
# 			try:
# 				r = requests.post(
# 					url=self.config.getUrl()[0] + self.excel.get_url(row=row),
# 					json=self.operationJson.getRequestsData(row=row),
# 					headers=headers,
# 					timeout=5
# 				)
# 				# print("url:",self.config.getUrl()[0]+self.excel.get_url(row=row),"json:",self.operationJson.getRequestsData(row=row),"headers:",self.postHeadersValue(row=row))
# 				return r
# 			except Exception as e:
# 				raise RuntimeError('接口请求法生未知的错误')
# 		elif s == 2:
# 			'''请求方法是data格式的post，这里读取得是excel文件中的数据'''
# 			try:
# 				r = requests.post(
# 					url=self.config.getUrl()[0] + self.excel.get_url(row=row),
# 					data=self.excel.get_request_data(row=row),
# 					headers=headers,
# 					timeout=5
# 				)
# 				return r
# 			except Exception as e:
# 				raise RuntimeError('接口请求法生未知的错误')
# 		elif s == 3:
# 			try:
# 				r = requests.post(
# 					url=self.config.getUrl()[0] + self.excel.get_url(row=row),
# 					json=data,
# 					headers=headers,
# 					timeout=5
# 				)
# 				return r
# 			except Exception as e:
# 				raise RuntimeError('接口请求法生未知的错误')
#
# 		else:
# 			print('Eorr:请检查请求参数!')
# #=========封装get请求，s=1，未登录，s=2，已登录=========================================
# 	def get(self,s,row,params=None):
# 		if s == 1:
# 			'''对get请求进行二次封装'''
# 			try:
# 				header = {
# 					'Agent-AppAuth': self.config.getAuth()[0],
# 					'User-Agent': 'okhttp/3.12.0'
# 				}
# 				r = requests.get(url=self.config.getUrl()[0]+self.excel.get_url(row=row),params=params,headers=header,timeout=5)
# 				return r
# 			except Exception as e:
# 				raise RuntimeError('接口请求法生未知的错误')
# 		elif s ==2:
# 			#成功登陆后
# 			try:
# 				header = {
# 					'Agent-AppAuth': self.pm.getFile('data','login','Token'),
# 					'User-Agent': 'okhttp/3.12.0',
# 					'Host':'yunappapi.zhangguishangcheng.shop',
# 					'Accept-Encoding':'gzip'
# 				}
# 				r = requests.get(url=self.config.getUrl()[0]+self.excel.get_url(row=row),params=params,headers=header,timeout=5)
# 				return r
# 			except Exception as e:
# 				raise RuntimeError('接口请求法生未知的错误')


# a = 1
# sum = 0
# for i in range(1,10):
#     for j in range(1,i+1):
#         sum = i*j
#         print("%dx%d=%d"%(i,j,sum),end=" ")
#     print("")


