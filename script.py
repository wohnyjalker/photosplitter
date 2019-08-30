from PIL import Image
import os
import sys

def print_help():
    print("Takes one argument: .jpg file\nUsage 'python script.py file.jpg'\nTo split all .jpg photos in current directory first:\n'chmod +x runscript' next './runscript'")
    exit()

if (len(sys.argv) < 2) or (len(sys.argv) >= 3):
    print_help()

if (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
    print_help()   

dir_name = 'folder'
counter = 1
file_path = os.getcwd() + '/' + dir_name + '/'
boxes = [(16, 201, 601, 591), (16, 600, 600, 990), (16, 1000, 600, 1390)]

try:
    # Create target Directory
    os.mkdir(dir_name)
    print("Directory", dir_name,  "created.") 
except FileExistsError:
    print("Directory", dir_name, "already exists.")
    pass

try:
    im = Image.open(sys.argv[1])
except FileNotFoundError:
    print(sys.argv[1], "no such file.")
    exit()

source_file_name = sys.argv[1].replace('.jpg','')
print("Source file:", sys.argv[1])

for box in boxes:
    name = source_file_name + "_img" + str(counter) + ".jpg"
    image_final_path = file_path + name

    region = im.crop(box)
    image_final = Image.new("RGB", (585, 390), 0)
    image_final.paste(region)
    image_final.save(image_final_path, quality=95)
    print(name, "saved.")
    counter += 1

