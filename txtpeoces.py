# -*- coding: utf-8 -*-
# @Time    : 2021/3/31 19:19
# @Author  : Deng Qidong
# @FileName: txtpeoces.py
# @Software: PyCharm

#第一步 去除文本空行，保存于"GENIA_rm_blank.txt"文件,可知处理后文件有6000行，即2000篇文献
def blank_remove():
    with open("GENIA.txt") as lines:
        file=open("GENIA_rm_blank.txt","w+")
        for line in lines:
            if line.strip()!='':
                file.write(line)
    file.close()
    lines.close()
        #读取之后文件行数
    with open("GENIA_rm_blank.txt") as lines:#读取新生成的文件
        print(len(lines.readlines()))#输出结果为6000
    lines.close()

#第二步 语料库的文章摘要用列表abstract_lst存储，
# 生成GENIA文献集合文件以便直接用linux命令行处理
def get_abstract_list():
    n=0
    abstract_lst=list()
    with open("GENIA_rm_blank.txt") as lines:
        for line in lines:
            n=n+1
            if n%3==0:#三的倍数行是摘要行
                abstract_lst.append(line)
    file = open("GENIA_abstract.txt", "w+")
    for i in abstract_lst:
        file.write(i)
    file.close()
    return abstract_lst


#blank_remove()
x=get_abstract_list()
