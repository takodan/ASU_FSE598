## 高級語言 01:37
1. 命令式60s
2. 過程化70s: 第一代高階語言, Pascal, C
3. OOP面相對象90s: 第二代高階語言, C++, Java
4. 面向服務10s: 第三代高階語言, C#, Python
5. 工作流可視化10s20s: 第四代高階語言

## 工作流/可視化/ 圖形語言 根據流程圖來編程06:35
1. Microsoft: XLang
2. BPML: BPMN
3. IBM: WebServicesFlowLanguage
4. 多公司: BPEL
5. Microsoft: VPL, Workflow Foundation
6. Amazon: SWF

## additional information
[有限狀態機Finite State Machine](https://medium.com/pm%E7%9A%84%E7%94%9F%E7%94%A2%E5%8A%9B%E5%B7%A5%E5%85%B7%E7%AE%B1/%E5%A6%82%E4%BD%95%E6%9C%89%E9%82%8F%E8%BC%AF%E7%9A%84%E9%87%90%E6%B8%85%E4%BA%8B%E7%89%A9%E7%9A%84%E7%8B%80%E6%85%8B-f9fb59b15054)

## EXAMPLE:Workflow Foundation借貸審核 16:43 (pic)
1. start
2. receive customer data
3. initial screening
4. send screening response
5. switch
    1. rejected: end
    2. incorrect: go back to "2. receive customer data"
    3. approved
        1. ask vendor1
        2. decision
            1. approved: save in CRM: expose result to customer
            2. reject: ask vender2 ...


## Amazon SWF: 基於AWS 18:23
1. 服務開發人員編寫服務: 託管到AWS並註冊到SWF(service provider)
2. 工作流開發人員編排現有服務成一個完整的工作流: 也託管到AWS並註冊到SWF(service consumer)
3. SWF負責operation(service broker)
4. 最終用戶經由客戶端使用以編排好的工作流(end user)

## 常見工作流軟體: 多數工作流語言多用於教育且可視化 22:43
1. MIT: Scratch (可視化編程教育)
2. Carnegie Mellon: Alice (可視化遊戲編程)
3. Google: App Inventor (可視化手機編程)
4. Lego: NXT & EV3 (可視化機器人編程)
5. Intel: IoT SOL (可視化IoT編程)