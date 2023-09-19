## 遞迴式的迭代分解 04:43
```py
Foo(n):
    if(n = 0):
        print i
        return
    else:
        Foo(n-1)
```
T(n) = 1 + T(n-1) 遞迴第一次
     = 1 + 1 + T(n-2) 遞迴第二次
     ...
     = n + 2 遞迴n次後進入條件式

T(n) = n + 2 = O(n)

## 遞迴式加上循環 08:51
```py
Foo(n):
    if(n = 0):
        print i
        return
    else:
        for( i in range(n))
            sum = sum + 1
            print(sum)
        Foo(n-1)
```
T(n) = O(n^2)

## 遞迴式加遞迴式 11:11
T(n) = O(2^n)
