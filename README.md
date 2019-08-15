# Python_study
demo

# 1、输出字典内的物品总数
# stuff = {'rope':1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#
# def displayInventory(inventory):
#     print('Inventory: ')
#     stuffCount = 0
#     for k,v in stuff.items():
#         print(str(v) + ' ' + k)
#         stuffCount += v
#     print('Total umber of items :' + str(stuffCount))
#
#
# displayInventory(stuff)

# 2、列表到字典

addedItems = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = {'gold coin':42,'rope':1}

def addToInventory(inventory, addedItems):
    set01 =set(addedItems)
    print(set01)
    dict01={}
    for item in set01 :
        dict01.update({item:addedItems.count(item)})
    print(dict01)
    for k,v in inventory.items():
        if k in dict01:
            dict01[k] += v
        else:
            dict01[k] = v
    # 按照键值排序
    dict02 = dict(sorted(dict01.items(), key=lambda d: d[1]))
    print(dict02)
    print('-----------------------')
    print('Inventory: ')
    stuffCount = 0
    for k,v in dict02.items():
        print(str(v) + ' ' + k)
        stuffCount += v
    print('Total umber of items :' + str(stuffCount))



if __name__ == '__main__':
     addToInventory(inventory, addedItems)
