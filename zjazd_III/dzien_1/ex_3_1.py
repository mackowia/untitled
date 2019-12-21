class ElectricCar:
    def __init__(self, max_range):
        self.max_range = max_range
        self._total_distance = 0   # " _ "(przed total_distance) nie pokaże uzytkownikowi tego wiersza

    def car_drive(self, distance):
        if distance > self.max_range - self._total_distance:
            #nie dojedziemy tak daleko bez ładowania
            available_distance = self.max_range - self._total_distance
            self._total_distance += available_distance
            return available_distance
        else:
            self._total_distance += distance
            return distance

    def charge (self):
        self._total_distance = 0

def test_electric_car_init():
    e = ElectricCar(100)
    assert e.max_range == 100

def test_electric_car_drive_within_range():
    e = ElectricCar(100)
    assert e.drive(80) == 80
    assert e.drive(20) == 20

def test_electric_car_drive_above_range():
    e = ElectricCar(400)
    assert e.drive(420) == 400

def test_electric_car_drive_above_range_several_parst():
    e = ElectricCar(100)
    assert e.drive(70) == 70
    assert e.drive(50) == 30
    assert e.drive(20) == 0

def test_electric_car_charge():
    e = ElectricCar(100)
    e.drive(100)
    e.charge()
    assert e.drive(120) == 100
