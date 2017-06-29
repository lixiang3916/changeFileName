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

    if line[0:fromStrLen]== fromStr:
        if line[-4:]=='.txt':
            inputFile = open(line)
            text = inputFile.read()
            inputFile.close()
            output = open(toStr+ line[fromStrLen:],'w')
            output.write(text)
            output.close()
            changedCount +=1
            os.remove(line)
        elif(line[-4:]=='.png'):
            try:
                img = Image.open(line)
                img.save(toStr + line[fromStrLen:])
                changedCount +=1
                os.remove(line)
            except:
                print(line + "文件损坏")
print(str(changedCount) + " 个文件已经重命名成功！")
os.system('pause')