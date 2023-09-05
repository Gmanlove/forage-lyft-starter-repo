class Engine:
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self, mileage_threshold):
        return self.current_mileage - self.last_service_mileage > mileage_threshold
