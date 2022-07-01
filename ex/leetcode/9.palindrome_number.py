class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        sx = str(x)
        l = len(sx)
        stop = int(l / 2)
        for i in range(l):
            if i > stop:
                break
            if int(sx[i]) != x % 10:
                return False
            x = int(x / 10)

        return True
