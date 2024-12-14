import numpy as np
import sys

arr = []
with open('i.tsv') as f:
    for l in f.readlines():
        arr.append(list(map(float,l.split('\t'))))
        
def extract(v):
    return v[3:]

lp = [[0] * len(arr) for _ in range(len(arr))]

def getMap(arr):
    spacemat = []
    gis = []
    for v in arr: #try removing more 
        gis.append(v[2])
        spacemat.append(extract(v)) # remove year, month

    # Project gis vector onto spacemat
    x = np.matrix(spacemat)
    y = np.array(gis)
    return (np.linalg.inv(x.T @ x) @ x.T @ y).T

#print(*(x[0,0] for x in getMap(arr[408:-1])))

for lsplit in range(0,len(arr)-2):
    for split in range(max(lsplit + 1, len(arr)-24),len(arr)):
        try:
            wawa = getMap(arr[lsplit:split])
        except np.linalg.LinAlgError:
            lp[lsplit][split] = -1

        l=arr[split]
        pred = round((np.matrix(extract(l)) @ wawa)[0,0] - l[2],3)
        lp[lsplit][split] = pred

for x in lp:
    print(*x,sep='\t')

sys.exit(0)

#np.set_printoptions(threshold=sys.maxsize)
#print(np.around(lp,decimals=3), sep='\t')

print(arr)
print("year\tmonth\tactual\tprediction\terror")
# get "training data"
spacemat = []
gis = []
split = -1


for v in arr[:split]: #try removing more 
    gis.append(v[2])
    print(*v[0:2])
    spacemat.append(extract(v)) # remove year, month

# Project gis vector onto spacemat
x = np.matrix(spacemat)
y = np.array(gis)
wawa = (np.linalg.inv(x.T @ x) @ x.T @ y).T
print(wawa)
a = x @ wawa
print(*a,sep='\n')

print("year\tmonth\tactual\tprediction\terror")
for l in arr:
    pred = (np.matrix(extract(l)) @ wawa)[0,0]
    print(*map(int,l[:3]), pred, pred-l[2], sep='\t')


lp = []
print("year\tmonth\tactual\tprediction\terror")
for split in range(len(arr[0]) + 20, len(arr)):
    spacemat = []
    gis = []
    for v in arr[:split]: #try removing more 
        gis.append(v[2])
        spacemat.append(extract(v)) # remove year, month

    # Project gis vector onto spacemat
    x = np.matrix(spacemat)
    y = np.array(gis)
    wawa = (np.linalg.inv(x.T @ x) @ x.T @ y).T
    l=arr[split]
    pred = (np.matrix(extract(l)) @ wawa)[0,0]
    lp.append((np.matrix(extract(arr[-1])) @ wawa)[0,0])
    print(*map(int,l[:3]), pred, pred-l[2], sep='\t')

print('Predictions for last month:')
print(np.around(lp,decimals=3), sep='\t')

print('Predictions for last month at different starting values:')
lp = []

for lsplit in range(len(arr) - len(arr[0]) - 20):
    spacemat = []
    gis = []
    for v in arr[lsplit:-1]: #try removing more 
        gis.append(v[2])
        spacemat.append(extract(v)) # remove year, month

    # Project gis vector onto spacemat
    x = np.matrix(spacemat)
    y = np.array(gis)
    wawa = (np.linalg.inv(x.T @ x) @ x.T @ y).T
    lp.append((np.matrix(extract(arr[-1])) @ wawa)[0,0])

print(np.around(lp,decimals=3), sep='\t')
