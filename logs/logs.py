#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author: Peng Chao

import logging
from utils.public import PublicMethod

pm = PublicMethod()
# def log(log_content):
#     # 定义文件
#     logFile = logging.FileHandler(pm.data_dir('logs', 'logInfo.md'), 'a',encoding='utf-8')
#     # log格式
#     fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s')
#     logFile.setFormatter(fmt)
#     # 定义日志
#     logger1 = logging.Logger('logTest', level=logging.DEBUG)
#     logger1.addHandler(logFile)
#     logger1.info(log_content)


import os
import logging
from logging.handlers import TimedRotatingFileHandler


class Logger(object):
    def __init__(self, logger_name='logs…'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        #self.log_file_name = 'logs'  # 日志文件的名称
        self.backup_count = 5  # 最多存放日志的数量
        # 日志输出级别
        self.console_output_level = 'WARNING'
        self.file_output_level = 'DEBUG'
        # 日志输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        if not self.logger.handlers:  # 避免重复日志
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=pm.data_dir('logs', 'logInfo.md'), when='D',
                                                    interval=1, backupCount=self.backup_count, delay=True,
                                                    encoding='utf-8')
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger



