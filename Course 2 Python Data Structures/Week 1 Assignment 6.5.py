text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('0')

slice1 = text[pos:]
slice2 = float(slice1)

print(slice2)
