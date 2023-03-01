class Rover:
    def __init__(self, weight, velocity):
        self.weight = weight
        self.velocity = velocity

    def rover_weight(self):
        print(f"Waga {self.weight} kg")

    def rover_velocity(self):
        print(f"Prędkość {self.velocity} km/h")

class Sampler:
    def __init__(self, sampler_range=36):
        self.sampler_range = sampler_range

    def sampler_description(self):
        print(f"Ten łazik posiada próbnik o zasięgu: {self.sampler_range} cm")



class LunarRover(Rover):
    def __init__(self, weight, velocity):
        super().__init__(weight, velocity)
        self.sampler = Sampler()



rover1 = Rover(200, 10)
rover1.rover_weight()
rover1.rover_velocity()

lunar_roving_vehicle = LunarRover(420, 13)
lunar_roving_vehicle.rover_weight()
lunar_roving_vehicle.rover_velocity()

sampler1 = Sampler()
sampler1.sampler_description()

lunar_roving_vehicle.sampler.sampler_description()