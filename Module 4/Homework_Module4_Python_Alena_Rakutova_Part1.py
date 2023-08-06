import string
import random
dictList = []#list of dictionaries variable should be available for both functions
def dict_list():#start of first function that return list of dictionaries with predifined syze and parameters that were choosen according the rules
    for a in range(random.randint(2,10)):
        size  = random.randint(1,26)
        keys = random.sample(string.ascii_lowercase,size)
        values = (random.randint(0,100) for a in range(size))
        oneDict = dict(zip(keys,values))
        dictList.append(oneDict)
    return dictList
dict_list()
print(dictList)
def result(dictList):#start for function that will select max values for the same keys and add indexes for the key according the rules. argument of the function the result of the previous function
    result = {}#I leave both variables within the function because they won't be used anywhere else
    indx = {}
    for i, d in enumerate(dictList):
        for k, v in d.items():
            if k in result.keys():
                if v > result[k]:
                    result[k] = v
                    indx[k] = i+1
            else:
                result[k] = v
    for k, v in indx.items():
        result[f'{k}_{v}'] = result[k]
        result.pop(k)
    return result, indx
result(dictList)
r = result(dictList)
print(r)
#I get rid of 2 additional prints of result and indx