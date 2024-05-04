d=[]
a=0
k=0
def f(n):
    global d
    for i in range(2,n//2):
        if n%i==0:
            d.append(i)
    return len(d)
for i in range(286564,287270):
    if f(i)>=k:
        k=len(d)
        a=i
print(len(d))
print(d[-1],d[-2])
