class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        for i in range((len(x_str))//2):
            if x_str[i] != x_str[-(i+1)]:
                print(False)
                return False
        print(True)
        return True
a = Solution()
a.isPalindrome(121)
a.isPalindrome(-121)
a.isPalindrome(10)
a.isPalindrome(3333)
        