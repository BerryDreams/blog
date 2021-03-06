---
title: 62. 最小路径和
categories: Leetcode
tags:
  - leetcode
  - 动态规划
---



## 动态规划

f(i,j)表示从(0,0)到(i,j)的路径数量。
```
f(i,j)=f(i−1,j)+f(i,j−1)
```
代码如下
```cpp
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> map(m, vector<int>(n));
        for(int i = 0; i < m; i++) {
            map[i][0] = 1;
        }

        for(int i = 0; i < n; i++) {
            map[0][i] = 1;
        }

        for(int i = 1; i < m; i++) {
            for(int j = 1; j < n; j++) {
                map[i][j] = map[i-1][j] + map[i][j-1];
            }
        }
        return map[m-1][n-1];
    }
};
```