#得到file1和file2的交集数据。前提是两列数据都是以\t分割而且是比较两个文件第一列的交集。原理就是通过NR==FNR来确定数据的是读第一个文件，还是第二个文件
#当读第一个文件时将将其第一列的数据读入到字典中，读第二列的时候判断其数据是不是在第一列
awk -F "\t" 'NR==FNR{a[$1]=0;next} {if($1 in a){print $1}}' file1 file2

#得到第二个数据中 不在第一个文件中的数据
awk -F "\t" 'NR==FNR{a[$1]=0;next} {if(!($1 in a)){print $1}}' file1 file2

#将两个文件按照行相同的方式合并在一起
awk 'NR==FNR{a[i]=$0;i++}NR>FNR{print a[j]" "$0;j++}' file1 file2
