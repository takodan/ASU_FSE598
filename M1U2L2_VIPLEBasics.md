## ASU VIPLE 00:36
1. 通用控制流編程
2. 可用於物聯網和機器人編程
3. 支持並行, 多線程
4. 面向服務, 支持RESTful, WSDL
5. 基於pi代數 (函數程式設計視基於lambda代數)

## VIPLE basic activities 04:23
1. activity自定義活動: 將模塊打包
2. variable
3. calculate
4. data: value
5. join與合併: 等所有線程結果輸入才會進入下一步
6. merge或合併: 多線程, 只要有一輸入就會進入下一步
7. if
8. switch: 根據條件切換路徑
9. while
10. break
11. end while


## VIPLE介面 15:05
1. 左側欄為活動
    1. 基本
    2. 通用服務: modules
    3. 機器人服務: 機器人驅動傳感控制
    4. 樂高機器人服務
    5. 量子計算服務
2. 中間為編程區
3. 右側欄為機器人編程設定
4. 右鍵可以翻轉模塊

## EXAMPLE: 19:41
1. 輸出Hello world到警示視窗: data(Hello world) -> simple dialog(通用服務:簡單對話)
2. 輸出Hello world到cmd: data -> print line(通用服務:行打印)
3. 輸入: simple dialog右鍵更改連接, 改成prompt, 設定PromptText和DefaultValue -> calculate(value) -> print line
4. 計算: 用作計算, 調用function(Convert, Math, DateTime), 判斷式
    - 預設變數value為輸入值
    - 可以使用join或merge輸入多變數, 並更改變數名稱
5. 變量: 只做變量命名, 需要輸入data(value), 全域變量state.variableName
6. 自定義活動可以增設參數(不用另設模塊), 活動參數instance.variableName