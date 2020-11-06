#1 jan 1990 was monday.
Days={0:'Monday',
      1:'Tuesday',
      2:'Wednesday',
      3:'Thursday',
      4:'Friday',
      5:'Saturday',
      6:'Sunday'
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


from Leap_year_tester import leap_year


def Day_Predictor(predict_day):
    known_date=1011900
    known_day="Monday"
    given=(str(known_date)).zfill(8)
    asked=(str(predict_day)).zfill(8)
    given_date=int(given[0:2])
    given_month=int(given[2:4])
    given_year=int(given[4:8])
    asked_date=int(asked[0:2])
    asked_month=int(asked[2:4])
    asked_year=int(asked[4:8])
    extra_days=0




    # Following is for only Years which are in "between" given and asked

    for x in range(given_year+1,asked_year):
      if leap_year(x):
        extra_days+=2
      else:
        extra_days+=1






    # Following is for rest of the months in the starting year

    for y in range(given_month+1,13):
      if leap_year(given_year):
        extra_days+=Months.get(y,1)
      else:
      	extra_days+=Months.get(y,0)




    # Following if for first months of the given year

    for z in range(1,asked_month):
      if leap_year(asked_year):
        extra_days+=Months.get(z,1)
      else:
        extra_days+=Months.get(z,0)




    #

    extra_days+= asked_date%7
    if leap_year(given_year):
        extra_days+= 7- given_date%7 +Months.get(given_month,1)
    else:
        extra_days+= 7- given_date%7 +Months.get(given_month,0)




    #

    lll=extra_days%7
    extra_days=lll
    return (f'{Days.get(extra_days)}')
