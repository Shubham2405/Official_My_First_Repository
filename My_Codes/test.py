b='***************'
num=[5,2,5,2,2,2,5,2,5]
for x in num :
    print(b[:x])

for x in num:
    n=num.count(x)
    print(n)
    if n>1:
        num.remove(x)
print(num)

