class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        possible_dubles = 0
        lenght_ = len(arr) - 1
        
        # Find the number of zeros to be duplicated
        for left in range(lenght_ + 1):
            # Stop when left points beyond the last element in the original list
            # which would be part of the modified list
            if left > lenght_ - possible_dubles:
                break
            
            # Count the zeros
            if arr[left] == 0:
                # Edge case: This zero can't be duplicated. We have no more space,
                # as left is pointing to the last element which could be included
                if left == lenght_ - possible_dubles:
                    arr[lenght_] = 0 # For this zero we just copy it without duplication
                    lenght_ -= 1
                    break
                possible_dubles += 1
        
        # Start backwards from the last element which would be part of new list.
        last = lenght_ - possible_dubles

        # Copy zero twice, and non zero once.
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dubles] = 0
                possible_dubles -= 1
                arr[i + possible_dubles] = 0
            else:
                arr[i + possible_dubles] = arr[i]