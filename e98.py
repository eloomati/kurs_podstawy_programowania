class Walking:
    """Klasa spacerów"""

    def __init__(self, weather, steps, time):
        self.weather = weather
        self.steps = steps
        self.time = time

    def display_weather(self):
        print("Nieprawidłowe dane") if len(self.weather) != 3 else print(f"T: {self.weather[0]} st. C, P: {self.weather[1]}hPa, H: {self.weather[2]} %")

    def meters(self):
        return self.steps * .7

    def change_steps(self, num_of_steps):
        self.steps = num_of_steps

    def increment_steps(self, num_of_steps):
        self.steps += num_of_steps

    def speed(self):
        speed = self.meters() / self.time
        print(f"Szedłeś z prędkością: {speed} m/s")

    def m_to_km(self):
        km = self.meters() / 1000
        if self.meters() < 1000:
            print("Nie przeszedłeś kilometra!")
        else:
            print(f"Przeszedłes {km} km.")

walk0 = Walking((23, 1023, 78), 1000, 2000)
walk1 = Walking((30, 1050, 20), 5000, 2000)
print(walk0.steps)

walk0.steps = 1400 # Zmiana ilośći kroków: bezpośrednia zmiana ztrybutu
print(walk0.steps)

walk0.change_steps(200) # Zmiana ilośći kroków: poprzeez metodę klasy
print(walk0.steps)

walk0.increment_steps(300) # Zmiana ilości kroków: poprzez kolejną metodę klasy
print(walk0.steps)

walk0.speed()
walk0.m_to_km()
walk1.m_to_km()

m = walk0.meters()
s = walk0.steps
t = walk0.time
print(f"Pokonano {s} kroków, czyli {m} metrów w czasie {t} s.")


walk0.display_weather()
walk1.display_weather()