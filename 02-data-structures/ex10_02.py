fname = input('Enter File Name: ')
fh = open(fname)
counts = dict()

for line in fh:
    line = line.strip()
    if line.startswith('From '):
        words = line.split()
        if len(words) >=6:
            time_str = words[5]         
            hour = time_str.split(':')[0]
            counts[hour] = counts.get(hour, 0) + 1

for hour in sorted(counts):
    print(hour, counts[hour])
