def dec_to_bin(inp):
	k=[]
	n=0
	while inp>1:
		k.append(inp%2)
		inp=inp//2
		n=n+1
	k.append(1)
	if len(k)<14:
		while len(k)!=14:
                        k.append('0')
	k.reverse()
	ans=''
	for x in k:
		ans+=str(x)
	if inp==0:
		ans='00000000000000'
	return(ans)

#This code returns us a function which converts any given decimal to 14 digit binary (Trailing zeroes also included)