import copy
import time
image=\
"""
------
-0000-
-0000-
------
"""

image=\
"""
XXXXXXXXXX
X0X000000X
X000XXXX0X
XXXXX0000X
XX0000XXXX
X00XX0000X
XX00X0XX0X
XXX000XX0X
XXXXXXXXXX
"""

arr = [list(x) for x in image.split()]

def pp(arr):
    return "\n".join("".join (x if x in "0X" else "U"  for x in line) for line in arr)

#print(arr)

def near2d(arr,x,y,xmax,ymax):
    """
    returns points near to the given point in 2d grid, checking bounds
    :param arr: given 2d list
    :param x: x coordinate of given point
    :param y: y coordinate of given point
    :param xmax: size of 2d list along first dimention
    :param ymax: size of 2d list along second dimention
    :return: list of tuples (x,y) of coordinates what are neighbpurs
    """
    ret = []
    if x >0: ret.append((x-1,y))
    if y > 0 : ret.append((x,y-1))
    if x < xmax-1:ret.append((x+1,y))
    if y < ymax - 1: ret.append((x, y+1))
    return ret


def flood_fill_algo(arr,x,y,free = "0"):
    global canvas,text,delay
    xmax = len(arr)
    ymax = len(arr[0])
    farr= copy.deepcopy(arr)
    farr[x][y] = "X"
    pos = [(x,y)]
    count = 0
    while pos:
        next_pos = []
        count+=1
        strcount = str(count)
        for x,y in pos:
            nears=near2d(arr,x,y,xmax,ymax)
            for nx,ny in nears:
                if farr[nx][ny] == free:
                    farr[nx][ny] = strcount
                    next_pos.append((nx,ny))
                    #s=""
                    print(pp(farr))
                    print()
                    #canvas.after(delay,fn)
                    #delay+=500

        pos = next_pos
    return farr



"""
import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root)
canvas.pack()
text=canvas.create_text(50,5,text=pp(arr), anchor = tk.CENTER)

delay = 500

root.mainloop()"""
ret = flood_fill_algo(arr,1,1)


