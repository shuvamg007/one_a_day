class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        def bin_search(a, l, h):
            nonlocal arr
            if not arr:
                arr.append(a)
                return len(arr)

            while l < h:
                mid = (l + h) // 2
                if a < arr[mid]:
                    h = mid
                else:
                    l = mid + 1

            if l == len(arr):
                arr.append(a)
            else:
                arr[l] = a
            return l + 1

        arr = []
        ret = []
        for i in obstacles:
            ret.append(bin_search(i, 0, len(arr)))

        return ret
