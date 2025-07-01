import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        extracted_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        left, right = 0, len(extracted_string) - 1
        
        while left <= right:
            if extracted_string[left] != extracted_string[right]:
                return False
            else:
                right -= 1
                left += 1
        return True