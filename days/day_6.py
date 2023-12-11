import math
def part_1(text):
    text = text.split('\n')
    speedsRaw = text[0].split(':')[1].strip().split(" ")
    speeds = []
    for number in speedsRaw:
        if(number.isnumeric()):
            speeds.append(int(number))

    distancesRaw = text[1].split(':')[1].strip().split(" ")

    distances = []
    for number in distancesRaw:
        if(number.isnumeric()):
            distances.append(int(number))

    numbers = []
    for i in range(len(speeds)):
        delta = speeds[i]**2 -4*distances[i]
        x0 = (-speeds[i] - delta**0.5)/(-2) - 0.00001
        x1 = (-speeds[i] + delta**0.5)/(-2) + 0.00001
        numbers.append(math.ceil(x0) - math.trunc(x1) - 1)
    result =1
    for number in numbers:
        result*=number
    return result

def part_2(text):
    text = text.split('\n')
    speedsRaw = text[0].split(':')[1].strip().split(" ")
    speeds = ''
    for number in speedsRaw:
        if(number.isnumeric()):
            speeds += number
    speeds = int(speeds)
    distancesRaw = text[1].split(':')[1].strip().split(" ")

    distances = ""
    for number in distancesRaw:
        if(number.isnumeric()):
            distances += number
    distances = int(distances)
    numbers = []

    delta = speeds**2 -4*distances
    x0 = (-speeds - delta**0.5)/(-2) - 0.00001
    numbers.append(math.ceil(x0) - math.trunc(x1) - 1)
    result =1
    for number in numbers:
        result*=number
    return result

print(part_2("""Time:        54     94     65     92
Distance:   302   1476   1029   1404"""))