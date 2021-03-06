# -*- coding:utf-8 -*-
"""
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,
但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
"""


"""
思路：循环1到n中的每个数字，对数字每一位对10求余数，判断余数为1，则计数加1
"""
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for i in range(1, n + 1):
            while i > 0:
                mod = i % 10
                i = i // 10
                if mod == 1:
                    count += 1
        return count


# 需要进一步理解
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        cur = n % 10
        high, low = n // 10, 0
        digit, count = 1, 0
        while high != 0 or cur != 0:
            if cur == 0:
                count = high * digit + count
            if cur == 1:
                count += high * digit + low + 1
            if cur > 1:
                count += (high + 1) * digit
            low = low + cur * digit
            cur = high % 10
            high = high // 10
            digit = digit * 10
        return count

if __name__ == '__main__':
    Solution = Solution()
    print(Solution.NumberOf1Between1AndN_Solution(55))
