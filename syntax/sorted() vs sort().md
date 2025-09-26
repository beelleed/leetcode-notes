# 📝 Python 排序方法比較：sorted() vs .sort()
## 📌 差別總覽

| 特性          | `sorted()`                                       | `.sort()`                         |
| ----------- | ------------------------------------------------ | --------------------------------- |
| **型別**      | 函數 (function)                                    | list 方法 (method)                  |
| **回傳值**     | **新 list**（已排序）                                  | **None**（就地排序 in-place）           |
| **適用對象**    | 任何可迭代物件 (list, tuple, string, set, dict keys...) | 只能用在 list                         |
| **是否改變原資料** | ❌ 不會                                             | ✅ 會改變                             |
| **效率**      | 複製一份資料再排序，稍慢                                     | 原地排序，稍快                           |
| **語法**      | `sorted(iterable, key=..., reverse=...)`         | `list.sort(key=..., reverse=...)` |

---

## 🔎 範例
1. sorted 不改變原資料
```python
nums = [3, 1, 2]
new_nums = sorted(nums)

print(nums)      # [3, 1, 2]   （原本的沒變）
print(new_nums)  # [1, 2, 3]   （新 list）
```

2. .sort 就地排序
```python
nums = [3, 1, 2]
nums.sort()

print(nums)      # [1, 2, 3]   （原本的被改變了）
```

3. sorted 可用於字串 / tuple / set
```python
s = "leetcode"
print(sorted(s))  
# ['c', 'd', 'e', 'e', 'l', 'o', 't']

t = (3, 1, 2)
print(sorted(t))  
# [1, 2, 3]
```
- .sort() 只能用在 list，否則會報錯。

4. key 與 reverse

- 兩者都支援 key 與 reverse：
```python
nums = [3, 1, 2]

print(sorted(nums, reverse=True))  
# [3, 2, 1]

nums.sort(key=lambda x: -x)
print(nums)  
# [3, 2, 1]
```

- reverse=False（預設值） → 升冪排序（由小到大）

- reverse=True → 降冪排序（由大到小）

## ✅ 總結

- sorted()

    - 適合需要保留原資料的情境

    - 適合處理非 list 的迭代物件（字串、tuple、set...）

- .sort()

    - 僅限 list

    - 原地排序，效率稍高

    - 適合只關心排序後結果、不在乎原順序的情境