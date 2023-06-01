class UndergroundSystem:

    def __init__(self):
        self.id_hmap = defaultdict(list)
        self.station = defaultdict(dict)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id_hmap[id].append((stationName, t))

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_st, start_time = self.id_hmap[id][-1]
        if stationName in self.station[start_st]:
            self.station[start_st][stationName].append(t - start_time)
        else:
            self.station[start_st][stationName] = [t - start_time]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.station[startStation][endStation]
        return sum(times) / len(times)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)