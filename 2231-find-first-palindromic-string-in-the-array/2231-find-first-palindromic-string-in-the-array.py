def checkPalindrome(word):
    left, right = 0, len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False
        else:
            right -= 1
            left += 1
    return True

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if checkPalindrome(word):
                return word
        return ""
