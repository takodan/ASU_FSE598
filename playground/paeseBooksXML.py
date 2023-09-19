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
parser.parse("./playground/myBooks.xml")