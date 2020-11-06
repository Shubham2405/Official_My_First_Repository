def prime_checker(n):
    r=21
    c=1
    while r!=0:
        c+=1
        r=n/c-n//c
    if c==n:
        print(f'{n} is a prime.')
    else:
        print(f'{n} is not a prime.')

prime_checker(46)

