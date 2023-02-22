asteroids = {
    "1212": {"date": "12.12.12", "scientist": "john, james", "AU": 3.3},
    "1222": {"date": "12.12.13", "scientist": "john, tom", "AU": 4.3},
    "1232": {"date": "12.12.14", "scientist": "john, usan", "AU": 55.3},
    "1242": {"date": "12.12.15", "scientist": "john, micho", "AU": 1.3}
}

for asteroid, info in asteroids.items():
    print(f"\n{'Asteroida'.upper()}: {asteroid}")
    dt = info['date']
    sc = info['scientist']
    au = info['AU']

    print(f"Data: {dt}")
    print(f"Naukowcy: {sc}")
    print(f"AU: {au}")