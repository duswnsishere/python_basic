a,b = input().split()
a = int(a)
b = int(b)
if b>=45:
       c = a
       d = b-45
       print(c,d,sep=' ')
elif b<45:
    if a == 0:
        c = 23
        d = 60 - (45-b)
        print(c,d,sep = ' ')
    else:
         c = a-1
         d = 60 - (45-b)
         print(c,d,sep= " ")