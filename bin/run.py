#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author: Peng Chao

import  unittest
import  os
import  smtplib
import HTMLTestRunner
from email.mime.text import MIMEText
#发送附件（生成的测试报告）邮件
from email.mime.multipart import MIMEMultipart
from config.getConfig import Config
from utils.operationExcel import OperationExcel
from utils.public import PublicMethod
from email.header import Header
import time


class Runner:
    def __init__(self):
       self.pm = PublicMethod()
       self.excel = OperationExcel()
#==============定义发送邮件==========
    def send_mail(self,file_new):
        #-----------1.跟发件相关的参数------
        smtpserver ='smtp.qq.com'  #发件服务器
        port = 25   #端口
        username = '496650409@qq.com' #发件箱用户名
        password = 'imwyhbbunimjcahi'        #发件箱密码
        sender = '496650409@qq.com'   #发件人邮箱
        receiver =['507195389@qq.com'] #收件人邮箱
        #'1663497322@qq.com','1255716588@qq.com'
        # ----------2.编辑邮件的内容------
        #读文件
        f = open(file_new,'rb')
        mail_body = f.read()
        f.close()

        # content = '通过数：{0} 失败数：{1} 通过率：{2}'.format(
        #     self.excel.run_success_result(),
        #     self.excel.run_fail_result(),
        #     self.excel.run_pass_rate(),
        # )
        # 邮件正文是MIMEText
        #body = MIMEText(content,_subtype='plain',_charset='utf-8')
        body = MIMEText(_text=None,_subtype='plain', _charset='utf-8')
        # 邮件对象
        msg = MIMEMultipart()
        msg['Subject'] =Header("自动化测试报告",'utf-8').encode()#主题
        msg['From'] =Header('发件人:'.format(sender))
        msg['To'] = Header('收件人:'.format(receiver))       #收件人
        msg['To'] = ','.join(receiver)
        msg['date'] = self.pm.timer
        msg.attach(body)
        # 附件
        att = MIMEText(mail_body, "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename="test_report.html"'
        msg.attach(att)
        # ----------3.发送邮件------
        try:
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver)  # 连服务器
            smtp.login(sender, password)
        except:
            smtp = smtplib.SMTP_SSL(smtpserver, port)
            smtp.login(sender, password)  # 登录
        smtp.sendmail(sender, receiver, msg.as_string())  # 发送
        smtp.quit()
        #发送邮件
        smtp = smtplib.SMTP()
        smtp.connect("smtp.qq.com")  # 邮箱服务器
        smtp.login(username, password)  # 登录邮箱
        smtp.sendmail(sender, receiver, msg.as_string())  # 发送者和接收者
        smtp.quit()
        print("邮件已发出！注意查收。")
    # ======查找测试目录，找到最新生成的测试报告文件======
    def new_report(self,test_report):
        lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
        lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))  # 按时间排序
        file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
        print(file_new)
        return file_new

    def getSuite(self):
        '''获取要执行的测试套件'''
        suite = unittest.TestLoader().discover(
            start_dir=self.pm.data_dirFile('tests'),
            pattern='test_dtd_*.py',
            top_level_dir=None)
        return suite

    def runAll(self):
        # 保存生成报告的路径
        report_path = self.pm.data_dir("report","test_Report.html")
        fp = open(report_path, 'wb')
        # 返回实例
        runner = unittest.TextTestRunner()
        # 执行所有的测试用例并发送邮件
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               title=u"DTD项目接口自动化测试报告",
                                               description=u"用例执行情况",
                                               verbosity=2
                                               ).run(self.getSuite())
        # 关闭文件，记住用open()打开文件后一定要记得关闭它，否则会占用系统的可打开文件句柄数。
        fp.close()
        # 测试报告文件夹
        test_path= self.pm.data_dirFile('report')
        new_report = self.new_report(test_path)
        self.send_mail(new_report)



if __name__ == "__main__":
    # 发送测试报告
    Runner().runAll()



