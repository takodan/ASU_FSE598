## 繼承 00:57
```py
class Pet():
    breed ="Chiuahuah"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"{self.breed}, {self.name}, {self.age}")

class Cat(Pet):
    origin = "American"
    def __init__(self, name, age):
        super().__init__(name, age)
        self.breed = "Persian"

def main():
    alf = Pet("Alf", 5)
    max = Cat("Max", 7)
    alf.info()
    max.info()

main()
```

## 封裝 08:33
私有化變數, class以外無法直接訪問, 但仍可在class內使用method修改
用`_`或`__`

## 多態性 14:17
1. 繼承可以重新定義變數或方法
2. 在變數或方法前加`Final`以防止重新定義
3. 也可以在class前加`Final`以防止繼承
4. 需要import
```py
from typing import Final
breed: Final = "Chihuahua"

@final
def info():
    pass

@final
class Pet():
```

## 是否為...的實利: 用isinstance() 22:37