# XML 基本要素
1. XML的應用p4
2. XML和HTML的比較p5p6
3. XML的格式p9
4. 名詞定義:
    1. 元素: 定義一個用來儲存數據的位置, 可以數據為空
    2. 屬性: 附加在元素內的信息
    3. 內容: 實際儲存的數據
5. 和其他語言一樣有特殊字符, 要區分可以使用&符號引用名稱或ASCII字符p15
6. 或是用`<![CDATA[ ... ]]>`標記數據讓XML忽略解析
7. 空字符p19
8. 歸依化p20
9. 注釋符p21
10. 命名空間p22


# XML 解析
1. DOM模型: 整個檔案讀取進內存成為樹狀結構
2. 樹遍歷算法p10
3. SAX模型: 一次只讀一個節點, 節省內存. 用於讀取, 搜索XML內容


# XML 編輯和查詢
1. 跳過程式碼部分
2. XPath p8
    1. 類似作業系統路徑
    2. 範例
        1. `/Courses/Course`: Courses底下所有Course元素
        2. `/Courses/Course/@Image`: Courses底下所有Course元素的所有Image屬性
        3. `/Courses/*`: Courses底下所有元素
        4. `/Courses/@*`: Courses底下所有元素的所有屬性
        5. `//Course`: 任意位置的所有Course元素
3. XPath函數p10
4. XPath應用p12~p17


# XML 類型定義
1. DTD語法p7p8
2. XML schema語法p19p22


# Other Data Standards 其他數據結構標準
1. 數據結構轉換範例
    1. 假設有ABCDE五種結構
    2. 把其中一種結構當成主要結構, 這裡選A
    3. 其他結構只要可以轉換成A就可以轉換成所有結構
    4. 所以剩下的四種結構, 每種結構都有一個轉換器轉換成A
    5. A有四個轉換器轉換成剩下的四種結構
    6. 總共需要8個轉換器
2. RSS 2.0: 一種有特定類型定義的XML
3. Atom: 類似RSS 2.0, 只是有更多類型可用
4. JSON: 
    1. 和Python的數組和字典類似, 差異p22
    2. JSON的值可以是: 列表, 字典, 字符串, 整数(正負樹, 正數不用符號), 浮點數, 布林值, NULL


# Enterprise Architecture 企業架構
1. 企業應用集成架構EAI目的p7:
    1. 集成開發和維護
    2. 訊息一致
    3. 方便應用互通
    4. 使企業可以獨立於應用供應商
    5. 單一訪問接口
2. 企業應用模型EAM p10
3. 聯邦企業應用框架FEAF
    1. 目的p11
    2. 開發步驟p12
    3. 架構組成p14
    4. 架構視圖p15~p19
    5. 業務架構框架:
        1. 用來描述企業分類和組織
        2. Zachman模型p20p21
        3. 企業架構規劃EAP p22p23
        4. 開放組織架構框架TOGAF p24


# Workflow Foundation 工作流
1. 工作流p3
2. 工作流優點p4
3. WF的活動模塊
    1. 控制p9p10p11
    2. 流程圖p12
    3. 異步p13
    4. 其他活動p14
4. WF的自定義活動p15
5. 實作
    1. 程序的入口點是Program.cs 中的 Main() 方法

# BPEL 業務過程執行語言
1. 和WF比較p3
2. BPEL結構
    1. 合作夥伴partner:客戶端或其他服務 p5
    2. 邏輯活動p7p8
3. 調用web services p14p15p19p20
4. 調用會由一個WSDL文件來定義

# 業務流程圖形表示
1. BPEL有圖形開發工具
2. BPMN: BPEL的替代方案
3. BPEL和BPMN比較p10
4. WF, BPEL, BPMN:
    1. 工作流程p11p12
    2. 重要總結p18


