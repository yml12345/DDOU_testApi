#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:PC

import hashlib
import base64
import smtplib
import random
import http.client,mimetypes
# 获取md5验证码
def getMD5(url, postData):
	headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	           'X-Requested-With': 'XMLHttpRequest'}
	conn = http.client.HTTPConnection('this.ismyhost.com')
	conn.request('POST', '/get_isignature', postData, headers=headers)
	response = conn.getresponse()
	return response.status, response.read()


# hash1加密
def hash1Encode(codeStr):
	hashobj = hashlib.sha1()
	hashobj.update(codeStr.encode('utf-8'))
	return hashobj.hexdigest()


# DES加密
def desEncode(desStr):
	k = des('secretKEY', padmode=PAD_PKCS5)
	encodeStr = base64.b64encode(k.encrypt(json.dumps(desStr)))
	return encodeStr