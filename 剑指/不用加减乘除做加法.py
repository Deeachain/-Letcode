# -*- coding:utf-8 -*-

'''
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
'''


class Solution:
    def Add(self, num1, num2):
        # write code here
        a = []
        a.append(num1)
        a.append(num2)
        return sum(a)

if __name__ == '__main__':
    Solution = Solution()
    print(Solution.Add(1, 2))
