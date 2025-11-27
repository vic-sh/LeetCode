class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        if x == 0:
            return True
        elif x < 0 or x % 10 == 0: 
            return False
        else:
            while x > rev:
                rev = rev * 10 + x % 10
                x = x // 10
        return x == rev or (rev // 10) == x

a = Solution()
print(a.isPalindrome(12321))
print(a.isPalindrome(121))
print(a.isPalindrome(-121))
print(a.isPalindrome(10))
print(a.isPalindrome(0))