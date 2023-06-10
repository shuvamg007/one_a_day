class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        l, r = maxSum // n, maxSum
        max_l, max_r = index, n - index - 1


        while l <= r:
            mid = (l + r) // 2
            sum_val = mid 

            tot = (mid * (mid-1)) // 2
            # print(sum_val, tot)
            # sum_val += tot

            if mid > max_l:
                sub = ((mid - max_l) * (mid - max_l - 1)) // 2
                sum_val += (tot - sub)
            else:
                sum_val += (tot + max_l - mid + 1)
            # print(sum_val)

            if mid > max_r:
                sub = ((mid - max_r) * (mid - max_r - 1)) // 2
                sum_val += (tot - sub)
            else:
                sum_val += (tot + max_r - mid + 1)

            # print(sum_val, l, r)
            # print()

            if sum_val == maxSum:
                return mid

            elif sum_val < maxSum:
                l = mid + 1

            else:
                r = mid - 1

        return l - 1
