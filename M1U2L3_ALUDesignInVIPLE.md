## EXAMPLE: 用VIPLE模擬ALU: 自定義邏輯門 03:45
1. 自定義活動
2. 設定參數(邏輯門的輸入), a, b
3. 模塊
    1. if(ab排列組合)做路徑選擇數據(最後只有1輸出, 但是下個組件要分成兩個輸入, 要2個或併)
    2. 選擇輸出數據0 or 1(最後只有1輸出, 1個或併)
    3. 輸出
- 與併: 多線路多輸入, 或併: 多線路單輸入

## EXAMPLE: 1bit 加法器 06:08 (pic)
1. 自定義活動
2. 設定參數(加法器的輸入), a, b, carryIn
3. 按照邏輯圖擺放部件, 需要多個與門來讓兩個參數同時輸入邏輯門 
4. 最後會輸出兩個值, 加法結果, carryOut (同樣利用與門)

## EXAMPLE: 測試 07:24
簡單的把打包好的加法器輸入參數, 直接print line
- 可以把右鍵點擊自定義活動轉成服務, 讓其他VIPLE程式使用

## EXAMPLE: 多路轉接器 11:29
1. 類似邏輯門, 輸入兩個(2bits)參數, 決定從四個參數中決定哪一個輸出(總共會有六個參數6bits輸入)

## 自動化測試 14:49
1. 自定義事件, 想辦法把測試邏輯寫出來, 當作事件輸出(圓點)而非數據輸出(三角)

## RESTful services 22:50
可以設定參數, 利用{0}{1}組合成URL

## Pi 代數 29:04
在run 可以把程式傳換成 Pi 代數

## Code Activity 29:58
直接編寫程式碼取代activity, 或是直接增加reference library


