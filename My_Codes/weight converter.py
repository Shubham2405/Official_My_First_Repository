wt=int(input("What is your weight ? "))
typ=input('Is it in Kg or Lb ')
cf=int(input('How many lbs is a kg ? '))
kg=(typ=='Kg')or(typ=='kg')
lb=(typ=='Lb')or(typ=='lb')

if kg:
    ans=(wt*cf)
elif lb:
    ans=(wt/cf)
else:
    ans=('Input is incorrect')

print(ans)
