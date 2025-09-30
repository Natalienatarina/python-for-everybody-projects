data = "X-DSPAM-Confidence:    0.8475"

ipos = data.find(':')
#print(ipos)

piece = data[ipos+1:]
#print(piece)
value = float(piece)
print(value)