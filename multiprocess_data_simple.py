#!/usr/bin/env python
#coding:utf-8
####################
# 本脚本的作用是使用异步的方法来对数据进行敏感词过滤。由于敏感词表的数据约有5w条且敏感词数据中含有"A&&B%%C"这种数据，表示的是去过query中同时还有A，B，C时才认为该query是敏感词。
####################

import sys
import time
sys.path.append("..")
import multiprocessing.pool as mtpool

#如果返回Fasle表示keyword是敏感词；返回True表示keyword不是敏感词
# 对于含有"&&"数据的进行处理
def judge_sensi(bl,keyword):
    flag_t = False
    bl_list = bl.split("&&")
    #print(len(bl_list))
    for bl_c in bl_list:
        if(bl_c not in keyword):
            flag_t = True
            break
    return flag_t

#过滤敏感词，如果是敏感词就返回false，否则返回true
def sentive_word_filt_u(sentive_list,word):
    for bl in sentive_list:
        if bl in word:
            return False
        elif "&&" in bl:
            flag_tmp = judge_sensi(bl,word)
            if flag_tmp == True:
                continue
            else:
                return False
    return True

# 对query_list文件进行过滤
def wordlist_filter(sensitive_list,query_list):
    query_list_part = list()
    print(query_list[:10])
    for query in query_list:
        if sentive_word_filt_u(sensitive_list,query) != False:
            query_list_part.append(query)
        else:
            print("sensitive word is ",query)
    return query_list_part

# 将结果写出
def output(output_file,search_list):
    with open(output_file,'w') as ofw:
        for num in search_list:
            ofw.write(num+"\n")


def usersearch_filter_uniq(usersearch_file):
    uniq_set = set()
    searchfile_list = list()

    # 读取敏感词表的数据
    sencetive_name = "./../sensitive_black_word.txt"
    sentive_list = list()
    with open(sencetive_name, "r") as rdf:
        for line in rdf.readlines():
            line = line.strip()
            sentive_list.append(line)
    print("The sensitive word length is:",len(sentive_list))

    with open(usersearch_file,'r',encoding='utf-8') as usfr:
        searchfile_list_tmp = list()
        # 对词进行去标点、长度过滤、和去重
        for lines in usfr.readlines():

            line_list = lines.strip().split(",")
            # print(line_list)
            if len(line_list) != 2:
                continue
            # print(len(line_list))
            keyword = line_list[0]
            drop_str = remove_nonch(keyword)
            if len(drop_str) > 15:
                continue
            if drop_str in uniq_set:
                continue
            uniq_set.add(drop_str)
            searchfile_list_tmp.append(drop_str)

    print("searchfile_list_tmp length is ",len(searchfile_list_tmp))

    # 多线程的对数据进行敏感词过滤
    t = 4
    searchfile_length = len(searchfile_list_tmp)
    searchfile_part = list()
    # 先将数据分词4份
    for i in range(4):
        searchfile_part.append(searchfile_list_tmp[round(searchfile_length*i/4):round(searchfile_length*(i+1)/4)])

    print(len(searchfile_part))
    # 开启进程
    async_list = list()
    pool = mtpool.Pool(t)
    # 异步将数据分片，然后执行每片数据
    for part in range(len(searchfile_part)):
        res = pool.apply_async(func=wordlist_filter,args=(sentive_list,searchfile_part[part],))
        async_list.append(res)

    print("async_list length is ",len(async_list))

    # 获取每一片数据的执行结果
    for async_data in async_list:
        for keyword in async_data.get():
            # print(type(keyword_list))
            # print((keyword_list))
            searchfile_list.append(keyword)
        # print(len(async_data))
    # print(type(async_list))
    print("The searchfile_list length is ",len(searchfile_list))

    # 将结果写出
    output_filename = "result_usersearchfile.txt"
    output(output_filename,searchfile_list)


filename = "./../usersearch.csv"
begin_time = time.time()
usersearch_filter_uniq(filename)
end_time = time.time()
cost_time = end_time-begin_time
print("The cost time is :",cost_time)
