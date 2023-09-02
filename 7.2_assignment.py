import re
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ") #mbox-short.txt
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    total = total + float(re.findall(r"[-+]?\d*\.\d+|\d+", line)[0])
print("Average spam confidence:", total / count)
# Average spam confidence: 0.7507185185185187

