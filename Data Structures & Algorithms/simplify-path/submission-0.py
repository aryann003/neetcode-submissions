class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        stack = []
        for pth in paths:
            if pth == "" or pth == ".": 
                continue
            elif pth == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(pth)
        ans = "/" + "/".join(stack)
        return ans

            

