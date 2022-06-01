#!/usr/bin/env python3

# BoBoBo

from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        search_map = {}
        for i in range(len(nums)):
            t = target - nums[i]
            if t in search_map:
                return [i, search_map[t]]
            else:
                search_map[nums[i]] = i

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        sx = []
        while x > 0:
            num = x % 10
            sx.append(num)
            x = x // 10

        for i in range(len(sx)//2):
            if sx[i] != sx[len(sx) - i - 1]:
                return False
        return True

    def romanToInt(self, s: str) -> int:
        trans_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        num = 0
        l = len(s)
        i = l - 1
        while i >= 0:
            c = s[i]
            t_num = trans_dict[c]
            num += t_num
            i -= 1

            if c == 'V' or c == 'X':
                if i >= 0 and s[i] == 'I':
                    num -= 1
                    i -= 1
            elif c == 'L' or c == 'C':
                if i >= 0 and s[i] == 'X':
                    num -= 10
                    i -= 1
            elif c == 'D' or c == 'M':
                if i >= 0 and s[i] == 'C':
                    num -= 100
                    i -= 1
        return num


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("MCMXCIV"))
