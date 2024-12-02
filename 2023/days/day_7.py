def part_1(text):
    def __isWeaker(hand1,hand2):
        power = ['A','K','Q','T','9','8','7','6','5','4','3','2','J']
        h1 = sorted(hand1[2].values(), reverse=True)
        h2 = sorted(hand2[2].values(), reverse=True)
        v1 = int(h1[0])*10
        v2 = int(h2[0]) * 10
        if(v1 !=50 and v2 != 50):
            v1 = v1 + int(hand1[2]['J']) * 10 if 'J' in hand1[2] else v1
            v2 = v2 + int(hand2[2]['J']) * 10 if 'J' in hand2[2] else v2
            v1 += int(h1[1])
            v2 += int(h2[1])
            return v1 - v2 < 0
        else:
            for i in range(len(hand1[0])):
                if(hand1[0][i] == hand2[0][i]):
                    continue
                else:
                    return power.index(hand1[0][i]) - power.index(hand2[0][i]) > 0
    lines = text.split("\n")
    order = []
    for line in lines:
        line = line.split(" ")
        data = {}
        for char in line[0]:
            if(char in data):
                data[char] += 1
            else:
                data[char] = 1
        hand = [line[0],line[1],data]
        for i in range(len(order) +1):
            if(i == len(order)):
                order.append(hand)
                continue
            if(__isWeaker(hand,order[i])):
                order.insert(i,hand)
                break
    result = 0
    for i in range(len(order)):
        result += int(order[i][1]) * (i+1)
    return result

