#!/usr/bin/python3
'''s=input()
print(int(s,2))
t=input()
p={"UPPERCASE":0,"LOWERCASE":0}
for c in t:
        if c.isupper():
                p["UPPERCASE"]+=1
        elif c.islower():
                p["LOWERCASE"]+=1
        else:
                pass
print("UPPERCASE",p["UPPERCASE"])
print("LOWERCASE",p["LOWERCASE"])'''

import re
value = []
items=[x for x in input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    #elif re.search("\s",p):
        #continue
    else:
        pass
    value.append(p)
print (",".join(value))
