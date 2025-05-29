# 🧠 Sliding Window vs. HashMap vs. Prefix Sum 解題技巧區分指南

---

## 🧭 判斷標準速查表

| 題目類型關鍵字 | 建議解法類型 |
|----------------|---------------|
| **連續子陣列/子字串** + 範圍控制 | ✅ Sliding Window |
| **統計頻率 / 查值是否存在 / 一次掃描找配對** | ✅ HashMap |
| **加總 = k / 目標差值 / 子陣列和問題** | ✅ Prefix Sum + HashMap |

---

## 🔹 Sliding Window 滑動視窗

### ✅ 使用時機：

- 陣列或字串中「連續子區間」
- 題目要求找「最大長度」、「最短長度」、「最大總和」

### 🧠 範例題目：

| 題號 | 題目 | 類型 |
|------|------|------|
| 3 | Longest Substring Without Repeating Characters | 無重複子字串長度 |
| 209 | Minimum Size Subarray Sum | 最小子陣列長度 |
| 904 | Fruit Into Baskets | 最多裝兩種水果的子陣列 |

### 🔧 標準寫法：

```python
left = 0
for right in range(len(s)):
    while 條件不滿足:
        left += 1
    更新答案
```

##🔹 HashMap 哈希表 / 字典
✅ 使用時機：
- 計算某個元素的出現次數

- 快速查找是否出現過某元素（Two Sum）

- 記錄某個狀態（字元、數值、出現位置等）

## 🧠 範例題目：
| 題號  | 題目                                             | 類型         |
| --- | ---------------------------------------------- | ---------- |
| 1   | Two Sum                                        | 查找目標差值     |
| 387 | First Unique Character in a String             | 字元次數統計     |
| 242 | Valid Anagram                                  | 比對字元頻率     |
| 3   | Longest Substring Without Repeating Characters | + Set 結合使用 |

## 🔧 常用語法：
```python
count = {}
count[ch] = count.get(ch, 0) + 1

# 或用 collections.defaultdict(int)
```

## 🔹 Prefix Sum 前綴和
✅ 使用時機：
- 題目問「有幾段子陣列的總和 = k」

- 不一定要連續滿足條件（可從 0 開始）

- 結合 HashMap 找差值是否出現過

## 🧠 範例題目：
| 題號  | 題目                           | 類型          |
| --- | ---------------------------- | ----------- |
| 560 | Subarray Sum Equals K        | 前綴和差值計數     |
| 974 | Subarray Sums Divisible by K | 餘數相同前綴和     |
| 523 | Continuous Subarray Sum      | 子陣列和是 K 的倍數 |

## 🔧 標準寫法：
```python
count = {0: 1}  # 注意初始化
prefix = 0
for num in nums:
    prefix += num
    if prefix - k in count:
        ans += count[prefix - k]
    count[prefix] = count.get(prefix, 0) + 1
```

## ✅ 總結表格
| 題目需求                | 使用方式                 |
| ------------------- | -------------------- |
| 連續區間 + 最長 / 最短條件    | Sliding Window       |
| 查某元素是否出現過、次數統計      | HashMap              |
| 連續子陣列和 = k（子區間差值問題） | Prefix Sum + HashMap |

## 🧪 快速練習題

| 題號  | 題目                                             | 解法                       |
| --- | ---------------------------------------------- | ------------------------ |
| 3   | Longest Substring Without Repeating Characters | Sliding Window + Set     |
| 209 | Minimum Size Subarray Sum                      | Sliding Window           |
| 904 | Fruit Into Baskets                             | Sliding Window + HashMap |
| 1   | Two Sum                                        | HashMap                  |
| 387 | First Unique Character in a String             | HashMap                  |
| 560 | Subarray Sum Equals K                          | Prefix Sum + HashMap     |
