# 12 Aprilie 2023
"""
https://leetcode.com/problems/simplify-path/description/
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        dirs = [dir for dir in dirs if len(dir) > 0]
        stack = []
        for dir in dirs:
            if dir == '.':
                continue
            else:
                if dir != '..':
                    stack.append(dir)
                else:
                    if len(stack) == 0:
                        stack.append('/')
                    stack.pop()
        return '/'+"/".join(stack[::-1])


if __name__ == '__main__':
    sol = Solution()
    path = "/a/../../b/../c//.//"   # output: /c
    dirs = path.split('/')
    dirs = [dir for dir in dirs if len(dir) > 0]
    print(dirs)
    print(sol.simplifyPath(path))
