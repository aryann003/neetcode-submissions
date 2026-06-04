class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = []

        for i in range(len(speed)):
            time = (target-position[i]) / speed[i]
            car.append((position[i],time))

        car.sort(reverse = True) #on basics of positons

        max_time = 0
        fleets = 0;
        for pos,time in car:
            if time > max_time:
                max_time = time
                fleets += 1
        return fleets
            

