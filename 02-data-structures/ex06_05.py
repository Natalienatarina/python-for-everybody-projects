data = "X-DSPAM-Confidence:    0.8475"
atpos = data.find('0')
atpos = float(atpos)
host = data[23:29]
print(host)