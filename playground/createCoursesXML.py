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
with open("./playground/myCourses.xml", "w") as f:
    f.write(xml_str)

import xml.etree.ElementTree as ET
root = ET.parse("./playground/myCourses.xml")
for course in root.findall("./Course"):
    print(course.find("Name").text)