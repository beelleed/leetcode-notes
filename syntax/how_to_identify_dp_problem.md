# 📚 如何判斷一題是否可以使用動態規劃（Dynamic Programming）

---

## 🎯 什麼是動態規劃？

動態規劃是一種適用於「將一個大問題拆成多個子問題，並重複使用子問題結果」的技巧，特別適合解決：

- 最長/最大/最短/最少 類型問題（例如：最大值、最短路徑、最長子序列）
- 多階段決策問題（每步都有選擇，需找到最優解）

---

## ✅ 判斷標準一覽

| 判斷條件           | 說明                                                      | LCS（最長公共子序列）是否符合？ |
|--------------------|-----------------------------------------------------------|----------------------------------|
| 1️⃣ 最優子結構      | 子問題的解可以組合出整體的最佳解                                | ✅ 是                             |
| 2️⃣ 重複子問題      | 同樣的子問題會被反覆計算                                    | ✅ 是                             |
| 3️⃣ 決策階段性      | 問題可以切割成多個階段逐步解決                                 | ✅ 是                             |
| 4️⃣ 無法貪心或DFS處理 | 貪心策略不能保證全域最優；DFS 或暴力解法會超時                    | ✅ 是                             |
| 5️⃣ 涉及「最長/最多」 | 題目要求最大值、最長長度、最多方法數等                            | ✅ 是                             |

---

## 🧠 更進階的 DP 類型分類

| 類型        | 範例題目 / 狀況                                      | 常見變數與狀態設計 |
|-------------|-------------------------------------------------------|--------------------|
| 序列型 DP   | 最長上升子序列、LCS、爬樓梯、跳格子                     | dp[i], dp[i][j]    |
| 分割型 DP   | 區間合併、石頭合併、回文切割                             | dp[i][j]（區間）    |
| 組合型 DP   | 換硬幣問題、背包問題、排列組合數                         | dp[i] = ways       |
| 狀態壓縮 DP | 記憶體或時間限制嚴格（如二維壓一維、用 bit mask 儲存狀態） | dp[mask][i]        |

---

## 🚫 不適合 DP 的情況

| 情境                          | 原因                                               |
|-------------------------------|----------------------------------------------------|
| 每個決策完全獨立              | 沒有子問題之間的遞推關係                             |
| 沒有「最大值 / 最短距離」等需求 | 不需要找出最優解、只要找到一種解法                    |
| 貪心可解並保證正確             | 例如區間合併（用 sort 處理）或找最大間隔差             |

---

## 🛠️ 四步設計 DP 解法

1. **定義狀態**：dp[i]、dp[i][j] 代表什麼
2. **寫出狀態轉移方程式**  
   例：`dp[i][j] = dp[i-1][j-1] + 1` （若字元相同）或 `max(dp[i-1][j], dp[i][j-1])`
3. **初始化 base case**：例如 dp[0][*] = 0，dp[*][0] = 0
4. **按順序填表**：通常是從小 (i, j) 推到大

---
## 📌 圖解範例：LCS Table 與指向箭頭

圖解展示如何填 LCS 表格：


::contentReference[oaicite:1]{index=1}


- 每個 cell dp[i][j] = 左/上/左上最大值或 +1
- 箭頭表示你要從哪個方向回推文字序列

---

## 🧠 DP 表格範例：背包 / Subset Sum

- 背包問題二維陣列填表邏輯

::contentReference[oaicite:2]{index=2}

---

## 📝 附加建議

- 想不到怎麼下手時，先想「我能不能定義一個 `dp[i]` 表示某狀態的最佳值？」
- 不會寫也沒關係，先從寫出狀態轉移方程式開始
- 可畫表格或遞推圖幫助自己理解 `dp` 怎麼一步步推進

---

## 📌 推薦入門 DP 題目清單

| 題號 | 題目                                    | 難度 | 類型   |
|------|-----------------------------------------|------|--------|
| 70   | Climbing Stairs                         | Easy | 序列型 |
| 198  | House Robber                            | Easy | 序列型 |
| 509  | Fibonacci Number                        | Easy | 序列型 |
| 1143 | Longest Common Subsequence              | Medium | 序列型 |
| 322  | Coin Change                             | Medium | 組合型 |
| 139  | Word Break                              | Medium | 組合型 |
| 221  | Maximal Square                          | Medium | 區間型 |
| 0/1 背包 | 多平台皆有                              | Medium | 組合型 |

---
