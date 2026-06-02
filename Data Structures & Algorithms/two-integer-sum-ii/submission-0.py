class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1
        while start < end:
            num = numbers[start] + numbers[end]
            if num == target:
                return [start+1,end+1]
            elif num > target:
                end -= 1
            else:
                start += 1
        