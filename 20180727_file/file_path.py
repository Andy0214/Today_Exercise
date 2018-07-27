#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author = "Andy"
# Date: 2018/7/27



import os


'''
os.path.join()就会返回一个文件路径的字符串，包含正确的路径分隔符
'''

str = os.path.join('usr', 'bin', 'spam')
print(str)#usr\bin\spam


myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))

'''
当前工作目录
利用 os.getcwd()函数，可以取得当前工作路径的字符串，并可以利用 os.chdir()改变它
'''
print(os.getcwd())
# os.chdir('C:\\Windows\\System32')
print(os.getcwd())


print('...............................')
'''
处理绝对路径和相对路径
• 调用 os.path.abspath(path)将返回参数的绝对路径的字符串。这是将相对路径转换为绝对路径的简便方法。
• 调用 os.path.isabs(path)，如果参数是一个绝对路径，就返回 True，如果参数是一个相对路径，就返回 False。
• 调用 os.path.relpath(path, start)将返回从 start 路径到 path 的相对路径的字符串。如果没有提供 start，就使用当前工作目录作为开始路径
• 调用 os.path.dirname(path)将返回一个字符串，它包含 path 参数中最后一个斜杠之前的所有内容。
• 调用 os.path.basename(path)将返回一个字符串，它包含 path 参数中最后一个斜杠之后的所有内容
• os.path.split(),返回一个路径的目录名称和基本名称
'''
print(os.path.abspath('.'))#C:\Users\yaoqian\PycharmProjects\Today_Exercise\20180727_file
print(os.path.abspath('..\\20180726_regex'))#C:\Users\yaoqian\PycharmProjects\Today_Exercise\20180726_regex

print(os.path.isabs('.'))#False
print(os.path.isabs(os.path.abspath('.')))#True
print(os.path.relpath('C:\\Windows', 'C:\\'))#Windows
print(os.path.relpath('C:\\Windows', 'C:\\Intel\\gp'))#..\..\Windows

print(os.getcwd())#C:\Users\yaoqian\PycharmProjects\Today_Exercise\20180727_file

path = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(path))#calc.exe
print(os.path.dirname(path))#C:\Windows\System32
print(os.path.split(path))#('C:\\Windows\\System32', 'calc.exe')
print((os.path.dirname(path), os.path.basename(path)))#('C:\\Windows\\System32', 'calc.exe')
print(path.split(os.path.sep))

print('----------------------------------')
'''
查看文件大小和文件夹内容
• 调用 os.path.getsize(path)将返回 path 参数中文件的字节数。
• 调用 os.listdir(path)将返回文件名字符串的列表，包含 path 参数中的每个文件
'''
print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))
print(os.path.getsize('C:\\Windows\\System32'))#包含文件夹，大小可能有误差
# print(os.listdir('C:\\Windows\\System32'))

totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalSize)

print('*******************************************')
'''
检查路径有效性
• 如果 path 参数所指的文件或文件夹存在，调用 os.path.exists(path)将返回 True，否则返回 False。
                                                 可以确定 DVD 或闪存盘当前是否连在计算机上
• 如果 path 参数存在，并且是一个文件，调用 os.path.isfile(path)将返回 True，否则返回 False。
• 如果 path 参数存在，并且是一个文件夹，调用 os.path.isdir(path)将返回 True，否则返回 False。
'''
print(os.path.exists('C:\\Windows'))
print(os.path.exists('C:\\some_made_up_folder'))
print(os.path.isdir('C:\\Windows\\System32'))
print(os.path.isfile('C:\\Windows\\System32'))
print(os.path.isdir('C:\\Windows\\System32\\calc.exe'))
print(os.path.isfile('C:\\Windows\\System32\\calc.exe'))
print(os.path.exists('G:\\'))

print('--------------------rw--------------------')
'''
文件读写过程,三个步骤：
1．调用 open()函数，返回一个 File 对象。
2．调用 File 对象的 read()或 write()方法。
3．调用 File 对象的 close()方法，关闭该文件。
'''
# helloFile = open('C:\\WiFi_Log.txt')
# helloContent = helloFile.read()
# hellolines = helloFile.readlines()
# print(helloContent)
# print(hellolines)
