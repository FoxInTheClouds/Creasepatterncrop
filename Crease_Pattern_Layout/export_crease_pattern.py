from PIL import Image
from timeit import default_timer as timer
import math
import os

start = timer()

background_colors=[(255,255,255,255),(249,249,249,255),(230,230,230,255),(245,245,245,255),(244,244,244,255)]

def isolate_image(im, remove_middle):
    im_array=list(im.getdata())
    width,height=im.size
    top_row=-1
    bottom_row=height
    columns=[False] * width
    current_row=-1
    wrong_row=False
    for index, item in enumerate(im_array):
        if current_row != (math.floor(index / width)):
            current_row=(math.floor(index / width))
            if wrong_row==True:
                bottom_row=height
            elif bottom_row == height:
                bottom_row=current_row -1
            wrong_row=False
        if item in background_colors:
            if remove_middle == True:
                im.putpixel(((index - (math.floor(index / width)) * width), math.floor(index / width)),(255,255,255,0))            
        else:
            wrong_row = True
            if top_row == -1:
                top_row = (math.floor(index / width))
            if columns[(index - (math.floor(index / width)) * width)] == False:
                columns[(index - (math.floor(index / width)) * width)] = True
    left_column=0
    left_column_done=False
    right_column=width
    for index, item in enumerate(columns):
        if item == False:
            if left_column_done==False:
                left_column=index + 1
              
            elif right_column == width:
                right_column = index
        else:
            left_column_done=True
            if right_column == width:
                right_column=width
    im.crop((left_column,top_row,right_column,bottom_row)).save(file, "PNG")

directory="inputFolded"
for file in os.listdir(directory):
    im=Image.open(os.path.join(directory,file))
    isolate_image(im, True)
directory="InputCreasePattern"
for file in os.listdir(directory):
    im=Image.open(os.path.join(directory,file))
    isolate_image(im, False)
end=timer()
print("Time: " + str(end - start))