#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : Liu Kun
# date   : 2022-05-15 21:04:20

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 1
# 题目名称: 两数之和
# 题目难度: Easy

# 知识点: 数组, 哈希表

# 题目详情:
"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]

提示：
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
只会存在一个有效答案

进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？
"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        时间复杂度：O(N^2)，其中 N 是数组中的元素数量。最坏情况下数组中任意两个数都要被匹配一次。
        空间复杂度：O(1)。
        :param nums:   整数数组
        :param target: 整数目标值
        :return: 数组下标
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum_v2(self, nums: List[int], target: int) -> List[int]:
        """
        时间复杂度：O(N)，其中 N 是数组中的元素数量。对于每一个元素 x，我们可以 O(1) 地寻找 target - x。
        空间复杂度：O(N)，其中 N 是数组中的元素数量。主要为哈希表的开销。
        :param nums:   整数数组
        :param target: 整数目标值
        :return: 数组下标
        """
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_case_1(self):
        result = self.inst.twoSum([2, 7, 11, 15], 9)
        self.assertEqual([0, 1], result)

    def test_case_2(self):
        result = self.inst.twoSum([3, 2, 4], 6)
        self.assertEqual([1, 2], result)

    def test_case_3(self):
        result = self.inst.twoSum([3, 3], 6)
        self.assertEqual([0, 1], result)


if __name__ == "__main__":
    unittest.main()
