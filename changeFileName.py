# -*- coding: utf-8 -*-
import os
import sys
from PIL import Image 

listfile = os.listdir(os.getcwd())
fromStr = raw_input("查找文件名关键字: ")
toStr = raw_input("替换为：")
fromStrLen = len(fromStr)
toStrLen = len(toStr)
changedCount = 0
for line in listfile:

    sPos = line.find(fromStr)
    if(sPos >= 0):
        des = line[0:sPos] + toStr + line[sPos + fromStrLen:]
        if line[-4:]=='.txt':
            inputFile = open(line)
            text = inputFile.read()
            inputFile.close()
            output = open(des,'w')
            output.write(text)
            output.close()
            changedCount +=1
            os.remove(line)
        elif(line[-4:]=='.png'):
            try:
                img = Image.open(line)
                img.save(des)
                changedCount +=1
                os.remove(line)
            except:
                print(line + "文件损坏")
print(str(changedCount) + "个文件已经重命名成功！")
os.system('pause')
