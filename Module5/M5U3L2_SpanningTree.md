## STP生成樹協議
1. 用於network switch網路交換器
2. 透過禁止部分端口來禁止不必要連接(例如環)產生
3. 實際流程:
    1. 一個網路交換器作為"root bridge"
    2. 把其他switch連接到"root bridge"的端口作為"root port"
    3. 在每個連接中任意選擇一邊不是"根端口"作為"designated port指定端口"
    4. 關閉沒有被選到的端口