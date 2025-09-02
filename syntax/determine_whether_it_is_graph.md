## 🧭 怎麼判斷一題是圖論題？
### 🚩 如果出現以下關鍵字 → 幾乎一定是圖論！
| 題目關鍵字                | 暗示圖論結構         |
| -------------------- | -------------- |
| `關係` / `依賴` / `前置條件` | 有向邊（DAG）       |
| `地圖` / `網格` / `城市`   | 節點＋邊 / 二維 BFS  |
| `傳送門` / `連通` / `跳躍`  | 邊的移動           |
| `最短路徑` / `最少步數`      | BFS / Dijkstra |
| `是否有循環` / `能不能走完`    | DFS 或拓樸排序      |

---

## 📚 題型分類 + 對應常用算法
1. 🧱 有向圖 + 拓樸排序

- 題型特色：依賴關係、流程順序、先修後修

- 代表題目：

    - Leetcode 207: Course Schedule

    - Leetcode 210: Course Schedule II

- 常用解法：BFS (Kahn's Algorithm)、DFS 判環

2. 🌐 無向圖 + 連通性問題

- 題型特色：城市間連通、島嶼、群組、朋友圈

- 代表題目：

    - Leetcode 200: Number of Islands

    - Leetcode 547: Number of Provinces

- 常用解法：DFS / BFS / Union-Find

3. 🏃‍♂️ 移動型圖論（最短路、BFS）

- 題型特色：網格地圖、迷宮、從起點走到終點、最短步數

- 代表題目：

    - Leetcode 542: 01 Matrix

    - Leetcode 994: Rotting Oranges

- 常用解法：Queue + BFS

4. 📦 加權圖 + 最短路徑

- 題型特色：有成本的移動（時間、金錢）

- 代表題目：

    - Leetcode 743: Network Delay Time

    - Leetcode 787: Cheapest Flights Within K Stops

- 常用解法：Dijkstra, Bellman-Ford

5. 🔁 是否存在循環

- 題型特色：避免死循環、檢查圖中是否有 cycle

- 代表題目：

    - Leetcode 207: Course Schedule

    - Leetcode 261: Graph Valid Tree

- 常用解法：DFS、Union-Find（無向圖）

---

## 🎯 快速判斷流程圖：

🧐 題目給你「一堆東西有依賴關係」嗎？ → 拓樸排序！

🗺 題目是地圖、網格移動？ → BFS！

🌐 題目問「誰跟誰有連通」？ → Union-Find 或 DFS！

🚀 題目有「最短路徑」或「成本」？ → Dijkstra！