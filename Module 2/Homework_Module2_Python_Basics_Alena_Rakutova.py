#Write a code, which will:
#1. create a list of random number of dicts (from 2 to 10)
#dict's random numbers of keys should be letter,
#dict's values should be a number (0-100),
#example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
#2. get previously generated list of dicts and create one common dict:
#if dicts have same key, we will take max value, and rename key with dict number with max value
#if key is only in one dict - take it as is,
#example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
# Each line of code should be commented with description.
# Commit script to git repository and provide link as home task result.

import string# as it mentioned in - dict's random numbers of keys should be letter and after clarification it should be lower case letters
import random#as per req. we need to generate random number of dict/keys in the dict/values
from collections import Counter
dictList = []#it is the blank list for generated dicts
for a in range(random.randint(2,10)): # random number of dictionaries
    size    = random.randint(1,26)    # random dictionary size that can fit all lowercase letters
    keys    = random.sample(string.ascii_lowercase,size)  # declare keys which are random lowercase letters
    values  = (random.randint(0,100) for a in range(size)) # random numbers (0-100)
    oneDict = dict(zip(keys,values))                      # assemble dictionary using keys and values.
    dictList.append(oneDict)                              # add it to the list of dictionaries
print(dictList) #show the list of dictionaries on the screen
#dictList1 = dictList.copy()
result = {} #declare empty result dictionary
indx = {}  #declare empty dictionary for keys and their dict number from vhere they get
for i, d in enumerate(dictList): # declare that we are starting a loop, working with i - number of dictionary(caclaulated for each iteration) and d dictionaries within list of dictionaries
    for k, v in d.items(): # work with keys and values in each dictionary
      if k in result.keys():# if key already in result dictionary
          if v > result[k]: # we check if value for the key > value that already in the result dictionary
              result[k] = v # and if so we change the value for that key
              indx[k] = i+1 #and fill key+ the number of dictionary where the max value was found into separate indx dictionary (i+1) = 1 if the highest value for the particular key was found in 1 dict
      else:
          result[k] = v #if condition don't met will save just key + value in the result dict
print(result)#for testing purpose
print(indx)#for testing purpose
for k, v in indx.items(): #start for loop where we add keys in result dict if they are in dict with indexes with the same values(max val)
    result[f'{k}_{v}'] = result[k]#and because we use _ for our new keys need to use f and '_'  to embed python items inside string literals for formatting
    result.pop(k) #just delete not formated key
print(result)
#I couldn't add indexes according to dictionary # with the biggest number
# after introducing pop my select returns not max value
# I don't see _2
