def have_common(a,b) : 
    return any(element in a for element in b)

def check_common(offset, numbers, priorities):
    for i in range (len(numbers)):
        if(numbers[i] in priorities):
            return i + offset;
    return -1
def day_5(txt):
    txt = txt.split('\n\n')
    priorities = {}
    total = 0
    for line in txt[0].split('\n'):
        priority = line.split('|')
        priority = [int(priority[0]),int(priority[1])]
        if(priority[1] not in priorities):
            priorities[priority[1]] = [priority[0]]
        else:
            priorities[priority[1]].append(priority[0])

    for line in txt[1].split('\n'):
        numbers = line.split(',')
        numbers = [int(i) for i in numbers]
        toAdd = numbers[len(numbers)//2]
        for i in range (len(numbers)-1):
            if(numbers[i] in priorities and have_common(priorities[numbers[i]],numbers[i+1:])):
                toAdd = 0
                break
        total += toAdd
    return total






def day_5_2(txt):
    txt = txt.split('\n\n')
    priorities = {}
    total = 0
    for line in txt[0].split('\n'):
        priority = line.split('|')
        priority = [int(priority[0]),int(priority[1])]
        if(priority[1] not in priorities):
            priorities[priority[1]] = [priority[0]]
        else:
            priorities[priority[1]].append(priority[0])

    for line in txt[1].split('\n'):
        numbers = line.split(',')
        numbers = [int(i) for i in numbers]
        toAdd = -1
        end = len(numbers) -1
        for i in range (len(numbers)-1):
            if (numbers[i] not in priorities) : continue
            if(numbers[i] == 29): print('test')
            error_idx = check_common(i +1, numbers[i+1:], priorities[numbers[i]])
            if(numbers[i] in priorities and error_idx != -1):
                while(error_idx != -1):
                    toAdd = len(numbers)//2
                    numbers[i], numbers[error_idx] = numbers[error_idx], numbers[i]
                    error_idx = check_common(i +1, numbers[i+1:], priorities[numbers[i]]) if numbers[i] in priorities else -1
            
        total += 0 if toAdd == -1 else numbers[toAdd]
    return total
