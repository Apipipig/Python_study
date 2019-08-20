"""
    日期：2019／05／05
    功能：python基础
"""

# 始终记录变量值最新值
# message = 'hello python world!'
# print(message)
#
# message = 'hello and byebye~'
# print(message)

# 使用方法修改字符串的大小写
# name = 'ada lovelace'
# print(name.title())
# print(name.upper())
# print(name.lower())

# This program says hello and ask for my name.

def demo1():
    print ('Hello world!')
    print ('What is your name?') # ask for their name
    myName = input()
    print('It is good to see you,' + myName)
    print ('The length of your name is:')
    print (len(myName))
    print('What is your age?')# ask for their age
    myAge = input()
    print('You will be'  + str(int(myAge) + 1) +  'in a year.')

def demo2():
    # While循环
    name = ''
    while name != 'your name':
        print('Please Type Your Name.')
        name = input()
    print('Thank you~')

def demo3():
    # Break语句，跳出死循环
    while True:
        print('Please type your name.')
        name1 = input()
        if name1 == 'your name':
            break
    print ('Thank you~')

def demo4():
    # continue内部循环,返回true时跳回循环开始处，返回false则继续执行后面的语句
    while True:
        print('Who are you?')
        name2 = input()
        if name2 != 'cat':
            continue
        print('Hello cat,what is the password?')
        password = input()
        if password == '123456':
            break
        print('I Love Cat~')

def demo5():
    # for循环和range()函数,循环固定次数
    total = 0
    for num in range(101):
        total = total + num
    print(total)
def demo6():
    # 从 0 数到 8，间隔为 2
    for i in range(0, 10, 2):
        print(i)

def demo7():
    # random.randint()函数调用求值为传递给它的两个整数之间的一个随机整数
    import random
    for i in range(5):
        print(random.randint(1,10))

def demo8():
    # 用sys.exit()退出程序
    import sys

    while True:
        print('Type exit to exit!')
        response = input()
        if response == 'exit':
            sys.exit()
    print('You typed' + response + '.')

def demo9():
    # 返回值和return语句
    import random

    def getAnswer(answerNumber):
        if answerNumber == 1:
            return 'It is certain'
        elif answerNumber == 2:
            return 'It is decidedly so'
        elif answerNumber == 3:
            return 'Yes'
        elif answerNumber == 4:
            return 'Reply hazy try again'
        elif answerNumber == 5:
            return 'Ask again later'
        elif answerNumber == 6:
            return 'Concentrate and ask again'
        elif answerNumber == 7:
            return 'My reply is no'
        elif answerNumber == 8:
            return 'Outlook not so good'
        elif answerNumber == 9:
            return 'Very doubtful'
    r = random.randint(1,9)
    fortune = getAnswer(r)
    print(fortune)

def demo9():
    spam = print('Hello!')
    None == spam

def demo10():
    # 用end链接参数传入print自带换行符
    print('Hello',end='')
    print('World!')

def demo11():
    # 用sep替换参数之间默认的空格
    # print('A','B','C')
    print('A','B','C',sep=',')


def demo12():
    # 局部作用域不能使用其他局部作用域内的变量
    def spam():
        eggs = 99
        bacon()
        print(eggs)
    def bacon():
        ham = 1
        eggs = 0
    spam()

def demo13():
    # 全局变量可以在局部作用域中du读取
    def spam():
        print (eggs)
    eggs = 12
    spam()
    print(eggs)

def demo14():
    # global语句定义全局变量 ??教材输出结果是spam
    def spam():
        global eggs
        eggs = 'spam' # this is the global

    def bacon():
        eggs = 'bacon'# this is a local
    def ham():
        print(eggs) # this is the global
    eggs = 42 # this is the global
    spam()
    print(eggs)

def demo15():
    # 只能是全局变量或者是局部变量，当函数被调用时检查到有局部变量赋值语句但局部变量不存在时，不会回退再取全局变量
    def spam():
        #print(eggs)   # ERROR!
        eggs = 'spamlocal'

    eggs = 'global'
    spam()



def demo16():
    # 数除以零时，就会发生 ZeroDivisionError
    def spam(divideBy):
        return 42 / divideBy

    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))


