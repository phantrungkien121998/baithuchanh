import re
value=[]
items=[x for x in input("Nhập mật khẩu:").split('.')]
# ###########
for p in items:
    if len(p)<6 or len(p)>12:
       contine
    else:
       pass
    if not re.search("[a-z]",p):
       contine
    elif not re.search("A-Z]",p):
        continue
    elif re.search("\s",p):
         continue
    else:
        pass
    value.append(p)
    print(",".join(value))
