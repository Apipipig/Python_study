"""
    内容：正则表达式小练习
    日期：2019／08／17
"""
import re
def demo1():
    phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    mo = phoneNumRegex.search('My phone number is 415-555-4242.')
    # group分组 0完全匹配、1第一个括号内分组匹配、2～
    print('Phone number found:' + mo.group(0))
    areCode,mainNumber = mo.groups()
    print('areCode is:' + areCode)
    print('mainNumber is:' + mainNumber)

def demo2():
    # 管道字符匹配多个分组
    heroRege = re.compile (r'Bat(man|mobile|copter|bat)')
    mo = heroRege.search('Batmobile is lost')
    print('Find result:'+ mo.group(1))

def demo3():
    # 问号实现可选匹配
    batRegex = re.compile(r'Bat(wo)?man')
    mo1 = batRegex.search('The Adventures of Batman')
    print('Find mo1 is:' + mo1.group())
    mo2 = batRegex.search('The Adventures of Batwoman')
    print('Find mo2 is:' + mo2.group())
    # 星号匹配零次或多次
    batRegex3 = re.compile(r'Bat(wo)*man')
    mo3 = batRegex3.search('The Acventures of Batwowowoman')
    print('Find mo3 is:' + mo3.group())
    # 加好匹配1次或多次
    batRegex4 = re.compile(r'Bat(wo)+man')
    mo4 = batRegex4.search('The Adventures of Batwowowowowowoman')
    print('Find mo4 is:' + mo4.group())
    mo5 = batRegex4.search('The Adventures of Batman')
    if mo5 == None:
        print('True')

def demo4():
    # 用花括号匹配特定次数
    haRegex = re.compile(r'(Ha){3}')
    mo1 = haRegex.search('HaHaHa')
    print('Find mo1 is:' + mo1.group())
    mo2 = haRegex.search('Ha')
    if mo2 == None:
        print('No mo2 here~')

def demo5():
    # 贪心匹配，二义情况下尽可能匹配最长字符
    greedyHaRegex = re.compile(r'(Ha){3,5}')
    mo1 = greedyHaRegex.search('HaHaHaHaHa')
    print('Find mo1 is:' + mo1.group())
    # 非贪心匹配，二义情况下尽可能匹配最短字符
    greedyHaRegex2 = re.compile(r'(Ha){3,5}?')
    mo2 = greedyHaRegex2.search('HaHaHaHaHa')
    print('Find mo2 is:' + mo2.group())

def demo6():
    # search 返回的Match对象只包含只返回第一次出现的匹配文本
    phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo1 = phoneRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
    print('Find mo1 is:' + mo1.group())
    # findall
    phoneRegex2 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no group 返回一个字符串列表
    mo2 = phoneRegex2.findall('Cell: 415-555-9999 Work: 212-555-0000')
    print('Find mo2 is:' + str(mo2))
    phoneRegex3 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has group 返回一个字符串的元组的列表
    mo3 = phoneRegex3.findall('Cell: 415-555-9999 Work: 212-555-0000')
    print('Find mo3 is:' + str(mo3))

def demo7():
    xmasRegex = re.compile(r'\d+\s\w+')
    mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maidse')
    print('Find mo is:'+ str(mo))

def demo8():
    # 自定义字符分类
    # 字符分类[aeiouAEIOU]将匹配所有元音字符
    vowelRegex = re.compile(r'[aeiouAEIOU]')
    mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
    print('Find mo is:' + str(mo))
    #非字符类，将匹配不在这个字符类中的所有字符
    vowelRegex2 = re.compile(r'[^aeiouAEIOU]')
    mo2 = vowelRegex2.findall('RoboCop eats baby food. BABY FOOD.')
    print('Find mo2 is:' + str(mo2))

def demo9():
    # 点星匹配所有字符
    nameRegex = re.compile(r'First name:(.*) Last name:(.*)')
    mo = nameRegex.search('First name:Al Last name: Sweigart')
    print(mo.group(1))
    print(mo.group(2))
    # 非贪心模式
    nongreedyRegex = re.compile(r'<.*?>') #“匹配一个左尖括号，接下来是任意字符，接下来是一个右尖括号”
    mo2 = nongreedyRegex.search('<To sreve man> for dinner.>')
    print('Find mo2 is:' + mo2.group())
    # 贪心模式
    greedyRegex = re.compile(r'<.*>')
    mo3 = greedyRegex.search('<To sreve man> for dinner.>')
    print('Find mo3 is:' + mo3.group())

def demo10():
    noNewlineRegex = re.compile('.*')
    mo = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
    print('Find mo is:' + mo.group())
    # 用句点字符匹配换行符
    noNewlineRegex2 = re.compile('.*',re.DOTALL)
    mo1 = noNewlineRegex2.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
    print('Find mo1 is:' + mo1.group())

def demo11():
    # 不区分大小写，可以向 re.compile()传入 re.IGNORECASE 或 re.I，作为第二个参数
    robocop = re.compile(r'robocop', re.I)
    mo = robocop.search('RoBoCop is part man, part machine, all cop.').group()
    print(mo)

def demo12():
    # sub()方法返回替换完成后的字符串
    namesRegex = re.compile(r'Agent \w+')
    mo = namesRegex.sub('CENSORED', 'Agent Alice gave the secret document to Agent Bob.')
    print(mo)
    # 使用正则表达式 Agent (\w)\w*，传入 r'\1****'作为 sub()的第一个参数,将只显示姓名首字母
    agentNameRegex = re.compile('Agent (\w)\w*')
    mo2 = agentNameRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent')
    print(mo2)

# def demo13():
    # 【项目】：电话号码和 E-mail 地址提取程序
    # 电话号码的正则表达式
    phoneRegex = re.findall(r'\(?0\d{2,3}[)-]?\d{7,8}',text)#\(?  [?表示括号可有可无,\(表示匹配(]
                                                    #0\d{2,3} 表示区号。
                                                    #[) -]?  表示区号后面可以跟")"," ","-"，也可能什么都没有
                                                    #\d{7,8} 表示7位或8位的号码
    # E-mail地址的正则表达式
    mailRegex = re.findall(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',text)

    # pyperclip.paste()函数取得剪贴板的文本
    # re模块匹配文本中所有的电话号码和E-mail地址
# import pyperclip, re
#     text = str(pyperclip.paste())
#     matches = []
#     for groups in phoneRegex.findall(text):
#         phoneNum = '-'.join(([groups[1], groups[3], groups[5]])

    # 将它们粘贴到剪贴板。
    # 现在你可以开始思考，如何用代码来完成工作。代码需要做下面的事情：
    # 使用 pyperclip 模块复制和粘贴字符串。
    # 创建两个正则表达式，一个匹配电话号码，另一个匹配 E-mail 地址。
    # 对两个正则表达式，找到所有的匹配，而不只是第一次匹配。
    # 将匹配的字符串整理好格式，放在一个字符串中，用于粘贴。
    # 如果文本中没有找到匹配，显示某种消息。



demo12()