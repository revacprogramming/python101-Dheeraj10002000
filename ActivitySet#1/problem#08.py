# Files

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    if line.startswith("X-DSPAM-Confidence:"):
        a=line.find('0.')
        z=float(line[a:])
        
        count=count+1
        total=total+z
print('Average spam confidence:',total/count)

