fname = input('Enter file name: ')
try: 
    fhand = open(fname)
except FileNotFoundError:
    print(f'File cannot be opened: {fname}')
    quit()
for line in fhand:
    line = line.rstrip().upper()
    print(line)