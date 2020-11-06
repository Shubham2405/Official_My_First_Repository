n=int(input('which prime u want ? '))
t=0
c=2
while t!=n:
     i=1
     r=1
     while r!=0:
              i=i+1
              r=(c/i)-(c//i)
              isprime=(c==i)
     c=c+1
     if isprime:
           t=t+1
     
print(c-1)
