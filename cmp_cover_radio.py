#!/usr/bin/env python
#-*-coding:utf-8
import re
import os
import json
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def cmp_cover(merge_hot_file,uid_file):
    uid_dict = dict()
    #merge_file = "./../data/merge_hot_data"
    with open(uid_file,'r') as pub:
        for line in pub.readlines():
            line = line.strip()
            uid_dict[line] = 1

    with open(merge_hot_file,'r') as fd:
        num  = 0
        #merge_hot_len = 0
        for line in fd.readlines():
            line = line.strip()
            uid = line.split("\t")[0]
            if uid in uid_dict:
                num = num + 1
            #merge_hot_len = merge_hot_len + 1
    print("hit number is ",num)
    cover = float(num)/len(uid_dict)
    print("cover radio is ",cover)

if __name__ == "__main__":
    # 去除推荐词中的同义词
    merge_hot_file = "./have_age_uniq_uid"
    #merge_hot_file ="./../data/user_30day_buy_query_20190702_uid"
    #merge_hot_file ="./individual_hotword_file_uid"
    uid_file = "./uid_0614"
    cmp_cover(merge_hot_file,uid_file)
