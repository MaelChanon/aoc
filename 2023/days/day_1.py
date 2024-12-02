def result_1(text):
    lines = text.split('\n')
    final = 0
    for line in lines:
        first = False
        last = False
        for i in range (len(line)):
            if (first and last):
                break
            if (not first and line[i].isnumeric()):
                first = line[i]
            if (not last and line[len(line) - i - 1].isnumeric()):
                last = line[len(line) - i - 1]
        print(first + last)
        final += int(first + last)
    return final

def result_2(text):
    def get_number(string,position,start):
        numbers = {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9
        }
        if (start and string[position].isnumeric()):
            return int(string[position])
        if (not start and string[position - 1].isnumeric()):
            return int(string[position -1])
        for i in range(3,6):
            if(start):
                sub = string[position : position + i]
            else:
                sub = string[position - i : position]
                print(string[position - i : position])
            if (sub in numbers):
                return numbers[sub]
        return -1

    lines = text.split('\n')
    final = 0
    for line in lines:
        first = False
        last = False
        tmp = -1
        for i in range(len(line)):
            if (first and last):
                break
            tmp = get_number(line,i,True)
            if (not first and tmp > 0):
                first = tmp * 10
            tmp = get_number(line,len(line)-i,False)
            if (not last and tmp > 0):
                last = tmp

        final += first + last
    return final