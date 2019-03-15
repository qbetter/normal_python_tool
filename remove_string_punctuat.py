# -- coding: utf-8 --
import time
import copy
import os
import sys
import json
import re,string

def is_legal_word(uchar):
    """判断一个unicode是否是汉字"""
    if(uchar >= u'\u4E00' and uchar <= u'\u9FA5'):
        #print("1")
        return True
    elif(uchar >= u'\u0030' and uchar <= u'\u0039'):
        #print("2")
        return True
    elif(( uchar >= u'\u0041' and uchar <= u'\u005A' ) or ( uchar >= u'\u0061' and uchar <= u'\u007A')):
        #print("3")
        return uchar.lower()
    else:
        return False

def remove_nonch(kw):
    kw_tmp = ""
    #如果是纯英文单词中间的空格只保留一个
    if(all(c in string.ascii_letters or c == " " for c in kw)):
        if(len(kw)>20):
            return kw_tmp
        #print("I't pure alpha")
        tmp_s = list(kw.split(" "))
        kw_tmp = ' '.join(e for e in tmp_s if e is not "")
        return kw_tmp
    if(len(kw)>10):
        #print(len(kw))
        return kw_tmp 
    else:
        for e in kw:
            #print(e)
            re = is_legal_word(e) 
            if(re == False):
                continue
            elif(re == True):
                kw_tmp += e
            else:
                kw_tmp += re
    
    return kw_tmp

