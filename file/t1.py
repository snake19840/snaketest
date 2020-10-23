#!/usr/bin/env python3
# -*- coding:utf8 -*-
# @TIME  :2018/9/17 9:02
# @Author:dazhan
# @File  :copyfiles2dir.py

import os
import shutil

def creatPath(save_dir,dd):
    # save_dir=r'\upload' #文件路径
    # dd=r'D:\桌面\test'    #文件保存主路径
    dir=save_dir.split('\\')
    # 想保存到的根路径
    # 如果目录不存在，则创建
    for d in dir:
        # print(d)
        dd+=d+"\\"
        if not os.path.isdir(dd):
            os.makedirs(dd)

if __name__ == '__main__':

    pageNmae=os.path.split(__file__)[-1].split(".")[0]
    loclPath=os.getcwd()


    source_path = os.path.dirname(os.path.dirname(loclPath))+"\\upload"

    target_path = os.path.abspath(r'D:\upload')

    if not os.path.exists(target_path):
        os.makedirs(target_path)

    if os.path.exists(source_path):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
        for root, dirs, files in os.walk(source_path):
            for file in files:
                r=root[len(source_path):]
                creatPath(r,target_path)
                # print(root)
                # print(file)
                # print(r)
                src_file = os.path.join(root, file)
                shutil.copy(src_file, target_path+r)
                print(src_file)

    print('copy files finished!')
