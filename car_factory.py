from datetime import datetime
from engine import Engine
from warning_light import WarningLight

class CarFactory:
    @staticmethod
    def create_capulet_engine(last_service_date, current_mileage, last_service_mileage):
        return Thovex(last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_sternman_engine(last_service_date, warning_light_is_on):
        return Palindrome(last_service_date, warning_light_is_on)

    @staticmethod
    def create_willoughby_engine(last_service_date, current_mileage, last_service_mileage):
        return Glissade(last_service_date, current_mileage, last_service_mileage)
