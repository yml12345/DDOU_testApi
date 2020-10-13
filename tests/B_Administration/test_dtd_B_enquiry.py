#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author: Peng Chao

import unittest
import json
from page.login import *
from page.enquiry import *
from utils.public import PublicMethod
from base.method import WebMethon,IsContent

class Enquiry(unittest.TestCase):

	def setUp(self):
		self.methon = WebMethon()

		self.excel = OperationExcel()
		self.pm = PublicMethod()
		self.operationJson = OperationJson()
		self.iscontent = IsContent()

	def tearDown(self):
		pass

	def test_Enquiry_001(self):
		'''
		登陆成功，系统管理_角色与权限管理,:/Role/GetRolesPaging
		:return:
		'''
		r = self.methon.post(1,2)
		self.assertTrue(self.iscontent.isContent(2, r.text))
		self.assertTrue(r.json()['IsSuccess'],True)
		self.assertEqual(r.json()['StatusCode'], 0)























if __name__ == '__main__':
	unittest.main(verbosity=2)