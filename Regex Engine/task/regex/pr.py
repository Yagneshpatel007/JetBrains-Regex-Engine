def singlechar(a, b):
    if a == b:
        return True
    elif a == '.':
        return True
    elif a == '':
        return True
    elif a == '' and b == '':
        return True
    else:
        return False


a, b = input().split('|')

con = True
for i in range(len(a)):
    if b == '':
        con = singlechar(a, b)
    elif singlechar(a[i], b[i]) == True:
        pass
    else:
        con = False
        break

print(con)
