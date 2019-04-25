#!/usr/bin/env python
#coding:utf-8
###########################
#将数据更改成同义词需要的样式,数据有两种格式带有=>符号的右边不能同义成左边；另一种是可以相互同义
# 比如“养乐多,益力多=>酸奶,优酸乳,果粒奶优”，搜养乐多或益力多会有同义词酸奶等，但是搜索酸奶就只有酸奶
##########################
import sys
import math
import time
import datetime


# 对互为同义的要分割一下
def word_split_normal(word):
    # word 的数据样式为： 棉衣,棉服,棉袄 =====> '棉衣,棉服','棉服,棉袄','棉衣,棉袄'
    #print(word)
    wordpart_list = list()
    word_part = word.split(',')
    for num in range(len(word_part)):
        for index in range(len(word_part)):
            if index == num:
                continue 
            strm = word_part[num] + "\t"+ word_part[index]+"\t"+"1000"
            print(strm)
            wordpart_list.append(strm)
    #print(len(wordpart_list))

def word_split_restrict(word):
    #print(word)
    wordpart_list = list()
    word_part = word.split('=>')
    if len(word_part) != 2:
        return
    left_part = word_part[0].split(",")
    right_part = word_part[1].split(",")
    for left_index in range(len(left_part)):
        for right_index in range(len(right_part)):
            strm = left_part[left_index] + "\t" + right_part[right_index]+"\t"+"1000"
            print(strm)

word_split_normal("绿植,盆栽,花卉,盆景")

word_split_restrict("养乐多,益力多=>酸奶,优酸乳,果粒奶优,果味酸奶")


def word_format_process(tongyici_file):
    
    with open(tongyici_file,'r') as tycr:
        for line in tycr.readlines():
            line = line.strip()
            if "=>" not in line:
                word_list = word_split_normal(line)
            else:
                word_list = word_split_restrict(line)

tongyici_file = "./../data/mysynonym_180927.txt"
word_format_process(tongyici_file)


