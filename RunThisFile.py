from datetime import datetime
import webbrowser
import random
import time

#Get the Current Time
now = datetime.now()
currentTime = now.strftime("%H:%M")
print(currentTime)

#Set the time you want the alarm to go off
setTime = raw_input("Enter time in HH:MM format\n")

#Open the text file with Youtube URLS, read the lines of the file and select one at random to laucnh.
#Version 3
s = open("Youtube URLs","r")
m = s.readlines()
L = [] #Create an Empty List
for i in range(0,len(m)-1): #credit to https://www.codespeedy.com/how-to-get-a-random-line-from-a-text-file-in-python/ for the logic
    x = m[i]
    z = len(x)
    a = x[:z-1]
    L.append(a)
L.append(m[i+1])
o = random.choice(L)
print(o)

while currentTime < setTime: #Set the condition that if the current time has passes your alarm time to launch a urls
    time.sleep(5) #sleeps for 5 sec so the code isn't constantly running
    now = datetime.now()
    currentTime = now.strftime("%H:%M")
s.close()
webbrowser.open(o)

#This is me practicing how to commit from the IDE Pycharm. Blah blah blah...


#Version 1
'''while currentTime > setTime:
    webbrowser.open("https://www.youtube.com/watch?v=EEjeTS3_RzM")
    break'''

#Version 2
'''while currentTime > setTime:
    with open("Youtube URLs") as f:
        readURLs = f.read()
        L = []
        for i in random(0,len(readURLs)-1)
            x = m[i]
            z = len(x)
            a = x[:z-1]
        L.append(a)
        print(L)
        break'''
