class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = list()
        push_idx, pop_idx = 0, 0

        stack.append(pushed[push_idx])
        push_idx += 1

        while push_idx <= len(pushed) and pop_idx < len(popped):

            if stack and stack[-1] == popped[pop_idx]:
                stack.pop()
                pop_idx += 1

            else:
                if push_idx == len(pushed):
                    return False

                stack.append(pushed[push_idx])
                push_idx += 1

        return True if not len(stack) else False