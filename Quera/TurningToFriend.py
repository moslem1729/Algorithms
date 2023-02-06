xy=input()
zv=input()

xy=xy.split()
x=int(xy[0])
y=int(xy[1])

zv=zv.split()
z=int(zv[0])
v=int(zv[1])

if x<z:
    print("Right")
else:
    print("Left")


