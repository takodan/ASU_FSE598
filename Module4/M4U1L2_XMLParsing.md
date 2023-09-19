## XML 解析器
1. DOM 文件物件模型
    1. 將整個文件讀取進內存, 可以以樹結構訪問 
    2. 如果檔案太大可能會有問題
    3. DOM 同樣可以用於 HTML
2. SAX Simple API for XML
    1. 循序存取
    2. 基於事件API, 一次讀取一個節點
3. XPath
    1. 查詢語言

## 用程式以DOM讀取XML
1. Python
```py
from urllib.request import urlopen # 用來從網址取得檔案
from xml.dom import minidom # 用來解析XML
# 解析檔案回傳XMLDocument object
doc = minidom.parse(urlopen("url"))
# 輸出, function 在下一個block
# doc.firstChild 也就是根
OutputNode(doc.firstChild)
```
2. C#
```cs
XmlDocument xd = new XmlDocument() // 創建一個新的 XMLDocument object
xd.Load("url") // 將網址解析進 XMLDocument object
```

## 用Python 輸出XML
```py
def OutputNode(node):
    # 一次印出一個節點
    print("Type={0}".format(node.nodeType))
    print("Name={0}".format(node.nodeName))
    print("Value={0}".format(node.nodeValue))
    # 看這個節點還有沒有子節點
    if node.hasChildNode():
        # 取出所有子節點
        children = node.childNode
        # 把子節點利用迴圈印出
        for child in children:
            OutputNode(child)
```

## 前序後序複習
```xml
<Name>name1</Name>
<Table>
    <CITY>name2</CITY>
    <STATE>name3</STATE>
    <ZONE>name4</ZONE>
</Table>
```
前序, 一個節點的子節點跑完, 才會到下一個節點: name1, name2, name3, name4
後序, 先到最底層節點, 跑完再回來上一層: name2, name3, name4, name1

## SAX讀取XML
1. 如果只是要讀取內容, 沒有要知道結構, 適用
2. 快速, 只能向前, 只能讀取
3. 基於work flow, 不會一次讀取整個內容
4. 更省內存, 但是因為不能指定算法路徑, 可能更耗時
5. 更容易搜索
6. 讀取路徑多為前序

## 用Python以SAX讀取XML
```py
from urllib.request import urlopen # 用來從網址取得檔案
from xml.sax import parse # 用來解析xml
from xml.sax.handler import ContentHandler # 用來定義解析方式
# 需要創建一個class繼承 ContentHandler
class MyHandler(ContentHandler):
    isTextRead = []
    def startElement(self, name, attrs):
        if name == "Code":
            print(f"Name={name}")
        else:
            print(f"Name={name}", end=" ")
        self.isTextRead.append(False)
    def characters(self, content):
        if not self.isTextRead.pop():
            print("Text=" + content.strip())
            self.isTextRead.append(True)
        else:
            self.isTextRead.append(True)
    def endElement(self, name):
        print(f"End{name}")
        self.isTextRead.pop()
thisHandler = myHandler()
parse("Course.xml", thisHandler)
```

## Bard給出的範例
簡單來說解析的時候, 遇到開始tag會呼叫startElement, 結束tag會呼叫endElement, 內容會呼叫characters
```py
import xml.sax

class MyHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        print("開始處理元素：", name)
        if attrs is not None:
            for key, value in attrs.items():
                print("屬性：", key, "=", value)

    def endElement(self, name):
        print("結束處理元素：", name)

    def characters(self, content):
        print("內容：", content)


parser = xml.sax.make_parser()
parser.setContentHandler(MyHandler())
parser.parse("books.xml")
```
XML檔案
```xml
<?xml version="1.0" encoding="UTF-8"?>
<books>
    <book id="1">
        <title>The Lord of the Rings</title>
        <author>J.R.R. Tolkien</author>
    </book>
</books>
```
output
```
開始處理元素： books
內容：

內容：
開始處理元素： book
屬性： id = 1
內容：

內容：
開始處理元素： title
內容： The Lord of the Rings
結束處理元素： title
內容：

內容：
開始處理元素： author
內容： J.R.R. Tolkien
結束處理元素： author
內容：

內容：
結束處理元素： book
內容：

結束處理元素： books
```