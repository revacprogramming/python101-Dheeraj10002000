# Dictionaries

#filename = "dataset/mbox-short.txt"
fname=input("enter the file name")
fhand = open('fname')
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[1])
    count += 1
print('There were %d lines in the file with From as the first word' % count)
# mbox-short.txt 