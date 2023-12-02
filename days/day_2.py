import re
from functools import reduce
from operator import mul
def result_1(text):
    BAG = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    lines = text.split('\n')
    valid = True
    final = 0
    for line in lines:
        for key in BAG.keys():
            if(not valid): break
            pattern = re.compile(r'(\d+) '+key)
            for matches in pattern.findall(line):
                if (int(matches) > BAG[key]):
                    valid = False
        if(valid):
            final += int(re.findall(r'(\d+)', line.split(':')[0])[0])
        valid = True
    return final


def result_2(text):
    lines = text.split('\n')
    final = 0
    tmp = []
    colors = ['red','green','blue']
    for line in lines:
        for key in colors:
            pattern = re.compile(r'(\d+) '+key)
            tmp.append(max([int(x) for x in pattern.findall(line)]))
        final += reduce(mul,tmp)
        tmp = []
    return final
