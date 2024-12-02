def part_1(text):
    text = text.replace("  ", " 0")
    lines = text.split("\n")
    total = 0
    for line in lines:
        winning,cards = [x.strip().split(" ") for x in line.split(':')[1].split("|")]
        points = 0
        for card in cards:
            if(card in winning):
                points = 1 if points == 0 else points*2
        total += points

    return total

def part_2(text):
    text = text.replace("  ", " 0")
    lines = text.split("\n")
    total = 0
    double = [0 for i in range(len(lines))]
    count = [1 for i in range(len(lines))]
    for i in range(len(lines)):
        winning,cards = [x.strip().split(" ") for x in lines[i].split(':')[1].split("|")]
        for card in cards:
            if(card in winning):
                double[i] += 1
    for i in range(len(double)):
        recur = [i + y for y in range(1,double[i] +1)]
        for y in recur:
            count[y] += 1*count[i]
    for i in count:
        total += i
    return total
