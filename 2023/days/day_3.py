import string
def result_1(text):
    def _isNumber(char):
        return char.isnumeric()

    lines = text.split('\n')
    final = 0

    for y in range (len(lines)):
        i = 0
        while (i<len(lines[y])):
            if(_isNumber(lines[y][i])):
                start = end = i
                i+= 1
                while( i< len(lines[y]) and _isNumber(lines[y][i])):
                    end += 1
                    i += 1
                around = []
                first = start
                last = end
                if(first>0):
                    first -= 1
                    around.append(lines[y][first])
                if(last< len(lines[y]) -1):
                    last += 1
                    around.append(lines[y][last])
                if (y > 0):
                    around.extend(list(lines[y - 1][first:last+1]))
                if (y < len(lines) -1):
                    around.extend(list(lines[y + 1][first:last+1]))
                if any(symbol != '.' for symbol in around):
                    final += int(lines[y][start:end + 1])
            else:
                i+= 1
    return final


def result_2(text):
    lines = text.split('\n')
    final = 0

    for y in range (len(lines)):
        i = 0

        while (i<len(lines[y])):
            if(lines[y][i]  == "*"):
                numbers= []
                startY = 0 if y == 0 else y - 1
                end = i if i == len(lines[y]) - 1 else i + 1
                while(startY <= y +1 and startY <= len(lines[y])):
                    start = 0 if i == 0 else i - 1
                    while(start<=end):
                        if(lines[startY][start].isnumeric()):
                            right = left = start
                            while(left - 1 >= 0 and lines[startY][left -1].isnumeric()):
                                left -= 1
                            while (right + 1 < len(lines[startY]) and lines[startY][right + 1].isnumeric()):
                                right += 1
                            numbers.append(int(lines[startY][left:right+1]))
                            start = right
                        start += 1
                    startY += 1
                if (len(numbers)>1):
                    mult = numbers[0]
                    for num in numbers[1:]:
                        mult *= num
                    final += mult
            i += 1
    return final
