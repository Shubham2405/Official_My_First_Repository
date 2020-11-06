def factor(i):
	n=0
	k=0
	T_N=i*(i+1)/2
	while k!=T_N:
		k+=1
		if T_N%k==0:
			n+=1
	return n