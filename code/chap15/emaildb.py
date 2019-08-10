import sqlite3

# check whether able to connect to the sql or not
conn = sqlite3.connect('emaildb.sqlite')
#cur is handle
cur = conn.cursor()

# delete the table 'Counts' which already exists
cur.execute('DROP TABLE IF EXISTS Counts')

# create table Counts
cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,)) # (email,) value is put in the '?' # cur just open not really retrieving the data
    row = cur.fetchone() # read first one from cur
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
                    
    # move data to the dist -> commit
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
