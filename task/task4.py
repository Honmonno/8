import random

def monty_hall_without_change(choices):
     
      random.shuffle(choices)
      return choices[random.randrange(len(choices))]
  
def monty_hall_with_change(choices):
     
     random.shuffle(choices)
     
     first_choice = random.randrange(len(choices))
     
     for i in range(len(choices)):
         if i != first_choice and choices[i] == 'к':
             host_choice = i
             break
     
     for i in range(len(choices)):
         if i != first_choice and i != host_choice:
             return choices[i] 
         
choices = ['к', 'к', 'а']

N = 100000
 

win_count = 0
for _ in range(N):
     result = monty_hall_without_change(choices)
     if result == 'а':
         win_count += 1

print(win_count/N)
 

win_count = 0
for _ in range(N):
     result = monty_hall_with_change(choices)
     if result == 'а':
         win_count += 1

print(win_count/N)