import glob
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import matplotlib.animation as ani

path = "img/test/2021-05-26_01-05-44_C_-30.96_60.00s_0004.fits"

file = glob.glob(path)
print(file)
data = fits.open(file[0])[0].data

dmax = np.max(data)
dmin = np.min(data)

flat_trashhold = (dmax-dmin)*0.5

#data_ids = data < flat_trashhold
#data[data_ids] = 0

def intersect (a,b,c,d):
    return a<=d and c<=b

def combine_row_stars(rows):
    len_rows = len(rows)
    known_stars = []
    prev_y = 0
    current_stars = []
    for y, row_list in rows:
        next_stars = []
        if y == prev_y+1:
            for y0, x0_known, x1_known in current_stars:
                next_found = False
                for x0,x1 in row_list:
                    if intersect(x0,x1 ,x0_known,x1_known ):
                        next_stars.append([y0,min(x0,x0_known) , max (x1,x1_known)])
                        next_found = True
                        break
                if not next_found:
                    known_stars.append([y0,prev_y,x0,x1])
        else:
            for y0, x0_known, x1_known in current_stars:
                known_stars.append([y0,prev_y,x0,x1])

            for x0,x1 in row_list:
                next_stars.append([y,x0,x1])
        current_stars = next_stars
        prev_y = y


    return known_stars





def row_stars_select(data, flat_trashhold):
    maxy,maxx = data.shape
    #print(maxx,maxy)
    rows = []
    for y in range(maxy):
        if y % 100 == 0:
            print("pricessing row :" , y )
        x = 0
        row = data[y]
        row_stars = []
        while x < maxx:
            while x < maxx and row[x] <flat_trashhold:
                x+=1
            if x >= maxx:
                continue
            star_x0 = x
            while x < maxx and row[x] > flat_trashhold:
                x += 1
                star_x1 = x
            row_stars.append((star_x0, star_x1))
        if row_stars:
            rows.append((y,row_stars))
    return rows





#print(dmax,dmin)

rows = row_stars_select(data,flat_trashhold)
#rows = [(449, [(2302, 2306)]), (450, [(2302, 2307)]), (451, [(2301, 2308)]), (452, [(2301, 2308)]), (453, [(2301, 2308)]), (454, [(2302, 2307)]), (668, [(502, 506)]), (669, [(502, 506)]), (670, [(502, 506), (625, 628)]), (671, [(502, 505), (624, 629)]), (672, [(624, 630)]), (673, [(624, 630)]), (674, [(624, 629)]), (675, [(624, 629)]), (676, [(624, 628)]), (751, [(1125, 1127)]), (752, [(1125, 1127)]), (1083, [(1569, 1570)]), (1084, [(391, 394)]), (1085, [(391, 395)]), (1086, [(391, 395)]), (1087, [(391, 395)]), (1088, [(392, 394)]), (1180, [(1549, 1551)]), (1181, [(1549, 1552)]), (1182, [(1550, 1551)]), (1184, [(1654, 1656)]), (1185, [(1654, 1656)]), (1186, [(1654, 1656)]), (1189, [(1667, 1669)]), (1190, [(1667, 1669)]), (1203, [(3269, 3278)]), (1204, [(3266, 3281)]), (1205, [(3264, 3282)]), (1206, [(3263, 3283)]), (1207, [(3261, 3284)]), (1208, [(3260, 3284)]), (1209, [(3260, 3285)]), (1210, [(3260, 3285)]), (1211, [(3259, 3285)]), (1212, [(3259, 3285)]), (1213, [(3259, 3284)]), (1214, [(3259, 3284)]), (1215, [(3260, 3284)]), (1216, [(3260, 3283)]), (1217, [(3261, 3283)]), (1218, [(3262, 3282)]), (1219, [(3263, 3281)]), (1220, [(3264, 3280)]), (1221, [(3265, 3279)]), (1222, [(3267, 3278)]), (1223, [(3269, 3276)]), (1224, [(3272, 3274)]), (1242, [(1612, 1614)]), (1243, [(1612, 1614), (1818, 1819)]), (1244, [(1612, 1614), (1818, 1819)]), (1253, [(1636, 1637)]), (1254, [(1636, 1637)]), (1265, [(1545, 1547)]), (1266, [(1545, 1548)]), (1267, [(1545, 1547)]), (1339, [(1862, 1864), (2671, 2673)]), (1340, [(1862, 1864), (2670, 2674)]), (1341, [(1862, 1864), (2669, 2675)]), (1342, [(2670, 2674)]), (1376, [(1500, 1501)]), (1377, [(1500, 1501)]), (1411, [(704, 705)]), (1412, [(703, 707)]), (1413, [(703, 708)]), (1414, [(703, 708)]), (1415, [(703, 708)]), (1416, [(703, 707)]), (1417, [(704, 706)]), (1461, [(886, 888)]), (1462, [(885, 890)]), (1463, [(885, 890)]), (1464, [(885, 890)]), (1465, [(885, 890)]), (1466, [(885, 890)]), (1467, [(886, 888)]), (1576, [(1376, 1378)]), (2040, [(2207, 2208)]), (2041, [(2207, 2208)])]


print(rows)
knowns = combine_row_stars(rows)

print("knowns :", knowns)

ramkafill = dmax
rd=20
for (y0,y1,x0,x1) in knowns:
    y0, y1, x0, x1 = y0-rd,y1+rd,x0-rd,x1+rd
    data[y0,x0:x1] = ramkafill
    data[y1, x0:x1] = ramkafill
    data[y0:y1, x0] = ramkafill
    data[y0:y1, x1] = ramkafill


fig = plt.figure()
im = plt.imshow(data, cmap = "gray")
plt.colorbar()
plt.show()

#print(data)


