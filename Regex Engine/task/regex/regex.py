import re
a,b = input().split('|')
regex = re.compile(a)
if re.match(regex, b):
    print(True)
elif re.findall(a, b):
    print(True)
elif a in b:
    print(True)
elif a == '':
    print(True)
elif a == '' and b == '':
    print(True)
else:
    print(False)