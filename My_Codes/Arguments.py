def algebra(sign,first_num,second_num):
	ans=''
	if sign=='+':
		ans=int(first_num)+int(second_num)
	elif sign=='-':
		ans=int(first_num)-int(second_num)
	elif sign=='*':
		ans=int(first_num)*int(second_num)
	elif sign=='/':
		ans=int(first_num)/int(second_num)
	else:
		print('Please Check Your Input (+ or - or * or /)')
	return ans

print(algebra(sign='-',first_num='5',second_num=4))
