a=input()#первое число
b=input()#второе число
a=int(a,16)
b=int(b,16)
a=str(bin(a))[2:]
a="0"*(8-len(a))+a
b=str(bin(b))[2:]
b="0"*(8-len(b))+b
s=""
for i in range(len(a)):
    if a[i]=="0" and b[i]=="0":
        s+="0"
    elif a[i]=="1" and b[i]=="1":
        s+="0"
    else:
        s+="1"
print(str(hex(int(s,2)))[2:].upper())