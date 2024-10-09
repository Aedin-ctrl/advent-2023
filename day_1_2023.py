imput_code = """(paste input here)"""

# part 1
def part1(imput_code):
    total = 0
    for i in imput_code.split("\n"):
        hold = ''.join([char for char in i if char.isdigit()])
        total += (int(f"{hold[0]}{hold[-1]}"))
    print(total)

# part 2
def part2(imput_code):
    values = {
        "one": "1", 
        "two": "2", 
        "three": "3", 
        "four": "4", 
        "five": "5", 
        "six": "6", 
        "seven": "7", 
        "eight": "8", 
        "nine": "9"
        }
    total = []
    for i in imput_code.split("\n"):
        print(i, "base")
        hold = []
        print(hold, "hold")
        for j in range(len(i)):
            if i[j].isdigit():
                hold.append(i[j])
            else:
                for l in values.keys():
                    if i[j:].startswith(l):
                        hold.append(str(values[l]))         
        total.append(int(f"{hold[0]}{hold[-1]}"))
        print(f"{hold}, {hold[0]}{hold[-1]}")
    return sum(total)
                
print(part1(imput_code))
print(part2(imput_code))
