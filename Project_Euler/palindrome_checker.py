n=input('What is the number ')
l=len(n)
a=0
for x in range(0,l):
    if (n[x]==n[(l-1)-x]):
      a+=1
is_palindrome=(a==l)
print(is_palindrome)


