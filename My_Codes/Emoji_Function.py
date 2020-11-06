def emoji_c(message) :
	l=message.split(' ')
	emoji={':)':'Smiley Chot ',
	       ':(':'Sad Chot '
	  }
	o=''
	for item in l:
	   o += emoji.get(item,f'{item} ')
	return o

r=emoji_c('Hello :)')
print(r)
