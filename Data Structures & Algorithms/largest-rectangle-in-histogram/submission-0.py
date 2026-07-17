class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        r = [n] * n
        l = [-1] * n
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                r[stack[-1]] = i
                stack.pop()
            stack.append(i)
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                l[i] = stack[-1]

            stack.append(i)


        max_area = 0
        for i in range(n):
            width = r[i] - l[i] -1 
            area = heights[i] * width
            max_area = max(max_area,area)

        return max_area 


         