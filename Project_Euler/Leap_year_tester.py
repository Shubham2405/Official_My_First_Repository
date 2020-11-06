def leap_year(i):
	if i%100==0:
		return(i%400==0)
	else:
		return(i%4==0)