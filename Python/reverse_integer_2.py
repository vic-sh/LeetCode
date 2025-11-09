class Solution:
    def reverse(self, x: int) -> int:
        minus = 1
        if x < 0:
            minus = -1
            x = -x
        y = x % 10
        while x // 10 > 0:
            x = x // 10
            y = y*10 + x % 10
        if y < -2**31 or y > 2**31-1:
            print(0)
            return 0
        y = minus * y
        print(y)
        return y

a = Solution()
a.reverse(123)
a.reverse(321)
a.reverse(-123)
a.reverse(120)