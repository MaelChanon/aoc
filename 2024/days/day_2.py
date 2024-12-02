def day2(str):
    str = [s.split(" ") for s in str.split("\n")]
    valid = 0 
    for lines in str:
        safe =  True
        numbers = [int(s) for s in lines]
        incresing = True if numbers[0] < numbers[1] else False
        d += 1
        for i in range (len(numbers) - 1):
            delta = numbers[i] - numbers[i+1]
            if(incresing and delta >= 0 or not incresing and delta <= 0 or abs(delta) < 1 or abs(delta) > 3):
                safe = False 
                break
        if(safe):
            valid += 1
    return valid
