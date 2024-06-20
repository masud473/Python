import time
# Morning: 5 am to 12 pm (noon)
# Early morning: 5 to 8 am
# Late morning: 11 am to 12 pm
# Afternoon: 12 pm to 5 pm
# Early afternoon: 1 to 3 pm
# Late afternoon: 4 to 5 pm
# Evening: 5 pm to 9 pm
# Early evening: 5 to 7 pm
# Night: 9 pm to 4 am1
timer=time.strftime('%H')
t=int(timer)
if(5<=t<12):
    g='Morning'
if(12<=t<17):
    g='Afternoon'
if(17<=t<21):
    g='Evening'
if(21<=t<=23 ):
    g='Night'
if(0<=t<=4 ):
    g='Night'
name=input('What is your name?\n')
print('Good',g,name)
