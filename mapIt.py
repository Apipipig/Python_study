"""
    内容：将一条街道的地址拷贝到剪贴板上，并在 Google 地图上打开它的地图

"""

import webbrowser, sys,pyperclip
if len(sys.argv) > 1:
    # 从命令行获取地址
    address = ' '.join(sys.argv[1:])
else:
    # 从剪贴板获取地址
    address = pyperclip.paste()

print(address)


webbrowser.open('https://www.google.com/maps/place/' + address)


# import pyperclip
#
# pyperclip.copy('test')
# a = pyperclip.paste()
# print(a)