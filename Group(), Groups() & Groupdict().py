import re
m = re.search(r'([A-Za-z0-9])\1+',input())
if m:
    print (m.group(1))
else:
    print ("-1")