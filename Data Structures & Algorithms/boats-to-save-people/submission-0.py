class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start = 0
        end = len(people)-1
        boats = 0
        while start <= end:
            if people[start] + people[end] > limit:
                boats += 1
                end -= 1
            else:
                boats += 1
                start += 1
                end -= 1

        return boats