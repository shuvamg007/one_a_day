class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions)

        op = []
        for spell in spells:
            tgt = math.ceil(success / spell)
            l, r = 0, len(potions) - 1
            while l <= r:
                mid = (l+r) // 2

                if tgt > potions[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

            op.append(len(potions) - l)

        return op
