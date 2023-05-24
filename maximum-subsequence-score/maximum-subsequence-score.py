class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = list(zip(nums1, nums2))
        pairs.sort(key=lambda x: -x[1])

        sum_val = [x[0] for x in pairs[:k]]
        tot_sum = sum(sum_val)
        answer = tot_sum * pairs[k-1][1]

        heapq.heapify(sum_val)
        for i in range(k, len(pairs)):
            top_val = heapq.heappop(sum_val)
            
            tot_sum -= top_val
            tot_sum += pairs[i][0]
            heapq.heappush(sum_val, pairs[i][0])

            answer = max(answer, tot_sum * pairs[i][1])

        return answer