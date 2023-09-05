from datetime import datetime
from warning_light import WarningLight

class Palindrome(WarningLight):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return service_threshold_date < datetime.today().date() or self.engine_should_be_serviced()
