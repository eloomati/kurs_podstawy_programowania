class Rover:
    def __init__(self, weight, velocity):
        self.weight = weight
        self.velocity = velocity

    def rover_weight(self):
        print(f"Waga {self.weight} kg")

    def rover_velocity(self):
        print(f"Prędkość {self.velocity} km/h")


class LunarRover(Rover):
    def __init__(self, weight, velocity): #Przeciążanie konstruktora (tworze połąćzenie między konstruktorami)
        Rover.__init__(self, weight, velocity)


rover1 = Rover(200, 10)
rover1.rover_weight()
rover1.rover_velocity()

lunar_roving_vehicle = LunarRover(420, 13)
lunar_roving_vehicle.rover_weight()
lunar_roving_vehicle.rover_velocity()