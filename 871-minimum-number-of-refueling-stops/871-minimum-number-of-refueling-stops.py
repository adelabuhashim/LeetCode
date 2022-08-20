class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        result = 0
        stations.sort(key = lambda x : x[1], reverse = True)
        print(stations)
        while startFuel < target:
            for i in range(len(stations)):
                if stations[i][0] <= startFuel:
                    startFuel += stations[i][1]
                    result += 1
                    stations.pop(i)
                    break
            else:
                return -1
        return result



 