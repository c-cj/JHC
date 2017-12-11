# -*- coding:utf-8 -*-
# Author chen

import re,os


#获得hostname
def get_hostname(config):
    reg1 = re.compile('(?P<hostname>[^(]+)(\((?P<status>[\w])\))?->.*')
    for eachline in config:
        p1 = reg1.search(eachline)
        if p1:
            hostname = p1.group('hostname')
            status = p1.group('status')
            if not status or status == 'M' or status == 'B':
                return hostname
            else:
                return hostname,status

#获得设备型号
def get_Product_Name(config):
    #Product Name: SSG-350M
    reg = re.compile('Product Name: (?P<pro_name>[\S]+)')
    for eachline in config:
        p1 = reg.search(eachline)
        if p1:
            pro_name = p1.group('pro_name')

            return pro_name
    return


# 返回序列号
def get_SN(config):
    reg = re.compile('Serial Number: (?P<sn>[\S]+), .*')
    for each in config:
        p = re.search(reg,each)
        if p:
            sn = p.group('sn')
            return sn
    return

#定义获取获取产品序列号的类
class Get_chassis(object):
    def __init__(self,config):
        self.config = config

    def get_hostname(self):
        reg1 = re.compile('(?P<hostname>[^(]+)(\((?P<status>[\w])\))?->.*')
        for eachline in self.config:
            p1 = reg1.search(eachline)
            if p1:
                hostname = p1.group('hostname')
                status = p1.group('status')
                if not status or status == 'M' or status == 'B':
                    return hostname
                else:
                    return hostname,status


"""
SZ7FC03U22-YUN-FW01(M)-> get chassis
Chassis Environment:
  Power Supply: Good
  Fan Status: Good
CPU Temperature: 104'F ( 40'C)
Slot Information:
Slot  Type              S/N                Assembly-No  Version  Temperature
  0   System Board      0079022013000042   0051-005     F07      86'F (30'C),  93'F (34'C)
  4   Management        0252022013000001   0049-004     D19     104'F (40'C)
  5   ASIC Board        003206482E130012   0050-003     C04
      Marin FPGA version 9, Jupiter ASIC version 1, Fresno FPGA version 110
      I/O Board
      Slot  Type                     S/N                Version  FPGA version
        1   4 port miniGBIC (0x3)    0204112012000027   B02          26
        3   4 port miniGBIC (0x3)    0204042013000067   B02          26
Alarm Control Information:
  Power failure audible alarm: disabled
  Fan failure audible alarm: disabled
  Low battery audible alarm: disabled
  Temperature audible alarm: disabled
    Normal alarm temperature is 132'F (56'C)
    Severe alarm temperature is 150'F (66'C)
"""

#SSG-550M
"""
    SZ7FC01U01-ZFB-FW02(B)->get chassis
Chassis Environment:
  Power Supply: Good
  Fan1 Status: Good
  Fan2 Status: Good
  Fan3 Status: Good
  CPU Temperature: 116'F ( 47'C)
  System Temperature:  75'F ( 24'C)

Alarm Control Information:
  Power failure audible alarm: disabled
  Fan failure audible alarm: disabled
  Temperature audible alarm: disabled
    CPU alarm temperature is 194'F (90'C)
    System alarm temperature is 149'F (65'C)

Slot Information:
Slot Name             Status   Asm-id   Serial Number    Version
 0   mgt              Online   01bf     JN1211A2FADB     REV 18
 1                    Empty
 2                    Empty
 3                    Empty
 4   8-gbsw-tx-s      Online   0732     AAFB6059         REV 13
 5                    Empty
 6                    Empty
SZ7FC01U01-ZFB-FW02(B)->
"""

#SSG350
# SSG350M与NS5400的序列号需用get system获得
"""
KXNW-FW-01(M)-> get chassis
Chassis Environment:
 I/O fan1 Status: Good
 Memory fan Status: Good
 CPU fan1 Status: Good
 CPU fan2 Status: Good
  CPU Temperature: 102'F ( 39'C)
  System Temperature:  87'F ( 31'C)

Alarm Control Information:
  Power failure audible alarm: disabled
  Fan failure audible alarm: disabled
  Temperature audible alarm: disabled
    CPU alarm temperature is 167'F (75'C)
    System alarm temperature is 167'F (75'C)

Slot Information:
Slot Name             Status   Asm-id   Serial Number    Version
 0   mgt              Online   01f1     ACLN2114         REV 05
 1                    Empty
 2                    Empty
 3                    Empty
 4                    Empty
 5                    Empty
KXNW-FW-01(M)->
SZOPC-EXT-FW-02(B)-> get system
Product Name: SSG-550M
Serial Number: JN123ED13ADB, Control Number: 00000000
"""

