from astropy.constants import *
from astropy.units import *
import numpy as np


print(G)
print()
print(c)

print(c.to("pc/yr"))
print()

print(2*au.to("km"))
print()
f = g*3*M_sun*100*kg/(2.2*au)**2

print(f)
print()
arr = [1,2,3] * meter
print(repr(arr))
print()
arr = np.array([1,2,3]) * meter

print(repr(arr))

print(repr(arr.unit))
print()
#imperial units, like mile :

cms = cm/s #centimeter per second
mph = imperial.mile/hour# mile / hour

q = 42 *cms

print(q.to(mph))


#convertion between wavelength and frequency:

freq = nm.to(Hz, equivalencies = spectral())

print(freq)

