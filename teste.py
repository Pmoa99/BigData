import sys

#!/usr/bin/python
count = 0
TAB_CHAR = 't'
for line in sys.stdin:
    for token in line.strip().split("\n"):
        if token:
            count += 1
            
print(count)
