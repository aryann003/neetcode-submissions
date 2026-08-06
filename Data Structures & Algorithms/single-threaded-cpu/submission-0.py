class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        arr = []
        for i in range(len(tasks)):
            arr.append((tasks[i][0],tasks[i][1],i))

        arr.sort()
        heap = []
        ans = []

        time = 0
        i = 0
        while i < len(tasks) or heap:

            if not heap and time < arr[i][0]:
                time = arr[i][0]

            while i < len(tasks) and arr[i][0] <= time:
                enque, process,index = arr[i]      
                heapq.heappush(heap,(process,index))
                i += 1

            process, index = heapq.heappop(heap)
            time += process
            ans.append(index)

        return ans

