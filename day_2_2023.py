imput_code = """(paste input here)"""

# part 1
def part1(imput_code):
    total = 0
    
    for i in imput_code.split("\n"):
        green = 0
        blue = 0
        red = 0
        
        id_num = int(i[5: i.index(":")])
        i = i[i.index(":") + 2:]
        
        for j in i.split("; "):
            for k in j.split(", "):
                amt = int(k[:k.index(" ")])
                if k[k.index(" ") + 1 :k.index(" ") + 2] == "g":
                    green = max(green, amt)
                if k[k.index(" ") + 1 :k.index(" ") + 2] == "b":
                    blue = max(blue, amt)
                if k[k.index(" ") + 1 :k.index(" ") + 2] == "r":
                    red = max(red, amt)
        if red <= 12 and blue <= 14 and green <= 13:
            total += id_num
    return(total)

# part 2
def part2(imput_code):
    total = 0
    
    for i in imput_code.split("\n"):
        green = 0
        blue = 0
        red = 0
        
        id_num = int(i[5: i.index(":")])
        i = i[i.index(":") + 2:]
        
        for j in i.split("; "):
            for k in j.split(", "):
                amt = int(k[:k.index(" ")])
                if k[k.index(" ") + 1 :k.index(" ") + 2] == "g":
                    green = max(green, amt)
                if k[k.index(" ") + 1 :k.index(" ") + 2] == "b":
                    blue = max(blue, amt)
                if k[k.index(" ") + 1 :k.index(" ") + 2] == "r":
                    red = max(red, amt)
        total += (red * blue * green)
    return(total)

print("part 1", part1(imput_code)) 
print("part 2", part2(imput_code))
