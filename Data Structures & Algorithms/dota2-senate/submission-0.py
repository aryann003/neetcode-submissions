from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()

        idx = len(senate)

        for i in range(len(senate)):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + idx)
            else:
                dire.append(dire[0] + idx)

            radiant.popleft()
            dire.popleft()

        return "Dire" if not radiant else "Radiant"
