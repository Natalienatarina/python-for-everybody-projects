fname = input('Enter File Name: ')
fh = open(fname)
counts = dict()

for line in fh: 
    line = line.strip()
    if line.startswith('From '):
        words = line.split()
        if len(words) >= 2:
            email = words[1]
            counts[email] = counts.get(email,0) + 1

maxcount = None
maxemail = None
for email, count in counts.items():
    if maxcount is None or count > maxcount:
        maxemail = email
        maxcount = count

print(maxemail, maxcount)


