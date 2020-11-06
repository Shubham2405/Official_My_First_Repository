r=list(range(2,200))
print(r)
p_sum=0
for x in r:
    input_range=range(2,x+1)
    c=5
    i=1
    while c!=0:
        i+=1
        c=x/i-x//i
    if i==x:
        p_sum+=x
        n=2000000//x
        factorlist=list(range(1,n+1))
        for t in factorlist:
            r.remove(t*x)
    print (r)
print(p_sum)
