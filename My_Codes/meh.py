name=str(input("What'syour name Sir ? "))            #Name is a variable
col=str(input("What is your favourite color ? "))    #col is a variable
print(name+ " likes "+ col)

course = 'Python For Beginners'                      #course is a variable
print(course[3:])
print(course[2:-8])
lesson=(course[:10])                                 #Lesson is a variable
print(lesson)

print("""
Hi Sir,
How are you
Nice to meet You.
See u later.""")

msg = f"<{name}> likes [{col}]"
print(msg)
       
print(len(course))

print(course.find('O'))
print(course.find('n'))
print(course.replace(' Python','AnAcOnDa  '))
print(course.replace('Python','AnAcOnDa  '))
print(abs(-2.8))
print(round(-2.8))

import math

print(math.tan(math.pi/4))

for item in 'Python yash ':
    print(item)

m=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
print(m[2][0])

for k in m:
    for t in k:
        print(t*'*')

num=[1,2,2,3,3,3,5,5,5,0,7,7,8,9,1,5,5,6,3]
print(num)
num.remove(5)
num2=num.copy()
print(num)
num2.sort()
print(num2)
num.reverse()
print(num)
