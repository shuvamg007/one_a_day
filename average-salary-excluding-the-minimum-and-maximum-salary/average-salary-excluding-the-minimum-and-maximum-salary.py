class Solution:
    def average(self, salary: List[int]) -> float:
        min_val, max_val = float('inf'), 0
        total = 0
        
        for i in salary:
            min_val = min(min_val, i)
            max_val = max(max_val, i)
            total += i

        total -= (min_val + max_val)
        return total / (len(salary) - 2)
