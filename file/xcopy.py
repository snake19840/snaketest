import shutil
import os
i = 0
k = 0
def creatPath(save_dir,dd):
    dir=save_dir.split('\\')

    # 想保存到的根路径

    # 如果目录不存在，则创建

    for d in dir:
        print(d)
        dd+=d+"\\"
        if not os.path.isdir(dd):
            os.makedirs(dd)


if __name__ == '__main__':
    save_dir=r'D:\桌面\APP\upload' #文件路径
    dd=r'D:\桌面\test'    #文件保存主路径
    creatPath(save_dir,dd)
