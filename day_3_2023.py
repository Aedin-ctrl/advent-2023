imput_code = """(paste input here)"""

# part 1
def part1(imput_code):
    total = 0
    num_start = ''
    num_end = ''
    for i, chr in enumerate(imput_code):
        if chr in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and num_start == '':
            num_start = i
        elif num_start != '' and chr in ['.', '*', '#', '%', '=', '-', '/', '+', '$', '@', '&', '\n']:
            num_end = i
            
            num = imput_code[num_start:num_end]
            
            box = []
            top = num_start < imput_code.index("\n")
            lft = num_start % (imput_code.index("\n") + 1) == 0
            rgt = num_end == (imput_code.index("\n"))
            bot = i + imput_code.index("\n") + 1 > len(imput_code)
            
            if not top:
                box.extend(imput_code[(num_start - ((not lft) * 1)) - (imput_code.index("\n") + 1): (num_end + ((not rgt) * 1)) - (imput_code.index("\n") + 1)])
            box.extend(imput_code[(num_start - ((not lft) * 1)): num_end + ((not rgt) * 1)])
            if not bot:
                box.extend(imput_code[(num_start - ((not lft) * 1)) + (imput_code.index("\n") + 1): (num_end + ((not rgt) * 1)) + (imput_code.index("\n") + 1)])
                
            for i in box:
                if i in ['*', '#', '%', '=', '-', '/', '+', '$', '@', '&']:
                    total += int(num)
            
            num_start = ''
            num_end = ''
    return total
        
# part 2
def part2(imput_code):
    grid = imput_code.splitlines()
    total = 0
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch != "*":
                continue

            cs = set()
            
            for cr in [r - 1, r, r + 1]:
                for cc in [c - 1, c, c + 1]:
                    if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[cr]) or not grid[cr][cc].isdigit():
                        continue
                    while cc > 0 and grid[cr][cc - 1].isdigit():
                        cc -= 1
                    cs.add((cr, cc))
                    
            if len(cs) != 2:
                continue

            ns = []

            for cr, cc in cs:
                s = ""
                while cc < len(grid[cr]) and grid[cr][cc].isdigit():
                    s += grid[cr][cc]
                    cc += 1
                ns.append(int(s))
            
            total += ns[0] * ns[1]
    return(total)
    
print("part 1", part1(imput_code))
print("part 2", part2(imput_code))
