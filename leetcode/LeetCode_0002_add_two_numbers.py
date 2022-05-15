#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : Liu Kun
# date   : 2022-05-15 22:48:16

# 导入所需的依赖库
import unittest
from typing import Optional, List

# 题目编号: 2
# 题目名称: 两数相加
# 题目难度: Medium

# 知识点: 递归, 链表, 数学

# 题目详情:
"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例 1：
https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/02/addtwonumber1.jpg
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例 2：
输入：l1 = [0], l2 = [0]
输出：[0]

示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

提示：
每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零
"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class ListNode:

    def __init__(self, val=0, next_one=None):
        """ 修改 next 为 next_one 来规避python内置函数 next() """
        self.val = val
        self.next_one = next_one


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        时间复杂度：O(1)，其实就是顺序执行。
        空间复杂度：O(N)，其中 N 是链表中的元素数量。主要为链表的开销。
        :param l1: 非空的链表形式表示的数字A
        :param l2: 非空的链表形式表示的数字B
        :return: 非空的链表形式表示的数字A+B的结果
        """
        dummy = curr = ListNode()
        carry = 0  # 进位
        while l1 or l2:
            # 补零
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            # 求和
            total = x + y + carry
            # 除10取余 作为 当前位
            curr.next_one = ListNode(total % 10)
            # 和数指针 向高位移动
            curr = curr.next_one
            # 除10取整 作为 进位 由于 0 <= Node.val <= 9 因此进位不是 0 就是 1
            carry = total // 10
            # 两数指针 向高位移动
            if l1: l1 = l1.next_one
            if l2: l2 = l2.next_one
        # 如果进位不为0 则相加后位数增加
        if carry:
            curr.next_one = ListNode(carry)
        # 从链表头开始逆序返回
        return dummy.next_one


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    def doList2ListNode(self, values: List[int]) -> Optional[ListNode]:
        """
        为了测试方便将 List 转为 ListNode
        :param values: List
        :return: ListNode
        """
        # 便于输出使用
        o = curr = ListNode()
        size = len(values)  # 避免最后接0
        for i, val in enumerate(values):
            curr.val = val
            if i + 1 < size:
                curr.next_one = ListNode()
                curr = curr.next_one
        return o

    def doListNode2List(self, obj: Optional[ListNode]) -> List[int]:
        """
        为了测试方便将 ListNode 转为 List
        :param obj: ListNode
        :return: List
        """
        curr = obj
        o = list()
        while True:
            o.append(curr.val)
            # 移动指针
            curr = curr.next_one
            # 退出条件
            if not curr: break
        return o

    # 请设计一些测试用例来验证
    def test_case_1(self):
        result = self.inst.addTwoNumbers(self.doList2ListNode([2, 4, 3]), self.doList2ListNode([5, 6, 4]))
        self.assertEqual([7, 0, 8], self.doListNode2List(result))

    def test_case_2(self):
        result = self.inst.addTwoNumbers(self.doList2ListNode([0]), self.doList2ListNode([0]))
        self.assertEqual([0], self.doListNode2List(result))

    def test_case_3(self):
        result = self.inst.addTwoNumbers(self.doList2ListNode([9, 9, 9, 9, 9, 9, 9]), self.doList2ListNode([9, 9, 9, 9]))
        self.assertEqual([8, 9, 9, 9, 0, 0, 0, 1], self.doListNode2List(result))


if __name__ == "__main__":
    unittest.main()
