## 計算機模塊 00:42
1. CPU
    1. data path數據路徑: 執行運算, 包含寄存器和ALU
    2. control unit控制單元: 控制數據路徑和其他模塊
2. memory module內存模塊: 二進制儲存資料, 有儲存位置地址
3. peripheral外圍設備
    1. 輸入模塊
    2. 輸出模塊: 硬盤也屬於此

## 計算機系統 04:52
1. organization組成
    1. logic(gates)邏輯層 
    2. register-transfer寄存器傳輸層
    3. module模塊層
2. architecture架構
    1. module模塊層
    2. instruction指令集: 作為軟硬體之間的接口, 架構多指指令集
3. software軟體
    1. machine code機器碼: 直接以二進制操作指令集
    2. assembly program彙編程序: 用一些符號代替二進制
    3. hight level language program高級語言
    4. system software系統
    5. application 程式

### TIPS:  硬體設計用來執行指令集 軟體設計用來編排指令集

## 計算機發展 10:50
1. 存儲程序概念
    1. 以數字表示指令
    2. 把這些數字儲存起來, 可以順序執行多條指令
2. 系列的概念
    1. 區分出指令集 (架構), 同指令集可以有不同的硬體
3. pipelining流水線架構: 並行引入指令執行
4. multi core多核架構

## 計算機指令集 16:48
1. CISC複雜指令集計算機: 多種指令執行各種不同任務
2. RISC精簡指令集計算機: 指令精簡對硬體和流水線架構更友好

## 計算機性能 17:57
1. 用戶CPU時間
速度 = 1/ 執行時間
X比Y快: 速度X/ 速度Y = 執行時間Y/ 執行時間X
2. CPU時間 = CPU Clock Cycles(一條指令需要幾個週期)* Clock Cycle Time(每個週期要花多少時間)
    - = CPU Clock Cycles/ Clock Rate(每秒可以執行幾個週期)
3. 硬體設計成需要在CPU Clock Cycles和Clock Cycle Time做權衡
    1. 較快的週期, 可能會需要多個週期來完成一條指令
    2. MIPS架構一條指令要五個週期
4. 功耗牆
    1. Cycle Time 縮減到一定時間功耗快速增加, 因此2004年後處理器架構改往多核發展

## 計算機架構 29:23 (pic)
0. 內存速度慢, 寄存器速度快
1. accumulator累加器: 一筆資料由內存, 另一筆經由寄存器(累加器)進入ALU, 結果回存寄存器, 內存存取寄存器也把資料給ALU
2. stack堆棧: 兩筆資料同由寄存器(堆棧)進入ALU, 先進後出, 結果回存寄存器的第一筆資料, 內存只從寄存器存取
3. memory-memory內存-內存: 兩筆資料同由內存進入ALU, 中間沒有寄存器
4. load-store加載-存儲(RISC為此類架構): 類似於堆棧, 但是可以藉由記憶體地址訪問特定資料
5. compound複合(CISC為此類架構): 資料從內存進入一寄存器和一有地址的寄存器, 所有資料均經過一條總線

## EXAMPLE: 不同架構的彙編程序
IC: 指令 MA: 內存訪問
y = x1 * x2 + x3 / x4
1. 累加器(只有一個寄存器, 沒有記憶體位置)
    1. Load x1: MA -> register
    2. mult x2: MA & register -> ALU -> register
    3. Store y: register -> MA(y)
    4. Load x3: MA -> register
    5. div x4: MA & register -> ALU -> register
    6. Add y: MA(y) & register -> ALU -> register
    7. Store y: register -> MA(y)
    8. result: IC:7, MA:7
2. 堆棧
    1. push x1: MA -> stack:x1
    2. push x2: MA - stack:x2, x1
    3. mult: stack -> ALU -> stack:y
    4. push x3: MA -> stack:x3, y
    5. push x4: MA -> stack:x4, x3, y
    6. div: stack -> ALU -> stack:z, y
    7. Add: stack -> ALU -> stack:y
    8. pop y: stack-> MA
    9. result: IC:8, MA:5
3. 內存-內存
    1. mult x1 x2: MA & MA -> ALU -> MAx2
    2. div x3 x4: MA & MA -> ALU -> MAx4
    3. Add x2 x4: MA & MA -> ALU -> MAx4
    4. move x4 y: MAx4 -> MAy
    5. result: IC:4, MA:11
4. 加載-存儲:
    1. move x1 R1: MA -> 寄存器
    2. move x2 R2: MA -> 寄存器
    3. move x3 R3: MA -> 寄存器
    4. move x4 R4: MA -> 寄存器
    5. mult R1 R2: 寄存器 -> ALU -> 寄存器R2
    6. div R3 R4: 寄存器 -> ALU -> 寄存器R4
    7. Add R2 R4: 寄存器 -> ALU -> 寄存器R4
    8. move R4 y: 寄存器 -> MA
    9. result: IC:8, MA:5

## conclusion
1. 硬體和軟體
2. 技術發展快速
3. 因功率限制Cycle Time 進一步縮短, 多往併行(線程, 多核)發展
4. 指令集為軟硬體之間的接口
5. 計算機架構由指令集決定