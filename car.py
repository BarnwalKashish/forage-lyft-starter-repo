from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass

class CarPart:
    def __init__(self, name, service_criteria):
        self.name = name
        self.service_criteria = service_criteria

    def get_name(self):
        return self.name

    def get_service_criteria(self):
        return self.service_criteria

class Engine(CarPart, ABC):
    def __init__(self, name, service_criteria):
        super().__init__(name, service_criteria)

class CarModel:
    def __init__(self, name):
        self.name = name
        self.car_parts = []

    def add_car_part(self, car_part):
        self.car_parts.append(car_part)

    def remove_car_part(self, car_part):
        self.car_parts.remove(car_part)

    def get_car_parts(self):
        return self.car_parts

class CarServiceComponent:
    def __init__(self):
        self.car_models = []

    def check_service_needed(self, car_model):
        # Implement the logic to check service needs based on the car parts
        pass
