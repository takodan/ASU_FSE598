## Python 容器 00:22
在python中為默認功能, 不需要導入
1. string
2. list
3. dict
4. set
5. tuple

## array vs Python list 01:44
1. 通常說在說Python數組就是指list, 但是Python和大部分語言的數組結構並不同, 數組是靜態的而list是動態的
2. 數組:
    1. 靜態的, 大小固定
    2. 由程序員管理
    3. 在內存中會是連續的, 效率較高
3. 列表:
    1. 動態的, 自動變大
    2. 由系統管理, 程序員不能直接控制大小
    3. 可能會需要額外資源, 效率較低
    4. Python的list運作類似於C++的LinkedList, 當數據增加會使用pointer指向下一段數據
4. 在Java中的Array是數組, ArrayList是列表
5. Python 實際上也是可以使用數組

## 創建 list 07:54
```py
myList = []
myList = [1,"2", 3]
myList = list() # same as []
myList = list(<iterable>) # convert another iterable to list
```

## 一些list 例子和方法09:18
列表也是對向
```py
myList[0]
myList[<star>:<finish>]
myList.append(value)
myList + myList
myList.extend(<iterable>)
myList.count(value)
myList.remove(value)
myList.pop(index) # if no index provided, pop last one
myList.revere() # no return the list
myList.sort() # can provided a function for sorting
myList.clear()
```

## 可以利用append和pop模擬stack 14:06

## Python 字典例子 dictionary 18:20
Key必須是string, Value可以是任何類型
```py
myDict = dict()
myDict = {"num1": 1, "num2": 2, "num3": 3}
myDict["num4"] # an error
myDict.get["num4"] # not cause an error, return None
```

## Python 集合 set 26:29
和list類似, 但set中沒有順序, 沒有index, 而且不會重複
```py
mySet1 = {1, 2, 3, 4, 5} 
mySet2 = {5, 4, 3, 2, 1} # same as mySet1
mySet3 = {1, 2, 3, 4, 5, 3, 3} # same as mySet2 mySet2
```

## Python 元祖 tuple 29:22
和list類似, 一樣使用`[index]`讀取數據, 但是tuple不可變的
```py
myTuple = (1, 2, 3)
```

## why tuple 33:59
1. tuple是不可變的, 靜態的, 效率較高
2. 多用於表示紀錄
3. 或作為function 的 return value



