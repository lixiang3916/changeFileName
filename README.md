# changeFileName
用途：
将文件夹中的文件批量重命名。

输入匹配的关键字和目标关键字

将文件夹中的每个文件的第一个匹配到的关键字替换成输入的目标关键字

使用过程：
第一种直接运行脚本文件
-----------------------------
>python changeFileName.py

查找文件名关键字: 2_

替换为：3_  

2 个文件已经重命名成功！

请按任意键继续. . .

--------------------------
结果：
将2_150_0_1.txt和2_150_0.png文件替换为3_150_0_1.txt和3_150_0.png

第二种使用方法
>python build py2exe

将脚本程序打包成exe，在别的没有Python环境的电脑上使用
