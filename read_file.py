
def read_file(l, file_name):
    with open(file_name) as f:
        for i in range(l): 
            lines = [next(f) for x in range(1)]
            lines = lines[0][1:-2].split(',')            
    f.close()
    return lines


lenght = 2
for asd in range(1, lenght+1, 1):
    print(asd, ' ========================================')
    lines_1 =read_file(asd, "output.txt")
    print(lines_1[1])



















