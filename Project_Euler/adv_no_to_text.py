def numfxn(i):
    numbers={
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
        10:'ten',
        11:'eleven',
        12:'twelve',
        13:'thirteen',
        14:'fourteen',
        15:'fifteen',
        16:'sixteen',
        17:'seventeen',
        18:'eighteen',
        19:'nineteen',
        20:'twenty',
        30:'thirty',
        40:'forty',
        50:'fifty',
        60:'sixty',
        70:'seventy',
        80:'eighty',
        90:'ninety',
    }
    ans=''
    if i in numbers:
        ans=numbers.get(i)
    
    elif len(str(i))==2:
        ans=numbers.get((int(((str(i))[0]))*10))+numbers.get((int(((str(i))[1]))))
    
    elif (len(str(i))==3)and(int(str(i)[1]+str(i)[2]) in numbers):
        ans=numbers.get((int(((str(i))[0]))))+'hundredand'+numbers.get(int(str(i)[1]+str(i)[2]))
    
    elif (len(str(i))==3)and(((int(((str(i))[2]))))==0)and(((int(((str(i))[1]))))==0):
        ans=numbers.get((int(((str(i))[0]))))+'hundred'
    
    elif (len(str(i))==3)and(((int(((str(i))[1]))))==0):
        ans=numbers.get((int(((str(i))[0]))))+'hundredand'+numbers.get((int(((str(i))[2]))))
    
    elif (len(str(i))==3)and((int(((str(i))[2])))==0):
        ans=numbers.get((int(((str(i))[0]))))+'hundredand'+numbers.get(int(str(i)[1]+str(i)[2]))
    
    elif len(str(i))==3:
        ans= numbers.get((int(((str(i))[0]))))+'hundredand'+numbers.get((int(((str(i))[1]))*10))+numbers.get((int(((str(i))[2]))))
    
    return ans
    