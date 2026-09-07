class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize != 0:
            return False

        mp = Counter(hand)
        hand.sort()

        for x in hand:
            if mp[x] == 0:
                continue

            for num in range(x, x + groupSize):
                if mp[num] == 0:
                    return False

                mp[num] -= 1

        return True