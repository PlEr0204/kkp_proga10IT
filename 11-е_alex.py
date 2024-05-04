d=[]
a=0
k=0
b=0
c=0
with open("C://Users//Lenovo//Downloads//БД_ученики (1).csv") as f:
    for i in f:
        d.append(i.strip().split(";"))
for i in range(len(d)):
    if int(d[i][-1])>=250:
        a+=1
    if int(d[i][1])==3:
        k+=1
        b+=int(d[i][-1])
    if int(d[i][1])==49 or int(d[i][1])==46 or int(d[i][1])==48:
        c+=1
print(a)
print(b/k)
print(c)
