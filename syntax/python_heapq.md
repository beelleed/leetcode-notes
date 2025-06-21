# 📚 Python `heapq` 教學筆記 | Heap 使用指南
---

## 📖 什麼是 heapq？| What is `heapq`?

### 🧠 定義 Definition

**EN**  
`heapq` is a built-in Python module that provides an implementation of the **min-heap** using lists.  
It allows for efficient insertion, removal, and retrieval of the smallest element.

**ZH**  
`heapq` 是 Python 內建模組，用來操作 **最小堆（min-heap）** 的資料結構，底層使用 list 實作。  
可高效進行加入、刪除與取得最小值等操作。

---

## 🧰 常用函數 | Common Functions

| 函數名稱        | 說明（中文）                       | Description (English)                        |
|-----------------|-------------------------------------|----------------------------------------------|
| `heapify(list)` | 將 list 就地轉成最小堆            | Convert list into a min-heap in-place       |
| `heappush(heap, item)` | 加入元素並維持堆性質     | Push item into heap while maintaining order |
| `heappop(heap)` | 移除並回傳最小值（堆頂）           | Pop and return the smallest element         |
| `heappushpop(heap, item)` | 先 push 後 pop，更快 | Push then pop in one operation              |
| `heapreplace(heap, item)` | 先 pop 再 push（效率高） | Pop then push in one operation              |
| `nlargest(k, iterable)` | 回傳前 k 大元素（需排序）     | Return k largest elements                   |
| `nsmallest(k, iterable)` | 回傳前 k 小元素             | Return k smallest elements                  |

---

## 📌 基本用法範例 | Basic Usage Examples

```python
import heapq

nums = [5, 3, 8, 1]
heapq.heapify(nums)        # nums 變成 min-heap：[1, 3, 8, 5]
heapq.heappush(nums, 2)    # 插入元素 2：[1, 2, 8, 5, 3]
print(heapq.heappop(nums)) # 取出最小值：1
```

## 🔄 模擬最大堆技巧 | Max Heap with heapq
因為 heapq 是最小堆，要模擬最大堆可以用「負數轉換技巧」：

```python
import heapq

nums = [5, 1, 8]
max_heap = [-n for n in nums]
heapq.heapify(max_heap)

# 取出最大值
max_val = -heapq.heappop(max_heap)
print(max_val)  # 輸出：8
```

## 🎯 應用場景 | When to Use
- Top K 問題（找前 k 大/小）

- 優先佇列（priority queue）

- 排程系統（task scheduling）

- 資料流中維持排序資料

## ⏱️ 時間複雜度 | Time Complexity
| 操作 Operation           | 複雜度 Complexity |
| ---------------------- | -------------- |
| `heappush` / `heappop` | O(log n)       |
| `heapify`              | O(n)           |
| `heap[0]`（取堆頂）         | O(1)           |

## 🧠 小結 | Summary
- heapq 是 Python 操作最小堆的標準工具

- 適合快速找出最小值或維持排序資料

- 模擬最大堆需將數字取負再轉回

## 📚 延伸閱讀 | References
- [Python 官方文件](https://docs.python.org/3/library/heapq.html)

- [LeetCode 題型：Top K Elements](https://leetcode.com/problems/top-k-frequent-elements)