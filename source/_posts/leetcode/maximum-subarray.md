---
title: 53. 最大子数组和
categories: Leetcode
tags:
  - leetcode
  - 动态规划
---

> 题目链接：https://leetcode-cn.com/problems/maximum-subarray/

## 题目描述

给你一个整数数组<code>nums</code> ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

**子数组**是数组中的一个连续部分。

**提示：**

- 1 <= nums.length <= 105
- -104 <= nums[i] <= 104

**进阶：**如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的<em>分治法</em>求解。

## 动态规划

dp[i]表示以nums[i]结尾的子数组的个数，所以dp[i] = max(dp[i-1] + nums[i], nums[i]);

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int len = nums.size();
        vector<int> dp(len);
        dp[0] = nums[0];
        int ret = nums[0];
        for(int i = 1; i < len; i++) {
            dp[i] = max(dp[i-1] + nums[i], nums[i]);
            ret = max(ret, dp[i]);
        }
        return ret;
    }
};
```