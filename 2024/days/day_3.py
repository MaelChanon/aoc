import re
def day3(str):
    total = 0
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, str)
    for s in matches:
        total+= int(s[0]) * int(s[1])
    return total

