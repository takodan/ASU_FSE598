## XMLTextWriter
1. 用於寫入XML的
    1. 文檔
    2. 元素
    3. 屬性
    4. 注釋
    5. 其他

## 以DOM在Python創建文檔
```py
from xml.dom import minidom
root = minidom.Document() # 建立DOM Document

courses = root.createElement("Courses") # 建立element
root.appendChild(courses) # 把courses接到root, 這裡root並不是跟元素而是XML Document

course = root.createElement("Course") # 建立element
course_name = root.createElement("Name") 
course_name.setAttribute("nameAttr","attributeValueHere") # 建立attribute
tempText = root.createTextNode("class1") # 建立內容

course_name.appendChild(tempText) # 把tempText接到course_name, 不論是element還是content都用 appendChild
course.appendChild(course_name) # 把course_name接到course
courses.appendChild(course) # 把course接到courses

course_name2 = root.createElement("Name") # 可以有重複的tag
tempText = root.createTextNode("class2")
course.appendChild(course_name2) # 可以先把name2接上course
course_name2.appendChild(tempText) #  再把text接上name2, 結果依然會顯示text
# 這裡因為courses已經有指向course, 所以不需要再appendChild

print(root.toprettyxml(indent="  ")) 

xml_str = root.toprettyxml(indent="  ") # XMLDoc 轉成字串
with open("myCourses.xml", "w") as f:
    f.write(xml_str)
```

## XPath
1. 用來描述元素位置, 類似於系統檔案位置
2. 例如XPath表達式: `/Courses/Course` 就是Courses底下所有Course元素的節點
3. XPath節點的類型:
    1. 元素
    2. 屬性
    3. 文本/內容
4. 常用表達式, 類似於UNIX:
    1. `@`代表屬性: `/Courses/Course/@Image`所有名為Image的屬性
    2. `.``..`代表當前目錄, 父目錄
    3. `*`代表所有: `/Courses/Course/@*`所有屬性
    4. `//`代表全文檔: `//Course`所有名為Course元素的節點
5. XPath有內建函數可以使用
6. XPath是XQuery的一部分
7. python中, 把xml解析成元素樹可以用`find`尋找
```py
import xml.etree.ElementTree as ET
root = ET.parse("myCourse.xml") # 解析進root
for course in root.findall("./Course") # 回傳找到的所有Course元素記憶體位置
    print(course.find("Name").text) # 加text改回傳位置上的內容
```
