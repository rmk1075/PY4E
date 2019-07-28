han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()

    if len(wds) < 3 or wds[0] != 'From' : #len<wds) < 3 -> wds[2] generates index out error
        continue
    print(wds[2])
