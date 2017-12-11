# -*- coding: utf-8 -*-

"""
=======================================
[Function]
    子模块：读取文本

[Date]
    Create : 2017-05-25
    Update : 2017-05-25

[Version]
    1.0
=======================================
"""



# ======================== 文本文件 ==========================

# 读取文本文件
import chardet

# 读取文本文件
def Read_Text_File( file_path):
    #配置存到列表all_line_list中
    all_line_list = []
    text_file = open( file_path , "rb")
    value = text_file.readlines()
    for e in value:
        r = chardet.detect(e)
        if r.get('encoding') == 'utf-8':
            all_line_list.append(e.decode('utf-8').replace('\r\n','').replace('\n',''))
        elif r.get('encoding') =='ascii':
            all_line_list.append(e.decode('ascii').replace('\r\n','').replace('\n',''))
        else:
            all_line_list.append(e.decode('gbk',errors='ignore').replace('\r\n','').replace('\n',''))

    return all_line_list