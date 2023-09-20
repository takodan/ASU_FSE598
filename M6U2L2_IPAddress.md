## IPv4
1. 地址有32bits, 有分ABCDE類, 
2. 地址前幾bits做類別判斷, 接著是網路號(網段號)和主機號
3. 類型範圍:
    1. A類: 0.0.0.0到127.255.255.255
    2. B類: 128.0.0.0到191.255.255.255
    3. C類: 192.0.0.0到239.255.255.255
    4. D類: 用作Multicasting, 幾乎沒有使用
    5. E類保留不用
4. 類型從A到C, 可用網路地址越多, 一個網路底下可用主機越少

## IPv4預留專有地址
1. 只在區域網路內使用
2. 1個A類: 10.0.0.0
3. 16個B類: 172.16.0.0 
4. 256個C類: 192.168.0.0

## 子網
1. 因為區域網路IPv4地址有限, 要把AB類的主機號切分成子網路和主機號增加可用地址
2. subnet mask子網絡遮罩/子網掩碼
    1. 掩碼: 類原本的網路號為1, 主機號為0
    2. 把要做子網路的地址和掩碼做與運算(兩個位都是1)
    3. 子網也會有主保留機號, 例如全0代表此網路, 全1用作廣播
3. VLSM可變長度子網掩碼: 藉由不同長度掩碼再分割子網
    1. 優點: 
        1. 可以有較小的網路交換器, 加速網路
        2. 易於管理
        3. 更安全
    2. 缺點:
        1. 增加複雜性, 需要比較多路由器
        2. 結構建立後難改變

## CIDR無類別域間路由
1. 類似VLSM, 但不受類型限制, 子網分配更有彈性
2. 掩碼以`/n`表示, n代表掩碼有幾個1
    - A類變成`/8`, B類變成`/16`
3. 兩種子網方式也可以用於區域網路

## EXAMPLE:CIDR地址分配
1. 有一個地址塊200.25.0.0/16
2. 分給A二分之一, B四分之一, C, D八分之一
3. 解法
    1. 原地止1100100.00011001.00010000.00000000, 200.25.16.0/20
    2. 先分二分, 也就是把掩碼前推一位
    3. 分給A:1100100.00011001.00010000.00000000, 200.25.16.0/21
    4. 保留1100100.00011001.00011000.00000000, 200.25.24.0/21
    5. 後面依相同方式切割