# 🧭 如何判斷使用回溯法（Backtracking）題型筆記
## ✅ 什麼是回溯法？
回溯法（Backtracking） 是一種遞迴演算法，用來探索「所有可能的解」，並在途中不滿足條件時「回頭嘗試其他路徑」。

---

## 🔍 常見題型特徵 | When to Use Backtracking
| 題目特徵               | 中文說明          | 英文說明                                           |
| ------------------ | ------------- | ---------------------------------------------- |
| ❓ 問「所有可能解」         | 要找出所有解或所有組合   | Find all possible combinations/solutions       |
| 🧩 元素有選／不選的可能性     | 每個元素可能加入或不加入  | Each element has choice to include/exclude     |
| ⛔ 有條件限制（如目標和、不能重複） | 有需滿足的條件時就剪枝   | Prune paths if constraints are violated        |
| 🔁 需要多步探索＋退回       | 嘗試不同路線直到成功或失敗 | Try paths recursively, and backtrack if failed |

---

## 🧪 題目例子 | Typical Problems
| 題號 | 題目名稱                 | 說明                 |
| -- | -------------------- | ------------------ |
| 78 | Subsets 子集           | 列出所有子集             |
| 39 | Combination Sum      | 找出總和為 target 的所有組合 |
| 46 | Permutations         | 所有不重複的排列           |
| 22 | Generate Parentheses | 所有合法括號組合           |
| 51 | N-Queens             | 所有皇后擺法解            |

---

## 📌 回溯的典型寫法 | Backtracking Template
```python
def backtrack(start, path):
    if 滿足條件:
        res.append(path[:])
        return

    for i in range(start, len(候選項目)):
        path.append(候選項目[i])
        backtrack(i 或 i+1, path)
        path.pop()
```

---

## 🧠 為什麼要寫一個 def？
- 因為每一次選擇都要進一步試探下一步，而這種 遞迴 + 嘗試 + 回退 的行為，需要一個遞迴函式來實現，這就是 def backtrack(...) 的原因。

---

## ✅ 判斷是否要用回溯的 3 步法
- 題目問「所有可能／組合／排列」？

- 解答數量不只一個？

- 是否有條件需要過濾？

➡️ 全部 YES，就 90% 是回溯法！

---

## 🎯 常見搭配技巧
- start 參數：避免重複選擇，控制下次從哪個 index 開始

- path 或 track：用來記錄目前已選項目

- path.pop()：回溯時撤銷上一步選擇

- 剪枝條件（例如剩餘 target < 0）：提早結束遞迴