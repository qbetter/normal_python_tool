#!/usr/bin/env python
#coding:utf-8
#####################
# 处理data的
#####################
import  sys

# 将数据格式改变成[term,query,1000]的形式，主要是排列组合方法
def get_sysn2format(word_list):
    list_len = len(word_list)
    result_list = list()
    for idx in range(list_len):
        word_idx = word_list[idx]
        # print(word_idx)
        for i in range(list_len):
            if i != idx:
                strm = word_idx + '\t' + word_list[i] + '\t' + "1000"
                result_list.append(strm)
    return result_list

#对list进行切割，使得长度大于1小于6.
def cut_list(word_list):

    result_list = list()
    tmp_list = word_list[:]

    while len(tmp_list) > 1:
        word5 = tmp_list[:5]
        result_list.append(word5)
        # print("word5 is ",word5)
        tmp_list = tmp_list[5:]
        # print("remain li ",tmp_list)
        if len(tmp_list) <2:
            break
    # print("word5 list is ")
    # for i in result_list:
    #     print(i)
    return result_list

def transsys2normal(filename):
    word5_list = list()
    wfile = open("format_sysnon_file.txt", 'w')
    fsf = list()
    with open(filename,'r',encoding='utf-8') as rf:
        for line in rf.readlines():
            line = line.strip()
            line_list = [word for word in line.split(" ") if len(word)>0]
            tmp_list = cut_list(line_list)
            word5_list.extend(tmp_list)

    for line in word5_list:
        print(line)
        format_line = get_sysn2format(line)
        print(format_line)
        fsf.append(format_line)

    for lines in fsf:
        for line in lines:
            #print(line)
            wfile.write(line+"\n")

    wfile.close()
transsys2normal("synonym.txt")

# w_l = ['人','士','人物','人士','人氏','人选','士','人物','人士','人氏','人选']
# cut_list(w_l)

