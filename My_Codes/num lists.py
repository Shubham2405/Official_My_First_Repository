num=[1,8,3,4,6,7,2,9,1,6,2,9]
n=len(num)
num.sort()
print(num)
ma=0
for x in num:
    if ma<x:
        ma=x
        print(ma)
for x in num:
    k=(num.count(x))
    if k>1:
        num.remove(x)
num.sort()
print(num)
