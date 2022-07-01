class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                  'M': 1000}
        l = len(s)
        skip = False
        num = 0
        for i in range(l):
            if skip:
                skip = False
                continue

            v = values[s[i]]
            if i+1 < l:
                if v < values[s[i+1]]:
                    v = values[s[i+1]] - v
                    skip = True

            num = num + v

        return num
