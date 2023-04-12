class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = list()
        dirs = path.split('/')

        for _dir in dirs:
            if _dir == '.' or _dir == '':
                continue
            elif _dir == '..':
                if stack:
                    stack.pop()

            else:
                stack.append(_dir)

        return '/' + '/'.join(stack)