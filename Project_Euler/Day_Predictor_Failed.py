#1 jan 1990 was monday.
Days={1:'Sunday',
      2:'Monday',
      3:'Tuesday',
      4:'Wednesday',
      5:'Thursday',
      6:'Friday',
      7:'Saturday'
      }
Months={
	1:3,
	3:3,
	4:2,
	5:3,
	6:2,
	7:3,
	8:3,
	9:2,
	10:3,
	11:2,
	12:3
}
def Day_Predictor(known_date,known_day,predict_day):
    given=(str(known_date)).zfill(8)
    asked=(str(predict_day)).zfill(8)
    given_date=int(given[0:2])
    given_month=int(given[2:4])
    given_year=int(given[4:8])
    asked_date=int(asked[0:2])
    asked_month=int(asked[2:4])
    asked_year=int(asked[4:8])
    extra_days=0
    for x in range(given_year+1,asked_year):
    	if x%100==0:
    		if x%400==0:
    			extra_days+=2
    		else:
    			extra_days+=1
    	elif x%4==0:
    		extra_days+=2
    	else:
    		extra_days+=1
    for x in range(given_month,13):
    	if x==2:
    		if given_year%100==0:
    			if given_year%400==0:
    				extra_days+=1
    		elif given_year%4==0:
    			extra_days+=1
    	extra_days += Months.get(x,0)

    for x in range(1,asked_month):
    	if x==2:
    		if asked_year%100==0:
    			if asked_year%400==0:
    				extra_days+=1
    		elif asked_year%4==0:
    			extra_days+=1
    	extra_days += Months.get(x,0)
    
    if given_year%100==0:
    	if given_year%400==0:
    		extra_days+= 7 - given_date%7+Months.get(given_month,1)
    	else:
    		extra_days+= 7 - given_date%7+Months.get(given_month,0)
    elif given_year%4==0:
    	extra_days+= 7 - given_date%7+Months.get(given_month,1)
    else:
    	extra_days+= 7 - given_date%7+Months.get(given_month,0)

    extra_days+=asked_date%7
    lll=extra_days%7
    extra_days=lll
    return extra_days