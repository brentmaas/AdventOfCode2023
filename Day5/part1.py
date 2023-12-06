def apply_map(item_map, item):
    for destination, source, length in item_map:
        if item >= source and item < source + length:
            return destination + item - source
    return item

with open("Input.txt", "r") as f:
    line = f.readline().strip()
    seeds = [int(s) for s in line[line.index(":")+2:].split(" ")]
    
    f.readline()
    f.readline()
    seed_to_soil = []
    while line := f.readline().strip():
        seed_to_soil.append([int(i) for i in line.split(" ")])
    
    f.readline()
    soil_to_fertilizer = []
    while line := f.readline().strip():
        soil_to_fertilizer.append([int(i) for i in line.split(" ")])
    
    f.readline()
    fertilizer_to_water = []
    while line := f.readline().strip():
        fertilizer_to_water.append([int(i) for i in line.split(" ")])
    
    f.readline()
    water_to_light = []
    while line := f.readline().strip():
        water_to_light.append([int(i) for i in line.split(" ")])
    
    f.readline()
    light_to_temperature = []
    while line := f.readline().strip():
        light_to_temperature.append([int(i) for i in line.split(" ")])
    
    f.readline()
    temperature_to_humidity = []
    while line := f.readline().strip():
        temperature_to_humidity.append([int(i) for i in line.split(" ")])
    
    f.readline()
    humidity_to_location = []
    while line := f.readline().strip():
        humidity_to_location.append([int(i) for i in line.split(" ")])

locations = []
for seed in seeds:
    soil = apply_map(seed_to_soil, seed)
    fertilizer = apply_map(soil_to_fertilizer, soil)
    water = apply_map(fertilizer_to_water, fertilizer)
    light = apply_map(water_to_light, water)
    temperature = apply_map(light_to_temperature, light)
    humidity = apply_map(temperature_to_humidity, temperature)
    location = apply_map(humidity_to_location, humidity)
    locations.append(location)
print(min(locations))