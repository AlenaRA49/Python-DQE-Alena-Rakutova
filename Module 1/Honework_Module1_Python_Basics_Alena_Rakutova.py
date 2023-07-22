#Create a python script
#1 Create list of random numbers from 0 to 1000
#2 Sort list from min to max (without using sort(), sorted())
#3 Calculate average for even and odd numbers
#4 Print average results in console
#5 Each line of code should be commented with description
#6 Commit script to git repository and provide link as home task result

import random #For creating randome list need to use random module
from statistics import mean #for calculating average need to use statistics module which contains an in-built function to calculate average of numbers.
a = random.sample(range(0, 1001), 100)#according to requirement we need to see random numbers from 0 to 1000, but range and random operators cut off the last number, so I took 1001 for sowwing 1000
i = [] #add new empty list for sorted values
while a: #the cycle will be running while a is ...
    min = a[0]#start point got loop
    for x in a: # take one of the number
        if x < min: #and compare with min on first step = 0
            min = x #annons now min = x
    i.append(min) #add min value to the end of the i list
    a.remove(min)# remove checked value form initial list
sorted = i # for testing purposes declare new list sorted which equal to i
#print (sorted) # check sorted lis on UI, commented because out of scope
e = [] #add new empty list for even values
o = [] #add new empty list for odd values
for num in sorted: #declare variable (num) which should be in list sorted
    if num % 2 == 1: #if the num divided by 2 has remainder 1
        o.append(num) #then add num to list o
odd = o#While I writing the code I need check myself, the step could be skipped
#print (odd) #Also it is just for testing
for val in sorted: #the same declare variable (val) which should be in list sorted
    if val % 2 == 0:#if the val divided by 2 doesn't have remainder
        e.append(val)#then add val to list e
even = e#declared for testing purposses
#print (even)#Also it is just for testing
avgOdd = mean(odd) #calculate average for odd values from the initial massive
avgEven = mean(even)#calculate average for even values from the initial massive
print (round(avgOdd,2)) #on UI I want to present rounded values, but for further calculation is better to use raw value
print (round(avgEven,2)) #on UI I want to present rounded values, but for further calculation is better to use raw value
