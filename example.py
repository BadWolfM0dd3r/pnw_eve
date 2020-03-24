from random import uniform

def roll_1(my_aircraft_value, en_aircraft_value):
    my_r1_rand_val = my_aircraft_value * uniform(0.45, 1.0)
    my_r1_total_val = my_r1_rand_val * uniform(0.45, 1.0)

    en_r1_rand_val = en_aircraft_value * uniform(0.45, 1.0)
    en_r1_total_val = en_r1_rand_val * uniform(0.45, 1.0)

    my_r1_casualties = en_r1_total_val / 54
    en_r1_casualties = my_r1_rand_val / 38

    return my_r1_total_val, my_r1_casualties, en_r1_total_val, en_r1_casualties

def roll_2(my_aircraft_value, en_aircraft_value):
    my_r2_rand_val = my_aircraft_value * uniform(0.45, 1.0)
    my_r2_total_val = my_r2_rand_val * uniform(0.45, 1.0)

    en_r2_rand_val = en_aircraft_value * uniform(0.45, 1.0)
    en_r2_total_val = en_r2_rand_val * uniform(0.45, 1.0)

    my_r2_casualties = en_r2_total_val / 54
    en_r2_casualties = my_r2_total_val / 38

    return my_r2_total_val, my_r2_casualties, en_r2_total_val, en_r2_casualties

def roll_3(my_aircraft_value, en_aircraft_value):
    my_r3_rand_val = my_aircraft_value * uniform(0.45, 1.0)
    my_r3_total_val = my_r3_rand_val * uniform(0.45, 1.0)

    en_r3_rand_val = en_aircraft_value * uniform(0.45, 1.0)
    en_r3_total_val = en_r3_rand_val * uniform(0.45, 1.0)

    my_r3_casualties = en_r3_total_val / 54
    en_r3_casualties = my_r3_total_val / 38

    return my_r3_total_val, my_r3_casualties, en_r3_total_val, en_r3_casualties

if __name__ == "__main__":
    # Units
    my_aircraft = 160
    en_aircraft = 80

    # Units total value
    my_aircraft_value = my_aircraft * 3
    en_aircraft_value = en_aircraft * 3

    # Summed total rolls
    my_rolls = []
    en_rolls = []

    # Summed total casualties
    my_casualties = []
    en_casualties = []

    # Roll 1
    first_roll = roll_1(my_aircraft_value, en_aircraft_value)

    my_rolls.append(first_roll[0])
    my_casualties.append(first_roll[1])

    en_rolls.append(first_roll[2])
    en_casualties.append(first_roll[3])

    # Roll 2
    second_roll = roll_2(first_roll[0], first_roll[2])

    my_rolls.append(second_roll[0])
    my_casualties.append(second_roll[1])

    en_rolls.append(second_roll[2])
    en_casualties.append(second_roll[3])

    # Roll 3
    third_roll = roll_3(second_roll[0], second_roll[2])

    my_rolls.append(third_roll[0])
    my_casualties.append(third_roll[1])

    en_rolls.append(third_roll[2])
    en_casualties.append(third_roll[3])

    print(f'My rolls: {my_rolls}')
    print(f'My casualties: {my_casualties}')
    print('\--------------------------------/')
    print(f'Enemy rolls: {en_rolls}')
    print(f'Enemy casualties: {en_casualties}')
