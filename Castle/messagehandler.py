#!/usr/bin/env python
# -*- coding: utf-8 -*-
def dealmessge(cls,message):
	if message['code'] == 0x0001:
		if message['name'] == 'tong' and message['pwd'] == '1111':
			sendmessage(cls,makesuccessmessage(0x1001,'登陆成功'))
			pass
		else:
			sendmessage(cls,makeerrormessage(0x3001,'账户密码错误'))
		pass
	else :
		sendmessage(cls,makeerrormessage(0x2001,'接口不存在'))
	pass


def sendmessage(cls,message):
	cls.write_message(message)
	pass

def makeerrormessage(code,msg):
	obj = {
	'code':code,
	'success':False,
	'msg':msg,
	'errorCode':-1
	}
	return obj

def makesuccessmessage(code,msg,data=None):
	obj = {
	'code':code,
	'success':True,
	'msg':msg,
	'result':data
	}
	return obj