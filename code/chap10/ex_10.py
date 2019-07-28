fname = input('Enter File: ')
if len(fname) < 1: fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(wds)
    for w in wds:
        di[w] = di.get(w,0) + 1

#print(di)

tmp = list()
for k,v in di.items():
    tmp.append((v,k))

tmp.sort(reverse = True)
print(tmp[:5])
