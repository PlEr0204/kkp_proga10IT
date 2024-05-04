f=open("output.txt")
n=0
s=0
k=0
k1=0
for x in f:
    z=x.split(";")
    if z[2]=="9" and int(z[3])>250:
        n+=1
    if z[1]=="3":
        s+=int(z[3])
        k+=1
    if z[1]=="48" or  z[1]=="49" or z[1]=="46":
        k1+=1
print(n)
print(s/k)
print(k1)
