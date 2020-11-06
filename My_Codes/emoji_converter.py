Input=input('>')
words = Input.split(' ')
output=''
emojis = {
    ':)':'simley chot ',
    ':(':'sad chot '
    }
for item in words:
    output+=emojis.get(item,f'{item} ')
print(output)
    
