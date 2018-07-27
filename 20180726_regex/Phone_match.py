#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author = "Andy"
# Date: 2018/7/26

import re

'''
?匹配零次或一次前面的分组。
*匹配零次或多次前面的分组。
+匹配一次或多次前面的分组。
{n}匹配 n 次前面的分组。
{n,}匹配 n 次或更多前面的分组。
{,m}匹配零次到 m 次前面的分组。
{n,m}匹配至少 n 次、至多 m 次前面的分组。
{n,m}?或*?或+?对前面的分组进行非贪心匹配。
^spam 意味着字符串必须以 spam 开始。
spam$意味着字符串必须以 spam 结束。
.匹配所有字符，换行符除外。
\d、\w 和\s 分别匹配数字、单词和空格。
\D、\W 和\S 分别匹配出数字、单词和空格外的所有字符。
[abc]匹配方括号内的任意字符（诸如 a、b 或 c）。
[^abc]匹配不在方括号内的任意字符。
'''

#匹配电话号自实现方法
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('-------------------------------------')

"""
正则表达式匹配
1．用 import re 导入正则表达式模块。
2．用 re.compile()函数创建一个 Regex 对象（记得使用原始字符串）。
3．向 Regex 对象的 search()方法传入想查找的字符串。它返回一个 Match 对象。
4．调用 Match 对象的 group()方法，返回实际匹配文本的字符串。
"""
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
for i in range(len(message)):
    chunk = message[i:i+12]
    # print(chunk)
    if phoneNumRegex.search(chunk):
        print(phoneNumRegex.search(chunk))
        mo = phoneNumRegex.search(chunk)
        print('Phone number found: ' + mo.group())

print('-----------------------')
'''
利用括号分组  
正则表达式字符串中的第一对括号是第1组。第二对括号是第2组。向 group()匹配对象方法传入整数1或2，就可以取得匹配文本的不同部分。
向group()方法传入0或不传入参数，将返回整个匹配的文本

用管道匹配多个分   |
如果 Batman 和 Tina Fey 都出现在被查找的字符串中，第一次出现的匹配文本，将作为 Match 对象返回
'''
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo2 = batRegex.search('Batmobile lost a wheel')
print(mo2.group())

print('-----------------------')
'''
用问号实现可选匹配
字符?表明它前面的分组在这个模式中是可选的
'''
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())#Batman

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())#'415-555-4242'
mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())#'555-4242'

'''
*   用星号匹配零次或多次(匹配星号之前的字符)
+   用加号匹配一次或多次
｛｝用花括号匹配特定次数
贪心(默认)和非贪心(?)匹配
'''
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()#'HaHaHaHaHa'
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()#'HaHaHa'

print('--------------------------------')
'''
findall()方法
findall()方法将返回一组字符串，包含被查找字符串中的所有匹配
1．如果调用在一个没有分组的正则表达式上，例如\d\d\d-\d\d\d-\d\d\d\d，方法findall()将返回一个匹配字符串的列表，
例如['415-555-9999', '212-555-0000']。
2．如果调用在一个有分组的正则表达式上，例如(\d\d\d)-(\d\d\d)-(\d\d\d\d)，方法 findall()将返回一个字符串的元组的列表
（每个分组对应一个字符串），例如[('415','555', '1122'), ('212', '555', '0000')]。
'''
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
pf1 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')#['415-555-9999', '212-555-0000']
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has no groups
pf2 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(pf1)
print(pf2)


'''
\d   0 到 9 的任何数字
\D   除 0 到 9 的数字以外的任何字符
\w   任何字母、数字或下划线字符（可以认为是匹配“单词”字符）
\W   除字母、数字和下划线以外的任何字符
\s   空格、制表符或换行符（可以认为是匹配“空白”字符）
\S   除空格、制表符和换行符以外的任何字符
'''


print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
'''
建立自己的字符分类
在字符分类的左方括号后加上一个插入字符（^），就可以得到“非字符类”。非字符类将匹配不在这个字符类中的所有字符

插入字符和美元字符
在正则表达式的开始处使用插入符号（^），表明匹配必须发生在被查找文本开始处
在正则表达式的末尾加上美元符号（$），表示该字符串必须以这个正则表达式的模式结束
'''
consonantRegex = re.compile(r'[^aeiouAEIOU]')
cf = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(cf)

beginsWithHello = re.compile(r'^Hello')
bs = beginsWithHello.search('Hello world!')
print(bs.group())

endsWithNumber = re.compile(r'\d$')
es = endsWithNumber.search('Your number is 42')
print(es.group())



print('.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*')
'''
用点-星匹配所有字符   .*
'''
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))#'Al'
print(mo.group(2))#'Sweigart'
print(mo.groups())#('Al', 'Sweigart')
print(mo.group())#FirsProtect the innocent.t Name: Al Last Name: Sweigart



print('................................................')
'''
用句点字符匹配换行   .
'''
noNewlineRegex = re.compile('.*')
ns = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print('ns:', ns)#Serve the public trust.
newlineRegex = re.compile('.*', re.DOTALL)
ns1 = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print('ns1:', 'st:'+ns1+':en')#'Serve the public trust.\nProtect the innocent.\nUphold the law.'

'''
不区分大小写的匹配,向 re.compile()传入 re.IGNORECASE 或 re.I，作为第二个参数
'''
robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()

robocop.search('ROBOCOP protects the innocent.').group()

robocop.search('Al, why does your programming book talk about robocop so much?').group()


print('----------------sub---------------')
'''
用 sub()方法替换字符串
Regex对象的 sub()方法需要传入两个参数。第一个参数是一个字符串，用于取代发现的匹配。第二个参数是一个字符串，即正则表达式
'''
namesRegex = re.compile(r'Agent \w+')
ns = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(ns)


agentNamesRegex = re.compile(r'Agent (\w)(\w)\w*')
anrs = agentNamesRegex.sub(r'\2****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(anrs)                                 #A**** told       C**** that       E**** knew     B**** was a double agent.