


def day1(str):
    str = [s.split("   ") for s in str.split("\n")]
    left = []
    right = []
    total = 0
    for s in str:
        left.append(int(s[0]))
        right.append(int(s[1]))
    
    for i in range(len(left)):
        minL = min(left)
        minR = min(right)
        total += abs(minL - minR)
        left.remove(minL)
        right.remove(minR)
    return total

print(day1(str))