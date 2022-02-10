---
title: 219. 存在重复元素 II
categories: Leetcode
cover: 'https://api.btstu.cn/sjbz/api.php'
top_img: 'https://api.btstu.cn/sjbz/api.php'
tags:
  - leetcode
  - 滑动窗口
---

> 这是第一篇leetcode刷题记录

给你一个整数数组&nbsp;<code>nums</code> 和一个整数&nbsp;<code>k</code> ，判断数组中是否存在两个 <strong>不同的索引</strong><em>&nbsp;</em><code>i</code>&nbsp;和<em>&nbsp;</em><code>j</code> ，满足 <code>nums[i] == nums[j]</code> 且 <code>abs(i - j) &lt;= k</code> 。如果存在，返回 <code>true</code> ；否则，返回 <code>false</code> 。

## 我的思路
将元素的位置和值组成节点并按节点的值排序，对于值相同的节点，只需要判断相邻的单位的位置差异，遍历完就可以判断出结果。算法复杂度主要在排序，为O(nlogn);

```cpp
struct Node {
    int val;
    int pos;
    bool operator<(const Node in) const {
        if(this->val < in.val) {
            return true;
        }else if(this->val > in.val) {
            return false;
        }else {
            return this->pos < in.pos;
        }
    }
    Node(int val, int pos) {
        this->val = val;
        this->pos = pos;
    }
};

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        vector<Node> list;
        for(int i = 0; i < nums.size(); i++) {
            Node *node = new Node(nums[i], i);
            list.push_back(*node);
        }
        sort(list.begin(), list.end());
        for(int i = 0; i+1 < list.size(); i++) {
            if(list[i].val == list[i+1].val) {
                if(list[i+1].pos-list[i].pos <= k) {
                    return true;
                }
            }
        }
        return false;
    }
};
```

## 使用滑动窗口

考虑数组 nums 中的每个长度不超过 k + 1k+1 的滑动窗口，同一个滑动窗口中的任意两个下标差的绝对值不超过 kk。如果存在一个滑动窗口，其中有重复元素，则存在两个不同的下标 i 和 j 满足 nums[i]=nums[j] 且 |i - j| ≤ k。如果所有滑动窗口中都没有重复元素，则不存在符合要求的下标。因此，只要遍历每个滑动窗口，判断滑动窗口中是否有重复元素即可。

如果一个滑动窗口的结束下标是 ii，则该滑动窗口的开始下标是 max(0,i−k)。可以使用哈希集合存储滑动窗口中的元素。从左到右遍历数组 nums，当遍历到下标 ii 时，具体操作如下：

1. 如果 i > k，则下标 i - k - 1 处的元素被移出滑动窗口，因此将 nums[i−k−1] 从哈希集合中删除；

2. 判断 nums[i] 是否在哈希集合中，如果在哈希集合中则在同一个滑动窗口中有重复元素，返回 true，如果不在哈希集合中则将其加入哈希集合。

当遍历结束时，如果所有滑动窗口中都没有重复元素，返回 false。

```cpp
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_set<int> s;
        int length = nums.size();
        for (int i = 0; i < length; i++) {
            if (i > k) {
                s.erase(nums[i - k - 1]);
            }
            if (s.count(nums[i])) {
                return true;
            }
            s.emplace(nums[i]);
        }
        return false;
    }
};
```