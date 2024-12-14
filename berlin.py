# Creates a GeoJSON for https://www.scribblemaps.com/ connecting a selection of Berlins around the world, 
# using the actual shortest straight-line path rather than a straight line path on the Mercator projection.
# didn't clean up the code at all

import numpy as np
import math

dat = [{"type":"Feature","id":"sm9885eff5","geometry":{"type":"Point","coordinates":[13.404954,52.5200066]},"properties":{"name":"Berlin"}},{"type":"Feature","id":"smfb79e40c","geometry":{"type":"Point","coordinates":[-78.9578022,39.9206363]},"properties":{"name":"Berlin"}},{"type":"Feature","id":"sm23d6af99","geometry":{"type":"Point","coordinates":[-81.7941315,40.5612163]},"properties":{"name":"Berlin"}},{"type":"Feature","id":"sma0a049a7","geometry":{"type":"Point","coordinates":[-72.7456519,41.621488]},"properties":{"name":"Berlin"}},{"type":"Feature","id":"sm09ab3ffe","geometry":{"type":"Point","coordinates":[-86.74245,34.181496]},"properties":{"name":"Berlin"}},{"type":"Feature","id":"sm2a9534b8","geometry":{"type":"Point","coordinates":[-83.62381,31.069448]},"properties":{"name":"Berlin"}},{"type":"Feature","id":"smb03aadbc","geometry":{"type":"Point","coordinates":[-75.219,38.324726]},"properties":{"name":"Berlin"}},{"type":"Feature","id":"smb0d491db","geometry":{"type":"Point","coordinates":[-74.92946,39.79143]},"properties":{"name":"Berlin"}},{"type":"Feature","id":"smc5f7758f","geometry":{"type":"Point","coordinates":[-73.37212,42.693092]},"properties":{"name":"Berlin"}},{"type":"Feature","id":"sm354a4658","geometry":{"type":"Point","coordinates":[-72.576351,44.21002]},"properties":{"name":"Berlin"}},{"type":"Feature","id":"sm63fcbaf0","geometry":{"type":"Point","coordinates":[-71.17991,44.470207]},"properties":{"name":"Berlin"}},{"type":"Feature","id":"sm00191cd5","geometry":{"type":"Point","coordinates":[-71.638306,42.381332]},"properties":{"name":"Berlin"}},{"type":"Feature","id":"sm88352f09","geometry":{"type":"Point","coordinates":[-89.9033,39.75894]},"properties":{"name":"Berlin"}},{"type":"Feature","id":"sm5fbac5a5","geometry":{"type":"Point","coordinates":[-98.49006,46.37873]},"properties":{"name":"Berlin"}},{"type":"Feature","id":"sm93fb1ba2","geometry":{"type":"Point","coordinates":[-88.94799,43.968346]},"properties":{"name":"Berlin"}}]

fcoords = [fea["geometry"]["coordinates"] for fea in dat][1:] # 1:
#print(len(fcoords))

#euler = []

#pairs = []
paths = []

def vec(a):
    lat, lon = a
    theta = (90 - lon) / 180 * math.pi
    phi = lat / 180 * math.pi
    return np.array([math.sin(theta) * math.cos(phi), math.sin(theta) * math.sin(phi), math.cos(theta)])

def normalize(a):
    x, y, z = a
    r = (x**2 + y**2 + z**2) ** 0.5
    return x/r, y/r, z/r

def unvec(a):
    x, y, z = a
    #lat = (1 if y>=0 else -1) * math.acos(x/(x**2 + y**2)**.5) / math.pi * 180
    sgny = (1 if y>=0 else -1)
    if x == 0:
        phi = math.pi/2 * sgny
    else:
        phi = math.atan(y/x)
        if x < 0:
            phi += math.pi * sgny

    return [phi / math.pi * 180, 90 - math.acos(z/(x**2 + y**2 + z**2)**.5) / math.pi * 180]

def midpoint(a, b):
    #assert vec(a) + vec(b) == wawa
    return unvec(vec(a) + vec(b))#unvec(normalize((vec(a) + vec(b)) / 2))

for i, a in enumerate(fcoords):
    for b in fcoords[:i]:
        path = [a, b]
        for _ in range(8): # accuracy ~1 meter for 1000 km path in USA
            inserts = []
            for i, j in zip(path[:-1], path[1:]):
                inserts.append(midpoint(i, j))
            #print(path, inserts)
            path = [x for y in zip(path, inserts) for x in y] + [b]
            #path, opath = [None] * (len(path) + len(inserts)), path
            #path[::2] = opath
            #path[1::2] = inserts
            #print(path)

        paths.append(path)
        #pairs.append((a, b))

print('{"features":['+','.join('{"type":"Feature","id":"sm1b159349","geometry":{"type":"LineString","coordinates":' + str(path) + '},"properties":{}}' for path in paths)+'],"type":"FeatureCollection","id":"root"}')
