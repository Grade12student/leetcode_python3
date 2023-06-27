class UndergroundSystem:
    def __init__(self):
        self.check_ins = {}  # {id: (start_station, start_time)}
        self.travel_times = {}  # {(start_station, end_station): [travel_times]}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_ins[id]
        end_station = stationName
        travel_time = t - start_time

        if (start_station, end_station) not in self.travel_times:
            self.travel_times[(start_station, end_station)] = []

        self.travel_times[(start_station, end_station)].append(travel_time)
        del self.check_ins[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel_times = self.travel_times[(startStation, endStation)]
        return sum(travel_times) / len(travel_times)
