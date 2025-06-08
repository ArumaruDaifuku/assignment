# Problem 2 - Bowling
# Since valid sequence is not defined for this problem, we can assume that the rolls we defined are all valid.
# The rolls will be a string of characters
# "X" = strike, "/" = spare, "-" = miss
 
def bowling_score(rolls):
    def convert_roll(char):
        if char == 'X':
            return 10
        elif char == '-':
            return 0
        else:
            return int(char)
    
    total = 0
    index = 0
    n = len(rolls)
    
    for frame in range(9):
        if index >= n:
            break
        if rolls[index] == 'X':
            if index + 1 < n:
                b1 = convert_roll(rolls[index+1])
            else:
                b1 = 0
            if index + 2 < n:
                if rolls[index+2] == '/':
                    b2 = 10 - b1
                else:
                    b2 = convert_roll(rolls[index+2])
            else:
                b2 = 0
            total += 10 + b1 + b2
            index += 1
        else:
            r1 = convert_roll(rolls[index])
            if index + 1 < n:
                if rolls[index+1] == '/':
                    if index + 2 < n:
                        b_roll = convert_roll(rolls[index+2])
                    else:
                        b_roll = 0
                    total += 10 + b_roll
                    index += 2
                else:
                    r2 = convert_roll(rolls[index+1])
                    total += r1 + r2
                    index += 2
            else:
                total += r1
                index += 1
                
    if index < n:
        if rolls[index] == 'X':
            b1 = convert_roll(rolls[index+1]) if index+1 < n else 0
            b2 = convert_roll(rolls[index+2]) if index+2 < n else 0
            total += 10 + b1 + b2
        else:
            r1 = convert_roll(rolls[index])
            if index + 1 < n:
                if rolls[index+1] == '/':
                    b_roll = convert_roll(rolls[index+2]) if index+2 < n else 0
                    total += 10 + b_roll
                else:
                    r2 = convert_roll(rolls[index+1])
                    total += r1 + r2
            else:
                total += r1
                
    return total
