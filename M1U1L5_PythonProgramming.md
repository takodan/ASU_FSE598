## 學習新語言的步驟 02:32
1. 基本輸入輸出
2. 創建變數
3. if判斷式
4. 迴圈
5. function
    1. return, void, parameter
    2. import library
6. 數據結構
7. object oriented
8. XaaS

## Python built-in editor: IDEL 04:53

## other IDE 06:38
1. Visual Studio
2. PyDev for Eclipse (easy for Java Eclipse user)
3. PyCharm
4. VSCode

## Visual Studio start a new Python project
1. file > new > project > python application > (edit code) > debug > start

## Python function 09:43
1. you can start coding without function
2. Python function doesn't use {}, it use indention.
```py
def main()
    i = 5
    j = 10 
    print("i =", i, ",j =", j)

if __name__ == "__main__":
    main()

print("this can still print")
``` 

## if and loop 17:13
1. if, else, else if
2. while, Foreach(for...in)

## read file 22:22
```py
data = []
with open ("myText.txt") as f:
    data = f.readlines()
    print(data)
f.close
```