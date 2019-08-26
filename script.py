from PIL import Image
import os, sys

def print_help():
    print("Takes one argument: .jpg file\nUsage 'python script.py file.jpg'\nTo split all .jpg photos in current directory first:\n'chmod +x runscript' next './runscript'")
    exit()

if (len(sys.argv) < 2) or (len(sys.argv) >= 3):
    print_help()

if (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
    print_help()   

dirName = 'folder'
counter = 1
filePath = os.getcwd() + '/' + dirName + '/'
boxes = [(16, 201, 601, 591), (16, 600, 600, 990), (16, 1000, 600, 1390)]

try:
    # Create target Directory
    os.mkdir(dirName)
    print("Directory", dirName,  "created.") 
except FileExistsError:
    print("Directory", dirName, "already exists.")
    pass

try:
    im = Image.open(sys.argv[1])
except FileNotFoundError:
    print(sys.argv[1], "no such file.")
    exit()

sourceFileName = sys.argv[1].replace('.jpg','')
print("Source file:", sys.argv[1])

for box in boxes:
    name = sourceFileName + "_img" + str(counter) + ".jpg"
    imageFinalPath = filePath + name

    region = im.crop(box)
    imageFinal = Image.new("RGB", (585, 390), 0)
    imageFinal.paste(region)
    imageFinal.save(imageFinalPath, quality=95)
    print(name, "saved.")
    counter += 1

