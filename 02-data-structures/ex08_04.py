fname = input('Enter file name:')
fh = open(fname)
words = []
for line in fh:
    line = line.strip()
    line_words = line.split()
    #print(line)
    for word in line_words:
        if word not in words:
            words.append(word)
words.sort()
print(words)