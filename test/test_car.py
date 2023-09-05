import unittest
from datetime import datetime
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex

class CarServiceTests(unittest.TestCase):
    def setUp(self):
        today = datetime.today().date()
        self.current_mileage = 0
        self.last_service_mileage = 0

        # Create instances of car types
        self.calliope = Calliope(today, self.current_mileage, self.last_service_mileage)
        self.glissade = Glissade(today, self.current_mileage, self.last_service_mileage)
        self.palindrome = Palindrome(today, False)
        self.rorschach = Rorschach(today, self.current_mileage, self.last_service_mileage)
        self.thovex = Thovex(today, self.current_mileage, self.last_service_mileage)

    def test_battery_should_be_serviced(self):
        self.calliope.current_mileage = 0
        self.glissade.current_mileage = 0
        self.rorschach.current_mileage = 0
        self.thovex.current_mileage = 0

        cars = [self.calliope, self.glissade, self.rorschach, self.thovex]

        for car in cars:
            with self.subTest(car=car):
                self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        self.calliope.current_mileage = 0
        self.glissade.current_mileage = 0
        self.rorschach.current_mileage = 0
        self.thovex.current_mileage = 0

        cars = [self.calliope, self.glissade, self.rorschach, self.thovex]

        for car in cars:
            with self.subTest(car=car):
                self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        self.calliope.current_mileage = 30001
        self.glissade.current_mileage = 60001
        self.rorschach.current_mileage = 60001
        self.thovex.current_mileage = 30001

        cars = [self.calliope, self.glissade, self.rorschach, self.thovex]

        for car in cars:
            with self.subTest(car=car):
                self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        self.calliope.current_mileage = 30000
        self.glissade.current_mileage = 60000
        self.rorschach.current_mileage = 60000
        self.thovex.current_mileage = 30000

        cars = [self.calliope, self.glissade, self.rorschach, self.thovex]

        for car in cars:
            with self.subTest(car=car):
                self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()
