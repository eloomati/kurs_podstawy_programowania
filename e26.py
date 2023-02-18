import winsound

frequency = 100 # 500Hz
duration = 500 # 0.5 s

for frequency in range(100,1500, 100):
    winsound.Beep(frequency, duration)