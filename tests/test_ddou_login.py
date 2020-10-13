#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author: Peng Chao
import requests
import json
import unittest
from config.getConfig import Config
from logs.logs import Logger
from base.method import WebMethon,IsContent
from utils.operationExcel import OperationExcel
from utils.public import PublicMethod
from utils.operationJson import OperationJson


class Login(unittest.TestCase):
	def setUp(self):
		self.methon = WebMethon()
		self.config = Config()
		self.excel = OperationExcel()
		self.pm = PublicMethod()
		self.operationJson = OperationJson()
		self.iscontent = IsContent()

	def tearDown(self):
		print('测试结束')

	def test_Login_001(self):
		'''
		登陆DDOU：/api/login
		:return:
		'''

		r = requests.post(
			url=self.config.getUrl()+self.excel.get_Url(1),
			json=self.operationJson.getRequestsData(1))
		print(r.json())
		self.assertTrue(r.json()['msg'],"成功")
		self.assertTrue(self.iscontent.isContent(1, r.text))

		#将登陆成功后得token写入到文件中
		#self.pm.writeFile('data','login','token',r.json()['Data']['token'])


if __name__ == '__main__':
	unittest.main(verbosity=2)