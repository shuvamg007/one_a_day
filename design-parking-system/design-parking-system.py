class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.type = [big, medium, small]
        self.ctr = [0, 0, 0]

    def addCar(self, carType: int) -> bool:
        if self.ctr[carType - 1] < self.type[carType - 1]:
            self.ctr[carType - 1] += 1
            return True

        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)