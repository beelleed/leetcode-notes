# 📚 貪婪演算法 Greedy Algorithm 筆記
## 🔍 定義 | Definition
### 🧾 中文說明：
- 貪婪演算法是一種在每個階段都做出當下看起來最好的選擇的策略，希望藉此導出全域最優解。

- 它不會回溯、不反悔，特別適用於「局部最優解能導出全局最優解」的問題。

### 🧾 English:
- A greedy algorithm builds up a solution by always making the choice that looks best at the moment. It does not reconsider choices once made and assumes that local optimal decisions lead to a globally optimal solution.

---

## ⚙️ 特徵 | Features
| 特徵   | 中文說明         | English Explanation                |
| ---- | ------------ | ---------------------------------- |
| 局部最優 | 每一步選當下最好的    | Makes the best local choice        |
| 不回頭  | 一旦選擇就不變更     | No backtracking or reconsideration |
| 計算快  | 時間複雜度常為 O(n) | Often O(n) or O(n log n) time      |

---

## ✅ 適用時機 | When to Use
- 問題有明確的最優子結構（Optimal Substructure）

- 每個子問題的最佳解不影響其他子問題的選擇

- 題目要求 最大值/最小值/最短/最多 等最佳化目標

---

## 🧮 範例 | Examples
### 🎯 LeetCode 題目應用：
| 題號   | 題目                                                                                              | 類型    |
| ---- | ----------------------------------------------------------------------------------------------- | ----- |
| 55   | [Jump Game](https://leetcode.com/problems/jump-game/)                                           | 範圍最遠  |
| 45   | [Jump Game II](https://leetcode.com/problems/jump-game-ii/)                                     | 次數最少  |
| 435  | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)           | 範圍選擇  |
| 1005 | [Maximize Sum After K Negations](https://leetcode.com/problems/maximize-sum-after-k-negations/) | 加總最大化 |

---

## ❌ 注意事項 | Pitfalls
- 貪婪 ≠ 通用解法

    - 並非所有問題都能用貪婪法求得最優解

    - 若局部最優會破壞全局最優 → 要用 DP、回溯等方法

---

## 📌 小結 | Summary
| 優點       | 缺點         |
| -------- | ---------- |
| 實作簡單、效率高 | 不一定保證全域最優解 |
| 不需額外記憶體  | 需證明適合用貪婪   |
