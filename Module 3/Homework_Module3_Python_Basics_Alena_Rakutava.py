import re
query = ("homEwork:" 
"\n"
"  tHis iz your homeWork, copy these Text to variable." \
"\n" \
"\n" \
"\n" \
"\n" \
"  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph." \
"\n"
"\n"
"\n"
"\n"
"  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE." \
"\n"
"\n"
"\n"
"\n"
"  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.")#copied task with all new lines and whitespaces
#print(query)
calc_whitespaces = query.replace(' ', '&')#change space to another symbol
calc_whitespaces1 = calc_whitespaces.replace('\n', '&')#change new line to other symbol
print(calc_whitespaces1.count(r"&"))#calculation of whitespaces and showing on UI
norm1 = re.sub("&+", " ", calc_whitespaces1)#replace added & sysmbol with space
#print(norm1)
norm2 = norm1.lower()#convert the string to lowercase
#print(norm2)
list_query = norm2.split()#convert into list
for i in range(len(list_query)):#allows to iterate with each item of the list with the help of its index
    if list_query[i] == 'iz': #look though all values and if it = iz
        list_query[i] = 'is'#replace it with is
print(list_query)#check
subs = '.'# Initializing substring
res = [i for i in list_query if subs in i]# using list comprehension to get string with all last words in aech sentence
print(res)
new_list = []#get rid of dots, create e empty list
for n in res: #for each element from res
    new_list.append(n.split('.')[0])#add all the elements into new list but without dots
res1 = " ".join(new_list) #compile string - it's list of words for the additional sentence
res2 = res1.replace('87','87.')#final dot in the list of words for the additional sentence
print('res3 ' + res2)#show what are the words for the sentence
list_add = res2.split()#split string into separate words in the list
add1 = "This is a"# first additional word
add2 = "and a"#second
add3 = "in the"
add4 = "and"
add5 = 'more than'
list_add.insert(0, add1)#insert each word in the correct plase within the list of strings
list_add.insert(5, add2)
list_add.insert(7, add3)
list_add.insert(9, add4)
list_add.insert(11, add5)
list_add1 = " ".join(list_add)#compile string from the list
list_query.insert(list_query.index('paragraph.')+1,list_add1) #add aditional sentence into the particular place
str_add2 = " ".join(list_query)#compile the string with the sentences
norm3 = str_add2.split(".")#split them for better access to the each separate sentance
norm3 = [i.lstrip() for i in norm3]#get rid of spaces on first plase each string element in the list
norm4 = [n.capitalize() for n in norm3]#convert the first letter of each sentence into Capital Case letter
final = ". ".join(norm4)#create text from the list of separate sentances
print(final)



