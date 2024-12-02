
def part_1(text):
    seeds = steps = text.split("\n\n")
    seeds = [int(x) for x in seeds[0].split(": ")[1].split(" ")]
    steps = steps[1:]

    for step in steps:
        choices = []
        for choice in step.split("\n")[1:]:
            choices.append([int(x) for x in choice.split(" ")])
        items = len(seeds)
        for i in range(items):
            seed = seeds.pop(0)
            final = True
            for choice in choices:
                if(choice[1]<= seed < choice[1] + choice[2]):
                    final = False
                    seeds.append(choice[0] + seed - choice[1])
            if(final):
                seeds.append(seed)

    min = seeds[0]
    for x in seeds[1:]:
        min = x if min>x else min
    return min


def part_2(text):
    seeds = steps = text.split("\n\n")
    seeds = [int(x) for x in seeds[0].split(": ")[1].split(" ")]
    steps = steps[1:]
    for step in steps:
        choices = []
        for choice in step.split("\n")[1:]:
            choices.append([int(x) for x in choice.split(" ")])
        items = len(seeds)/2
        i = 0
        while(i < items):
            seed = seeds.pop(0)
            offset = seeds.pop(0)
            max_value = seed + offset
            final = True
            for choice in choices:
                if(seed >=choice[1] and max_value <= choice[1]+choice[2]):
                    seeds.append(choice[0] + seed - choice[1])
                    seeds.append(offset)
                    final = False
                    break
                elif(seed<choice[1] and max_value>choice[1]):
                    seeds.insert(0,choice[1] -seed)
                    seeds.insert(0, seed)
                    seeds.insert(0,max_value-choice[1])
                    seeds.insert(0,choice[1])
                    final = False
                    i -= 2
                    break
                elif (seed > choice[1]and seed<choice[1]+choice[2] and max_value > choice[1]+choice[2]):
                    seeds.insert(0, choice[1]+choice[2] - seed)
                    seeds.insert(0, seed)
                    seeds.insert(0, max_value - choice[1] - choice[2])
                    seeds.insert(0, choice[1]+choice[2])
                    final = False
                    i -= 2
                    break
                else:
                    continue
            if(final):
                seeds.append(seed)
                seeds.append(offset)
            i+= 1

    min = seeds[0]
    for i in range(int(len(seeds)/2 )- 1):
        min = seeds[i*2+2] if min > seeds[i*2+2] else min
    return min

