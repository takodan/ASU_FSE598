## Python 函數 01:15
1. 目的:
    1. 抽象化: 將部分程式碼構成一個模快/單元
    2. 重用: 可以在程序中多次使用
2. 數據傳遞:
    1. 通過全域/靜態變量
    2. 函數參數, 返回值
3. 在定義函數時: 參數稱作形式參數, 調用時稱作實際參數

## 範例
```py
def myFunction(num):
    pass

def main():
    returnValue = myFunction([1, 2, 3])

main()
```
1. Python不定義參數類型也可以定義參數

## 參數傳遞 07:30
1. 值傳遞: 值複製到函數中成為區域變量, 優點是無副作用, 缺點是使用上可能較不靈活, 效率較差
2. 指針(引用)傳遞: 實際上只是指針, 指向實際參數
3. 全域/靜態便量: 沒有參數傳遞直接調用
4. java和python: 都是類似使用指針

## python 參數 12:50
1. python中還是可註記參數類型, 但不會檢查(不同類型不會引發錯誤)
2. 要檢查類型需另外使用 assert 來引發錯誤
```py
def myFunction(num:list):
    pass

def myFunction2(num):
    assert isinstance(num, list)
```

## assert 18:41
1. 會讓程式強制出錯, 會停止程式, 給出 AssertionError
2. 只用在開發階段, 不用在生產階段
```
assert <condition>
assert <condition>, <error message>
```
## 硬件異常 19:34
1. 內部異常: 由CPU內部發出, 多為計算上的錯誤, 也稱為程式異常, 例如除以零
2. 外部異常: 由CPU以外其他組件發出, 例如內存不足, 訪問衝突

## 異常處理 23:00
1. 異常的層面
    1. 硬件
    2. 操作系統
    3. 程式語言
    4. 用戶
2. 如果異常沒有在上一層捕獲, 通常會出現在下一層

## 在python引發異常 27:11
1. assert
2. raise: 引發的異常部會停止程序, 只會有訊息
```py
raise TypeError("costume error message")
```
3. 其他方式後面會講

## 更多python參數 30:28
1. overloading
    1. 定義函數名一樣, 但是參數不一樣
    2. 用來輸入不同類型的參數
2. python 不須使用overloading, 因為python類型本來就是動態的
3. python 還可以設定默認參數, 關鍵詞參數
    1. 需接續在一般參數後
    2. 沒有給參數值就會是默認值
    3. 在給參數時可以給予關鍵詞, 改變給予參數的順序
```py
def myFunction(first, second, third = 0, fourth = 0):
    pass
myFunction(1, 2, fourth = 4) # no third parameter
```

4. 未知,任意參數
    1. 在定義參數前加`*`便可以在呼叫時以tuple傳入參數
    2. 放在參數後, 默認參數前
    3. 其實就和輸入list類似
```py
def myFunction(first, *numbers, final = 0):
    pass
myFunction(1, (2, 3, 4))
```

## 重溫print
1. `print(*object, sep = '', end = '\n', file = sys.stdout, flush = False)`
    1. sep: 分隔符
    2. end: 結尾, 預設為`\n`換行
    3. 改變輸出目標, 必須有write(string)方法
    4. 指定輸出方式是flush刷新或是緩衝