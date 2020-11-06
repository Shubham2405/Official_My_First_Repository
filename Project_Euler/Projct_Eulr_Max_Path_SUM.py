from Dec_to_Bin import dec_to_bin

data=['''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23''']
l=data[0].split('\n')
for x in range(15):
    t=l[x].split(' ')
    l[x]=t
ans_list=[]
for z in range(2**14):
    a=dec_to_bin(z)
    list_for_sum=[]
    y_cor=0
    x_cor=0
    while y_cor<14:
        x_cor+=int(a[y_cor])
        list_for_sum.append(l[y_cor+1][x_cor])
        y_cor+=1
    compare=0
    for s in list_for_sum:
        compare+=int(s)
    ans_list.append(compare)
    

    #This code gives us the list which contains all possible sum of values from second row that is excluding the first element.
    