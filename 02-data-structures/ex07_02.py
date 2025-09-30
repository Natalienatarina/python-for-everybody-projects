# Use the file name mbox-short.txt as the file name
fname = input('Enter file name: ')
fh = open(fname)

count = 0
total = 0.0
for line in fh:
    line = line.strip()
    if line.startswith('X-DSPAM-Confidence:'):
        ipos = line.find(':')
        number_str = line[ipos+1:].strip()
        try:
            number = float(number_str)
            total += number
            count += 1
        except ValueError:
            continue

if count > 0:
    average = total / count
    print('Average spam confidence:', average)
else:
    print('No matching lines found.')
    