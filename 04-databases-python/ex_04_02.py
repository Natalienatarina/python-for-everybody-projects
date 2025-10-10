import sqlite3

conn = sqlite3.connect('ex_04_02.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Counts (org TEXT, count INTEGER)
''')

cur.execute('DELETE FROM Counts')


fh = open('mbox.txt')
for line in fh: 
    line = line.strip()
    if line.startswith('From '):
        words = line.split()
        if len(words) >= 2:
            email = words[1]
            domain = email.split('@')[1]

        cur.execute('SELECT count FROM Counts WHERE org == ?', (domain,))
        row =cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))

conn.commit()


