#Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
# Write a Python program to solve the general version of the above problem. 
# Ask the user for the time now (in hours) and then ask for the number of hours to 
# wait for the alarm. Your program should output what the time will be on a 
# 24-hour clock when the alarm goes off.


import array
hours = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23] #if we want to display '1:00 PM' instead of '13', we would replace that value.
print("Enter the current time in hour.")
currentTime = int(input())

print("How long do you want to wait for the alarm?")
hoursToWait = int(input())

idx = currentTime

for counterHour in range(0,hoursToWait):
    if idx == (len(hours)-1): # we could just replace '(len(hours) -1)' with the value 23 since that's the max index value.
        idx = 0 # if it's at element 23, we reset it to 0, or midnight.
    else:
        idx +=1 # increment the index by one.11

#display the hour.
print("Your alarm clock will go off at '{0}:00'.".format(hours[idx])) #We can use idx by itself, however if we have custom values in the hours list, it will not work.
