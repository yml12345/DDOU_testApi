#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author: Peng Chao

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
		pass

	def test_Login_001(self):
		'''
		登陆大桶大后台系统：/Account/Login
		:return:
		'''
		r = self.methon.post(0,1)
		self.assertTrue(r.json()['IsSuccess'],True)
		self.assertTrue(self.iscontent.isContent(1, r.text))

		#将登陆成功后得token写入到文件中
		self.pm.writeFile('data','login','token',r.json()['Data']['token'])


if __name__ == '__main__':
    unittest.main(verbosity=2)