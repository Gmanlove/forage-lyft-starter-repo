from datetime import datetime
from engine import Engine

class Glissade(Engine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return service_threshold_date < datetime.today().date() or self.engine_should_be_serviced(60000)
