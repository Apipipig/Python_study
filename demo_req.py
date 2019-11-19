def demo1():
    # 检查对象属性
    import requests
    res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
    print(type(res))


def demo2():
    # 检查错误
    import requests
    res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))
def demo3():
    # web页面写入文件
    import requests
    res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
    res.raise_for_status()
    playFile = open('RomeoAndJuliet.txt', 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)

    playFile.close()

demo3()