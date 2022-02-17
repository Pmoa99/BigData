#!/usr/bin/python
import sys


TAB_CHAR = '\t'

lastKey = None
a = 0
s = 0
count = 0
total = 0

for line in sys.stdin:
    key, value = line.strip().split(TAB_CHAR)

    if lastKey and lastKey != key:
        print(lastKey + TAB_CHAR + 'Number char:' + str(a) + TAB_CHAR + 'Number words:' + str(s))
        lastKey = key
        a = len(key)
        s = int(value)
    else:
        lastKey = key
        a = len(str(key))
        s += int(value)
    
    count +=1

    

if lastKey:
    total = a/s
    print(lastKey + TAB_CHAR + 'Average Lenght:' + str(total))
