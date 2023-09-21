import os

# ==============================  BYTES

r_file_path = "my_file.bin"  # FILE FOR READ 

try:
    os.remove(r_file_path)
    a = 0 # DUUMY
except OSError as e:
    with open(r_file_path, "w") as fc:
        print(f"File created {r_file_path}: {e}")
    fc.close()

def read_file(l, file_name):
    with open(file_name) as f:
        for i in range(l): 
            lines = [next(f) for x in range(1)]
    f.close()
    lines = lines[0][1:-3].split(',')
    return lines

def colour(R,G,B): # Convert RGB888 to RGB565
    return (((G&0b00011100)<<3) +((B&0b11111000)>>3)<<8) + (R&0b11111000)+((G&0b11100000)>>5)

def write_file(content):
    file_path1 = "example.txt"
    with open(file_path1, "a") as fc:
        for c in range(0, 204, 3):
            colors = int(content[c]),int(content[c+1]),int(content[c+2])
            # print(colors)            
            # converts.append(colors)     
            fc.write(str(colors) + ',')
        # print(' --')
        fc.write("\n")
    fc.close()    


# with open("output.txt") as f:
#     for i in range(1, 97, 1): 
#         lines = [next(f) for x in range(1)]
#         lines = lines[0][1:-3].split(',')
#         # print(i)
#         write_file(lines)
#     f.close()    




num = 255
 
# Open file in binary write mode
binary_file = open(r_file_path, "wb")
 
# Write bytes to file
num_bytes = num.to_bytes(1, 'big')
binary_file.write(num_bytes)
 
# Close file
binary_file.close()




# ==============================  STR


# r_file_path = "example.txt"  # Укажите путь к файлу, который вы хотите удалить

# try:
#     os.remove(r_file_path)
#     # print(f"Файл {file_path} успешно удален.")
# except OSError as e:
#     with open(r_file_path, "w") as fc:
#         print(f"File created {r_file_path}: {e}")
#     fc.close()

# def read_file(l, file_name):
#     with open(file_name) as f:
#         for i in range(l): 
#             lines = [next(f) for x in range(1)]
#     f.close()
#     lines = lines[0][1:-3].split(',')
#     return lines


# def colour(R,G,B): # Convert RGB888 to RGB565
#     return (((G&0b00011100)<<3) +((B&0b11111000)>>3)<<8) + (R&0b11111000)+((G&0b11100000)>>5)


# def write_file(content):
#     file_path1 = "example.txt"
#     with open(file_path1, "a") as fc:
#         for c in range(0, 204, 3):
#             colors = colour(int(content[c]),int(content[c+1]),int(content[c+2]))
#             # print(colors)            
#             # converts.append(colors)     
#             fc.write(str(colors) + ',')
#         # print(' --')
#         fc.write("\n")
#     fc.close()    


# with open("output.txt") as f:
#     for i in range(1, 97, 1): 
#         lines = [next(f) for x in range(1)]
#         lines = lines[0][1:-3].split(',')
#         # print(i)
#         write_file(lines)
#     f.close()    



