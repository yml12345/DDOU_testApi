#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author: Peng Chao
import json
from page.login import *
from utils.public import PublicMethod
from utils.operationJson import OperationJson

operJson = OperationJson()
pm = PublicMethod()

#对提交询价表单的数据进行重新赋值的封装
def setCustomerinquiry(row,CommodityID,CommodityName,CommodityDetail,CommodityMaterial,
                       Amount,Province,City,Distrinct,Street,ConsigneeAddress,Imgs):
	dict1 = operJson.getRequestsData(row)
	dict1["CommodityID"]=CommodityID
	dict1["CommodityName"]=CommodityName
	dict1["CommodityDetail"]=CommodityDetail
	dict1["CommodityMaterial"]=CommodityMaterial
	dict1["Amount"]=Amount
	dict1["Province"]=Province
	dict1["City"]=City
	dict1["Distrinct"]=Distrinct
	dict1["Street"]=Street
	dict1["ConsigneeAddress"]=ConsigneeAddress
	dict1["Imgs"]=Imgs
	return dict1

def setShopCart(row,CommodityID,Amount):
	dict1 = operJson.getRequestsData(row)
	dict1["CommodityID"] = CommodityID
	dict1["Amount"] = Amount
	return dict1

def setcartID(row,CartIDs):
	dict1 = operJson.getRequestsData(row)
	dict1["CartIDs"] = CartIDs
	return dict1

def getcartID():
	#获取存到文件中的cartID，存的是str，读出来拆分成列表
	cartID =pm.getFile('data','enquirydata','cartID')
	cs = cartID.split(',')
	return cs

#对提交询价表单的数据进行重新赋值的封装
def setAddress(row,ReceiveName,Mobile,Sex,Province,
               City,Distrinct,Address,AddressID,IsDefault,OperateType,ensure_ascii=False):
	dict1 = operJson.getRequestsData(row)
	dict1["ReceiveName"]=ReceiveName
	dict1["Mobile"]=Mobile
	dict1["Sex"]=Sex
	dict1["Province"]=Province
	dict1["City"]=City
	dict1["Distrinct"]=Distrinct
	dict1["Address"]=Address
	dict1["AddressID"]=AddressID
	dict1["IsDefault"]=IsDefault
	dict1["OperateType"]=OperateType
	return dict1
#通过购物车提交订单
def setOrderData(row,SettlementType,PaymentType):
	dict1 = operJson.getRequestsData(row)
	#购物车ID
	dict1['CartIDs'] = getcartID()[0]
	dict1['SettlementType'] = SettlementType
	dict1['PaymentType'] = PaymentType
	return dict1

#通过详情确认订单,Amout:购买得数量
def setConfirmOrder(row,Amout):
	dict1 = operJson.getRequestsData(row)
	dict1['CommodityID'] = pm.getFile('data','login','CommodityID')
	dict1['Amout'] = Amout
	return dict1

#通过详情页提交订单，Amount：购买数量，SettlementType:结算方式，PaymentType:支付方式
def setOrdersData(row,Amount,SettlementType,PaymentType):
	dict1 = operJson.getRequestsData(row)
	#购物车ID
	dict1['CommodityID'] = pm.getFile('data','login','CommodityID')
	dict1['Amount'] = Amount
	dict1['SettlementType'] = SettlementType
	dict1['PaymentType'] = PaymentType
	return dict1

