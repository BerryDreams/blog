---
title: 57. 插入区间
categories: Leetcode
tags:
  - leetcode
  - 模拟
---

> 题目链接：https://leetcode-cn.com/problems/insert-interval/

## 题目描述

给你一个<code>无重叠的</code>，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

**提示：**

- <code>0 <= intervals.length <= 104</code>
- <code>intervals[i].length == 2</code>
- <code>0 <= intervals[i][0] <= intervals[i][1] <= 105</code>
- <code>intervals 根据 intervals[i][0] 按 升序 排列</code>
- <code>newInterval.length == 2</code>
- <code>0 <= newInterval[0] <= newInterval[1] <= 105</code>

## 模拟

当遍历到一个区间，判断插入区间在其左边还是右边
- 在右边则不处理插入区间，直接插入当前区间。
- 在左边就插入插入区间，然后插入当前区间。
- 否则表明当前区间和插入区间有交集，更新插入区间范围。

> Ps.定义一个flag，确保插入有且只有一次。

```cpp
class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> ret;
        bool flag = false;
        int nowl = newInterval[0], nowr = newInterval[1];
        for(int i = 0; i < intervals.size(); i++) {
            int l = intervals[i][0], r = intervals[i][1];
            if(l > nowr) {
                if(!flag) {
                    ret.push_back({nowl, nowr});
                    flag = true;
                }
                ret.push_back({l,r});   
            }else if(nowl > r) {
                ret.push_back({l,r});
            }else {
                nowl = min(nowl, l);
                nowr = max(nowr, r);
            }
        }
        if(!flag) {
            ret.push_back({nowl,nowr});
        }
        return ret;
    }
};
```