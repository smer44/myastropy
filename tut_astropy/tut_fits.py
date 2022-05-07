# from https://www.youtube.com/watch?v=goH9yXu4jWw&ab_channel=HorizonIITM
import numpy as np
import matplotlib.pyplot as plt

from astropy.io import fits

fname = "example.fits"

data = fits.open(fname)
print(data )
data.info()
# the image information is in the primary block
#HDU -header data unit is a high level FITS file component,
#typically containing data and an association header
print("data[0]", data[0])
print("len(data)", len(data))
print("data[0].header",str(data[0].header).split())


arr = data[0].data + 0.0

print("data[0].data", arr)
print("type(data[0].data)", type(arr))
print("arr.shape", arr.shape)
print("arr.dtype", arr.dtype)

print("np.mean(arr)", np.mean(arr))
print("np.std(arr)", np.std(arr))

#ValueError: 'dl' is not a valid value for name; supported values are
# 'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn',
# 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r',
# 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r',
# 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r',
# 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r',
# 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r',
# 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r',
# 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu',
# 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1',
# 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral',
# 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r',
# 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot',
# 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone',
# 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r',
# 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r',
# 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r',
# 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar',
# 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r',
# 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r',
# 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r',
# 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r',
# 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism',
# 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring',
# 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r',
# 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo',
# 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r',
# 'viridis', 'viridis_r', 'winter', 'winter_r'

#for x in range(len(arr)):
# arr[x,x] = 1600

a = np.min(arr)
arr = (arr-a)/(np.max(arr)-a)*32
#print(arr)

#from matplotlib.colors import LogNorm
plt.imshow(arr, cmap = "gray")
plt.colorbar()
#histogram = plt.hist(arr.flat,bins=500)
plt.show()
"""
from astropy.visualization import make_lupton_rgb

rgb_default = make_lupton_rgb(arr,arr,arr,Q = 10)

plt.imshow(rgb_default,origin = "lower")
plt.show()"""

#units and coordinates

from astropy import units as u
from astropy.coordinates import SkyCoord


