class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, total_gas, curr_gas = 0,0,0

        for i in range(len(gas)):
            n = gas[i] - cost[i]
            curr_gas += n
            total_gas += n
            if curr_gas < 0:
                curr_gas = 0
                start = i+1

        return start if total_gas >= 0 else -1
        