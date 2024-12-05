def find_word(to_find,current_pos, walk, text, maxX,maxY):
    x = current_pos[0]
    y = current_pos[1]
    for letter in to_find:
        if(x >= maxX or y >= maxY or x< 0 or y<0 or letter != text[y][x]):
            return 0
        x += walk[0]
        y += walk[1]
    return 1
    
def day4(text):
    to_find = 'XMAS'
    text = text.split('\n')
    line_count = len(text)
    char_line = len(text[0])
    char_count = char_line * len(text)
    count = 0
    a = 0
    for y in range(line_count):
        for x in range(char_line):
            if text[y][x] in [to_find[0],to_find[-1]]:
                word = to_find[::-1] if text[y][x] == to_find[-1] else to_find
                count += find_word(word,[x,y],[1,0],text,char_line,line_count)
                count += find_word(word,[x,y],[0,1] ,text,char_line,line_count)
                count += find_word(word,[x,y],[1,-1],text,char_line,line_count)
                count += find_word(word,[x,y],[1,1],text,char_line,line_count)

def day4_2(text):
    to_find = ['MAS','SAM']
    text = text.split('\n')
    line_count = len(text)
    char_line = len(text[0])
    char_count = char_line * len(text)
    count = 0
    a = 0
    for y in range(1, line_count - 1):
        for x in range(1, char_line -1):
            if text[y][x] == 'A' and  f"{text[y-1][x-1]}{text[y][x]}{text[y+1][x+1]}" in to_find and f"{text[y+1][x-1]}{text[y][x]}{text[y-1][x+1]}" in to_find:
                count += 1
    return count

