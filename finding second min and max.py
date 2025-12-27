x=list(map(int,input().split()))
x1=min(x)
x2=max(x)
min2=float('inf')
max2=float('-inf')
min1=max1=x[0]
for i in range(1,len(x)):
    if x1<x[i]<min2:
        min2=x[i]
    if x2>x[i]>max2:
        max2=x[i]
print(min2,max2)