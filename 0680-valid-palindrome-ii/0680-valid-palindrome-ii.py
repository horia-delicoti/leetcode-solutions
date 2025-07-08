def checkPalindrom(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        right -= 1
        left += 1
    return True

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                if checkPalindrom(s, left+1, right):
                    left += 1
                elif checkPalindrom(s, left, right - 1):
                    right -= 1
                else:
                    return False
            right -= 1
            left += 1
        return True