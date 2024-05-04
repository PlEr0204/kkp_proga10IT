def prost(x):
    d=[]
    for i in range(1, int(x**0.5)+1):
        if x%i==0:
            d.append(i)
            if i!=x//i:
                d.append(x//i)
    d.sort()
    return(d)
maxd=-1
max1=0
max2=0
for i in range(286564, 287270+1):
    t=prost(i)
    if maxd<=len(t):
        maxd=len(t)
        max1=t[-1]
        max2=t[-2]
print(maxd, max1, max2)
        
    
