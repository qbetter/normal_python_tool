#!/bin/bash

#目的：将synonym_dict.mt文件从“utf-8”转换成“gb18030”，由于文件中的某行数据不规范，在用iconv转换的过程中会使得转换失败，因此需要去除不规范的那一行。
#处理过程是逐行遍历转换成数据，转换之后用file和grep查看数据是不是正确的格式，如果不是说明此行有误，就去掉改行；若每错就继续遍历。
#

#file_length=`wc -l synonym_dict.mt | cut -d" " -f1`

#echo "file length is "$file_length


function get_real_symdata(){

    file_length=`wc -l $table_name | cut -d" " -f1`

    echo "file length is "$file_length

    for ((line=1; line<$file_length; line++))
    do
        echo $line
        head -$line  $table_name | iconv -f'utf8' -t'gb18030' > ttttt
        zhuangtai=`file ttttt | grep Non`
        zt_len=${#zhuangtai}
        if [ $zt_len -gt 0 ]
        then
            echo "drop this line"
            sed -i $line'd' $table_name
            line=$[$line-1]
        else
            echo "continue"
        fi        

    done
}

#table_name="synonym_dict.mt"
table_name="strip_synonym_dict_tail.mt"
get_real_symdata

