class Rover:
    def __init__(self, weight, velocity):
        self.weight = weight
        self.velocity = velocity

    def rover_weight(self):
        print(f"Waga {self.weight} kg")

    def rover_velocity(self):
        print(f"Prędkość {self.velocity} km/h")


class LunarRover(Rover):
    def __init__(self, weight, velocity, sampler_range): #Przeciążanie konstruktora (tworze połąćzenie między konstruktorami)
        super().__init__(weight, velocity)
        self.sampler_range = sampler_range # Teraz ten atrybut jest 'jawny', bo pochodzi z 'jawnego' parametru konstruktora

    def sampler_description(self):
        print(f"Ten łazik posiada próbnik o zasięgu: {self.sampler_range} cm")


rover1 = Rover(200, 10)
rover1.rover_weight()
rover1.rover_velocity()

lunar_roving_vehicle = LunarRover(420, 13, 36)# Teraz wywołujemy sampler_range jawnie z poziomu kolejnego parametru
lunar_roving_vehicle.rover_weight()
lunar_roving_vehicle.rover_velocity()
lunar_roving_vehicle.sampler_description()