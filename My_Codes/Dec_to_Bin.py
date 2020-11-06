def dec_to_bin(inp):
	k=[]
	n=0
	while inp>1:
		k.append(inp%2)
		inp=inp//2
		n=n+1
	k.append(1)
	k.reverse()
	ans=''
	for x in k:
		ans+=str(x)
	return(int(ans))
