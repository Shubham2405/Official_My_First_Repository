r=range(0,500)
for x in r:
    for y in r:
        t=x+y+(((x**2)+(y**2))**(1/2))
        if t==1000:
            print(f'{x} is x and {y} is y')
