def apply_map_ranges(item_map, item_ranges):
    dest_ranges = []
    while len(item_ranges) > 0:
        current_ranges = [item_ranges.pop(0)]
        for destination, source, length in item_map:
            for i in range(len(current_ranges)):
                if current_ranges[i][0] < source + length and source < current_ranges[i][0] + current_ranges[i][1]:
                    item_source, item_length = current_ranges.pop(i)
                    if item_source < source:
                        current_ranges.append((item_source, source - item_source))
                    if item_source + item_length > source + length:
                        current_ranges.append((source + length, item_source + item_length - source - length))
                    dest_ranges.append((destination - source + max(item_source, source), min(item_source + item_length, source + length) - max(item_source, source)))
                    break
        for current_range in current_ranges:
            dest_ranges.append(current_range)
    return dest_ranges

with open("Input.txt", "r") as f:
    line = f.readline().strip()
    seeds = [int(s) for s in line[line.index(":")+2:].split(" ")]
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i+1]))
    
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

soil_ranges = apply_map_ranges(seed_to_soil, seed_ranges)
fertilizer_ranges = apply_map_ranges(soil_to_fertilizer, soil_ranges)
water_ranges = apply_map_ranges(fertilizer_to_water, fertilizer_ranges)
light_ranges = apply_map_ranges(water_to_light, water_ranges)
temperature_ranges = apply_map_ranges(light_to_temperature, light_ranges)
humidity_ranges = apply_map_ranges(temperature_to_humidity, temperature_ranges)
location_ranges = apply_map_ranges(humidity_to_location, humidity_ranges)
print(min([location_range[0] for location_range in location_ranges]))