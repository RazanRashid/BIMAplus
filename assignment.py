import math 
#number of polygon points
n = int(input("Enter the number of polygon points: "))
if n < 3:
    n=int(input("Please enter the number of points not less than 3: "))

#points Coordinates
x = []
y = []

print("Enter x and y coordinates for polygon points ...")
for i in range(n):
    xcoord = float(input("Enter X Coordinate for point " + str(i + 1) + ": "))
    x.append(xcoord)
    ycoord = float(input("Enter Y Coordinate for point " + str(i + 1) + ": "))
    y.append(ycoord)
print(" ")

#print coordinates in table
print("Coordinates Table")
print(f"{'Point':>3} {'X':>8} {'Y':>10}")
print("-" *35)
for i in range(n):
    print(f"{i+1:>3} {x[i]:>12} {y[i]:>10}")
print(" ")

print("Geometric characteristics: ")

#Calculate the cross sectional area
Axl = []
for i in range(n):
    Ax = (x[i]+x[i-1])*(y[i]-y[i-1])
    Axl.append(Ax)
TAx = 0.5*sum(Axl)
print("Ax:    ", TAx)

#calculate the static cross sectional moments 
Sxl =[]
for i in range(n):
    Sx = (x[i]-x[i-1])*((y[i]**2)+(y[i-1]*y[i])+(y[i-1]**2))
    Sxl.append(Sx)
TSx = -abs((1/6)*sum(Sxl))
print("Sx:   ", round(TSx, 2))
Syl =[]
for i in range(n):
    Sy = (y[i]-y[i-1])*((x[i]**2)+(x[i]*x[i-1])+(x[i-1]**2))
    Syl.append(Sy)
TSy = (1/6)*sum(Syl)
print("Sy:    ", round(TSy, 2))

#calculate the axial moments of interia of the transmission
Ixl =[]
for i in range(n):
    Ix = (x[i]-x[i-1])*((y[i]**3)+((y[i]**2)*y[i-1])+y[i]+(y[i-1]**2)+(y[i-1]**3))
    Ixl.append(Ix)
TIx = -abs((1/12)*sum(Ixl))
print("Ix:   ", round(TIx, 2))

Iyl =[]
for i in range(n):
    Iy = (y[i]-y[i-1])*((x[i]**3)+((x[i]**2)*x[i-1])+(x[i]*(x[i-1]**2)+(x[i-1]**3)))
    Iyl.append(Iy)
TIy = ((1/12)*sum(Iyl))
print("Iy:    ", round(TIy, 2))

Ixyl = []
for i in range(n):
    Ixy = (y[i]-y[i-1])*((y[i]*(3*x[i]**2+2*x[i]*x[i-1]+x[i-1]**2)) + \
        y[i-1]*(3*x[i]**2+2*x[i]*x[i-1]+x[i]**2))
    Ixyl.append(Ixy)
    TIxy = -abs((1/24)*sum(Ixyl))
print("Ixy:  ", round(TIxy, 2))

#coordinates of the cross section centroid
xt = TSy/TAx
print("xt:    ", round(xt, 2))
yt = TSx/TAx
print("yt:   ", round(yt, 2))

#Calculate the moments of interia with respect to the axes in parallel of points gravity
Ixt = TIx - ((yt**2)*TAx)
print("Ixt:  ", round(Ixt, 2))
Iyt = TIy -((xt**2)*TAx)
print("Iyt:   ", round(Iyt, 2))
Ixyt = TIxy + (xt*yt*TAx)
print("Ixyt: ", round(Ixyt, 2))




                                                                                           