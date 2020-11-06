def sn(i):
	sm=0
	for x in range(1,i):
		if i%x==0:
			sm+=x
	return(sm)

ans=[]

for x in range(10001):
	s1=sn(x)
	if sn(s1)==x:
		if s1!=x:
			ans.append(x)

