from PIL import Image
import tkinter
import tkinter.filedialog

AA_NAME = input("What is the name of the ASCII art?:")


while len(AA_NAME) == 0:
    print("Please set a name!")
    AA_NAME = input("What is the name of the ASCII art?:")

Filepass = tkinter.filedialog.askdirectory(title="Which file do you want to put it in?") + '/'

file_name = tkinter.filedialog.askopenfilename(filetypes = [("Image file", ".bmp .png .jpg .tif"), ("Bitmap", ".bmp"), ("PNG", ".png"), ("JPEG", ".jpg"), ("Tiff", ".tif") ])

img= Image.open(file_name)

size=img.size

width = img.width

height = img.height

def change_grayscale(r,g,b,a=255):
    grey = int((0.2989 * r + 0.5870 * g + 0.1140 * b))
    if a != 0:
        if grey > 255:
            return 255
        else:
            return grey
    else:
        return 255

AA_Reduction = int(input("How big is it?\nPlease specify the width:"))

AA_Reduction = width/AA_Reduction

img_resize = img.resize((int(img.width // AA_Reduction), int(img.height // AA_Reduction)))

img= img_resize

size_resize=img_resize.size
'''
width = img_resize.width

height = img_resize.height
'''
AA_result = ""

colorset = "MWN$@%#&B89EGA6mK5HRkbYT43V0JL7gpaseyxznocv?jIftr1li*=-~^`':;,. "

for y in range(size_resize[1]):
    AA_result += "\n"
    for x in range(size_resize[0]):
        xy=(x,y)
        r,g,b=img.getpixel((xy))                        #RGB形式の場合はここと1つ下の行の#を消してください
        GW_pixel = change_grayscale(r,g,b)
        #r,g,b,a=img.getpixel((xy))                     #RGBA形式の場合はここと1つ下の行の#を消してください
        #GW_pixel = change_grayscale(r,g,b,a)
        AA_result += colorset[GW_pixel //4] *2
        print(x,y)

#print(AA_result)

with open(Filepass + str(AA_NAME) + ".txt", mode="w") as f:
    f.write(AA_result)