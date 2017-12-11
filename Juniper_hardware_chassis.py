# -*- coding:utf-8 -*-
# Author chen

import re,os

# 读取text文件
def reader_text(file_path):
    text_list = []
    try:
        text_file = open(file_path, "r",encoding='gb2312')
        all_text = text_file.readlines()
        text_file.close()
        for Echo_Line in all_text:
            text_list.append(Echo_Line.replace("\n", ""))
    except:
        print("打开 %s 文件错误！请检查是否存在该文件！" % file_path)
    return text_list

def write_text(file_path):
    # ->get chassis
    #SZ7FC01U01-ZFB-FW02(B)->
    pass


