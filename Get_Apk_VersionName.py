# -*- coding:utf-8 -*-
import subprocess
import re
import os

# 切换工作路径
working_director = "C:\\Users\\zhengdongqi\\AppData\\Local\\Android\\sdk\\build-tools\\24.0.1"
os.chdir(working_director)
# print(os.getcwd())

# Apk_Path = APK路径
Apk_Path = input("请输入要查询版本号的apk的路径：")

# 查看AndoridManifest.xml中的配置信息
COMMOND2 = "aapt d badging "
# COMMOND3 = " AndroidManifest.xml"
commond = COMMOND2 + Apk_Path
# print(commond)


def get_apk_name(cmd1):
    file = []
    p = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    file = str(p.communicate()).split()
    p.kill()
    print("该apk的版本号是：")
    for f in file:
        versionname = re.match(r"versionName='(.*)'.*", f, re.M | re.I)
        if versionname:
                print(versionname.group(1))
                break

if __name__ == '__main__':
    get_apk_name(commond)
