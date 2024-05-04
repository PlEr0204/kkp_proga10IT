a=[33,38,56,89,85]#входные данные
b=17#делитель
d=[]
k=0
for i in range(len(a)):
    d.append(a[i]%b)
for i in range(len(d)):
    if d.count(d[i])>1:
        k+=a[i]
print(k)