#NS-5400
"""
4FX13-3G_NS5400-U31_39(B)-> get chassis
Chassis Environment:
  Power Supply: Good
  Fan Status: Good
  Battery Status: Good
  CPU Temperature: 131'F (55'C)
Slot Information:
Slot  Type                 S/N                Assembly-No              Temperature    DRAM Size
 1    Management-III       0225112009000062   0072-002                 105'F (41'C)   2048MB
 2    Processing-8G2-G4-TX   0228102012000014   0045-001                 109'F (43'C)   1024MB
 3    Processing-8G2-G4-TX   0228102012000026   0084-001                 111'F (44'C)   1024MB
 4    Processing-8G2-G4-TX   0228102012000022   0084-001                 113'F (45'C)   1024MB
Alarm Control Information:
  Power failure audible alarm: disabled
  Fan failure audible alarm: disabled
  Low battery audible alarm: disabled
  Temperature audible alarm: disabled
    Normal alarm temperature is 168'F (76'C)
    Severe alarm temperature is 192'F (89'C)
4FX13-3G_NS5400-U31_39(B)->
"""

"""
get chassis

Chassis Environment:
  Power Supply: Good
  Fan Status: Good
  Battery Status: Good
  CPU Temperature: 161'F (72'C)
Slot Information:
Slot  Type                 S/N                Assembly-No              Temperature    DRAM Size
 1    Management           0102062010000017   0058-004                 132'F (56'C)   2048MB
 2    Processing-8G2       0131022013000007   0045-010                 134'F (57'C)   1024MB
Alarm Control Information:
  Power failure audible alarm: disabled
  Fan failure audible alarm: disabled
  Low battery audible alarm: disabled
  Temperature audible alarm: disabled
    Normal alarm temperature is 168'F (76'C)
    Severe alarm temperature is 192'F (89'C)

"""

def get_chassis(config):
    #Product Name: SSG-350M
    #Product Name: SSG-550M
    #Product Name: NetScreen-2000
    #Product Name: NS5400
    #Product Name: NS5200


    pro_name = -1
    cpu_temp = []
    sys_temp = []
    error_list = []
    reg = re.compile('Product Name: (?P<Pname>[\S]+)')

    for eachline1 in config:
        p = reg.search(eachline1)
        if p:
            Pname = p.group('Pname')

            if Pname == 'SSG-550M':
                pro_name = 0
            elif Pname == 'NetScreen-2000':
                pro_name = 1
            #其他防火墙需要再添加
            else:
                error_list = ['该防火墙为：%s，目前不支持该巡检' % Pname]
                return error_list
    #SSG550M温度
    if pro_name == 0:
        cpu_max_temp = 90
        sys_max_temp = 65
        reg1 = re.compile('CPU Temperature: [\S]+\'F \( (?P<temp1>[\S]+)\'C\)')
        reg2 = re.compile('System Temperature:  [\S]+\'F \( (?P<temp2>[\S]+)\'C\)')
        temp1 = ''
        temp2 = ''
        for eachline2 in config:
            p1 = reg1.search(eachline2)
            p2 = reg2.search(eachline2)

            if p1:
                temp1 = p1.group()

            if p2:
                temp2 = p2.group()

        return temp1+'\r\n'+temp2
    #ISG200温度
    elif pro_name == 1:
        norm_alarm_temp = 56
        seve_alarm_temp = 66

        reg1 = re.compile('CPU Temperature: [\S]+\'F \( (?P<temp3>[\S]+)\'C\)')
        reg2 = re.compile('[\d]+[\s]+(?P<type>[\S]+[\s]?[\S]+)[\s]+[\S]+[\s]+[\S]+[\s]+[\S]+[\s]+[\S]+\'F '
                          '\((?P<temp4>[\S]+)\'C\)(,[\s]+[\S]+\'F \((?P<temp5>[\S]+)\'C\))?')
        temp1 = ''
        for eachline2 in config:
            p1 = reg1.search(eachline2)
            p2 = reg2.search(eachline2)

            if p1:
                temp1 = p1.group()
            if p2:
                temp2 = p2.group()
                sys_temp.append(temp2)

        temp = temp1+'\r\n'+'\r\n'.join(sys_temp)
        return temp.lstrip('\r\n').rstrip('\r\n')

