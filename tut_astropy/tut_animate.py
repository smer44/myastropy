#tutorial how to display animation with fits files
import glob
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import matplotlib.animation as ani

path = "img/"
files = glob.glob(path + "*.fits")# returns list of strings, in alphabetical order
fnumber = 0
fsize = len(files)
fname = files[fnumber%fsize]
data = fits.open(fname)
arr = data[0].data

fig = plt.figure()
im = plt.imshow(arr, cmap = "gray",animated= True)

def update_img(frame):
    global fsize, im
    fname = files[frame % fsize]
    data = fits.open(fname)
    arr = data[0].data
    arr[frame % fsize+5,:]= 30000
    im.set_array(arr)
    return [im]

#anim = ani.FuncAnimation(fig, update_img, interval = 50, blit=True)
anim = ani.FuncAnimation(fig, update_img, interval = 50)
plt.colorbar()
plt.show()



#plt.show()