def demo17():
    # 异常处理1
    # 用try和except语句处理错误,如果在 try子句中的代码导致一个错误，程序执行就立即转到 except 子句的代码
    def spam(divideBy):
        try:
            return 42 / divideBy
        except ZeroDivisionError:
            print('Error:Invalid argument.')

    print(spam(2))
    print(spam(12))
    print(spam(0))
    print((spam(1)))

def demo18():
    # 异常处理2
    # 在函数调用中的 try 语句块中，发生的所有错误都会被捕捉，但不会继续执行:
    def spam(divideBy):
        return 42 / divideBy

    try:
        print(spam(2))
        print(spam(12))
        print(spam(0))
        print(spam(1)) #未被执行是因为，一旦执行跳到 except 子句的代码，就不会回到 try 子句。它会继续照常向下执行。
    except ZeroDivisionError:
        print('Error:Invalid argument.')

def demo19():
    # 一个小程序，猜数字
    # This is a guess the number game.
    import random
    secretNumber = random.randint(1,20)
    print('I am thinkingof a number between 1 and 20.')

    # Ask the player to guess the number.
    for guessTaken in range(1,7): #循环6次
        print('Take a guess.')
        guess = int(input())

        if guess < secretNumber :
            print('Your guess is to low.')
        elif guess > secretNumber :
            print('Your guess is to high.')
        else:
            break # 如果该猜测既不大于也不小于秘密数字，那么它就一定等于秘密数字，这时你 希望程序执行跳出 for 循环
    if guess == secretNumber:
        print('Good job!You guess my number in ' + str(guessTaken) + 'guesses!')
    else:
        print('Nope.The nunmber I was thinking of was' + str(secretNumber))



def demo20():
    """# 3.11.1项目练习
    # def collatz():
    #     number = int(input())
    # if number % 2 == 0
    #     print()
    # elif number % 2 == 1
    #
    # else:
"""

  ########################################################################################################
  # 列表

def demo21():
    # 保存猫的名字
    catsname = []
    while True:
        print('Enter the name of the car' + str(len(catsname) + 1) +
        '(Or enter nothing to stop.):')
        name = input()
        if name == '':
            break
        catsname = catsname + [name]
    print('The cats name are:')
    for name in catsname:
        print(' '+ name)


def demo22():
    # in 和 not in 操作符
    myPets = ['Zophie','Pooka','Fat-tail']
    print('Enter a pet name: ')
    name = input()
    if name not in myPets:
        print('I do not have a pet named' + name)
    else:
        print(name + 'is my pet.')


def demo23():
    birthday = {'Alice':'Apr 1','Bob':'Dec 12','Carol':'Mar 14'}

    while True:
        print('Enter a name:(blank to quit)')
        name = input()
        if name == '':
            break
        if name in birthday:
            print(birthday[name] + ' is the birthday of ' + name)
        else:
            print('I do not have birthday information for' + name)
            print('What is their birthday?')
            bday = input()
            birthday[name] = bday
            print('Birthday database update.')

def demo24():
    import pprint
    message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    count = {}

    for charater in message:
        count.setdefault(charater,0)
        count[charater] = count[charater] + 1
    # 适用字典包含嵌྇套的列表或字典
    # pprint.pprint(count)
    # 漂亮打印的文本作为字符串
    print(pprint.pformat(count))

#demo 25 棋盘

theBoard = {'top-L':' ','top-M':' ','top-R':' ',
            'mid-L':' ','mid-M':' ','mid-R':' ',
            'low-L':' ','low-M':' ','low-R':' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('------')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('------')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

#printBoard(theBoard)
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for' + turn + '.Move on which space?')
    move = input()
    theBoard[move]= turn
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'
#printBoard(theBoard)
##############################################################################

stuff = {'rope':1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory: ')
    stuffCount = 0
    for k,v in stuff.items():
        print(str(v) + ' ' + k)
        stuffCount += v
    print('Total umber of items :' + str(stuffCount))


displayInventory(stuff)


# 输出字典信息，居中左右对齐
def printPicnic(itemsDict,leftWidth,rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth , '-'))
    for k,v in itemsDict.items():
        print(k.ljust(leftWidth,'.') + str(v).rjust(rightWidth))
    picnicItems = {'sandwiches':4,'apples':2,'cups':2,'cookies':999}
    printPicnic(picnicItems, 12, 5)
    printPicnic(picnicItems, 20, 6)


if __name__ == '__main__':
    printPicnic(itemsDict, leftWidth, rightWidth)

