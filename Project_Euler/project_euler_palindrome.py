r=range(100,1000)
latest_pal=0
for a in r:
    for b in r:
        n=str(a*b)
        l=len(n)
        t=0
        for x in range(0,l):
            if (n[x]==n[(l-1)-x]):
              t+=1
        is_palindrome=(t==l)
        if is_palindrome and int(n)>int(latest_pal):
            latest_pal=n
print(latest_pal)

        
        
