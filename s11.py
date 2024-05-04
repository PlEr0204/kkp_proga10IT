f=open('1.csv')
k1=0
k2=0
sum2=0
for x in f:
    z=x.split(";")
    if z[0]=="Ю" and z[2]=="английский язык":
        k1+=1
    if z[0]=="ЮВ":
        k2+=1
        sum2+=int(z[3])
print(k1)
print(sum2/k2)
#Не для демо задания это с РешуОГЭ