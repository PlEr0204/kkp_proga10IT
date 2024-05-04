def s(st):
    ans = ''
    mb = []
    count = 1
    ans += st[0]
    for i in range(len(st) - 1):
        if st[i] != st[i + 1]:
            ans += st[i + 1]
            mb.append(count)
            count = 1
        else:
            count += 1
    ans1 = ""
    for i in ans:
        if i != ans[len(ans) - 1]:
            ans1 += i
    return ans1, mb
a = input()
b = input()
c = input()
ans1, mb1 = s(a + "_")
ans2, mb2 = s(b + "_")
ans3, mb3 = s(c + "_")
z = [0]*len(mb1)
otv = ''
for i in range(len(mb1)):
    z[i] = (mb1[i] + mb2[i] + mb3[i]) - max(mb1[i], mb2[i], mb3[i]) - min(mb1[i], mb2[i], mb3[i])
    otv += ans1[i] * z[i]
if ans1 == ans2 == ans3:
    print(otv)
else:
    print("IMPOSSIBLE")
