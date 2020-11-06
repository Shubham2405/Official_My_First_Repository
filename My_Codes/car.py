i='p'
status=' '
while i.lower()!='quit':
      i=input(f'>')
      if i.lower()=='help':
          print(f'''Start - to start the car.
Stop - to stop the car.
Quit - to quit the game .''')
      elif i.lower()=='start' and status!='on':
              status='on'
              print(f'Car started... Ready to go !')
      elif i.lower()=='start' and status=='on':
              print('CAR is ALREADY ON !!!')
      elif i.lower()=='stop' and status!='off':
              status='off'
              print("car stopped")
      elif i.lower()=='stop' and status=='off':
              print('CAR is ALREADY stopped')
      elif i.lower()!='quit':
          print("I don't understand that")
    

