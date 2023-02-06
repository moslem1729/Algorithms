sflx=input()
sflx=sflx.split()
s=int(sflx[0])
f=int(sflx[1])
l=int(sflx[2])
x=int(sflx[3])

if x<s:
    print("exam did not started!")
elif x>=f:
    print("exam finished!")
else:
    t=f-x
    if t>l:
        print(l)
    else:
        print(t)