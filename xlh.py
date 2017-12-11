#coding: utf-8

import os
import re

def readtxt(filename):
    mylist = []
    f = open(filename,'r')
    all = f.readlines()
    f.close()
    for line in all:
        mylist.append(line.replace(" ","").replace("\n",""))
    print (mylist)
    return mylist

def findxlh(mylist):
    xlh_list = readtxt("xlh.txt")
    for xlh in xlh_list:
        xlh_num = re.compile(xlh)
        if re.findall(xlh_num,mylist):
            return xlh

def main():
    workpath = os.getcwd()
    datapath = os.path.join(workpath,"data")
    data_list = os.listdir(datapath)
    for i in data_list:
        filepath = os.path.join(datapath,i)
        mylist = readtxt(filepath)
        if findxlh(mylist):
            txtfile = os.path.split(i)[0]
            print ("%s 中存在序列号 %s",(txtfile,findxlh(mylist)))

main()






