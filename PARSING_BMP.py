import struct


file_name = 'N.bmp'

with open(file_name, "rb") as f:
     file_data = f.read()

image_width = struct.unpack_from('<i', file_data, 18)[0]
image_height = struct.unpack_from('<i', file_data, 22)[0]
f.close

print(image_width, image_height)

image_file = open(file_name, "rb")

# Blindly skip the BMP header.
image_file.seek(54)

# We need to read pixels in as rows to later swap the order
# since BMP stores pixels starting at the bottom left.
rows = []
row = []
pixel_index = 0

while True:
    if pixel_index == image_width:
        pixel_index = 0
        rows.insert(0, row)
        # if len(row) != 240 * 3:
        #     raise Exception("Row length is not 1920*3 but " + str(len(row)) + " / 3.0 = " + str(len(row) / 3.0))
        row = []
        rowX = []
    pixel_index += 1

    r_string = image_file.read(1)
    g_string = image_file.read(1)
    b_string = image_file.read(1)

    if len(r_string) == 0:
            # This is expected to happen when we've read everything.
            if len(rows) != 240:
                print ("Warning!!! Read to the end of the file at the correct sub-pixel (red) but we've not read 240 rows!")
            break
    
    r = ord(r_string)
    g = ord(g_string)
    b = ord(b_string)

    row.append(b)
    row.append(g)
    row.append(r)

image_file.close()

# Open a file in write mode
file_name = "output1.txt"
with open(file_name, "w") as file:

    print ("Repacking pixels...")
    sub_pixels = []
    for row in rows:
        for sub_pixel in row[2::3]:
            if sub_pixel == 0:
                sub_pixels.append(sub_pixel)
        # Write content to the file
        file.write(str(sub_pixels))
        file.write('\n')
        sub_pixels = []

# File is automatically closed when the 'with' block exits
print ("Packed", len(sub_pixels), "sub-pixels.")    
print(f"{file_name} has been written.")
file.close()

msg = "--- DONE ---"
print(msg)  