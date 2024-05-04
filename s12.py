f=open("1.csv")
ans=0
for x in f:
    sum1=0
    sum2=0
    z=x.split(";")
    for i in range(len(z)):
        z[i]=int(z[i])
    d=[]
    for j in z:
        d.append(z.count(j))
    if d.count(4)==4 and d.count(1)==3:
        for i in range(len(z)):
            if d[i]==4:
                sum1+=z[i]
            if d[i]==1:
                sum2+=z[i]
        if sum1/4>sum2/3:
            ans+=1
print(ans)
