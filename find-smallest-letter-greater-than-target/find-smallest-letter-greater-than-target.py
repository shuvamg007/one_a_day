class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        min_l, max_l = letters[0], letters[-1]        
        letters = set(letters)

        if max_l <= target:
            return min_l

        for l in letters:
            if target < l < max_l:
                max_l = l

        return max_l