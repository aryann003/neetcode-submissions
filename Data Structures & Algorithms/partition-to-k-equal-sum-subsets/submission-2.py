class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        if len(nums) < k:
            return False

        total = sum(nums)

        if total % k != 0:
            return False

        target = total // k

        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        sides = [0] * k

        def solve(index):

            if index == len(nums):
                return True

            for j in range(k):

                # Don't put the number if it exceeds target
                if sides[j] + nums[index] > target:
                    continue

                # Skip buckets having the same sum
                if j > 0 and sides[j] == sides[j - 1]:
                    continue

                # Choose
                sides[j] += nums[index]

                # Explore
                if solve(index + 1):
                    return True

                # Undo
                sides[j] -= nums[index]

                # If this bucket was empty,
                # don't try other empty buckets
                if sides[j] == 0:
                    break

            return False

        return solve(0)