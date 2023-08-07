import re
#Functions
# Function #1 Where I'm calculating the number of new lines and whitespaces
def calc_whitespaces(inp):
    res = inp.replace(' ', '&').replace('\n', '&')
    count = res.count(r"&")
    print(f"This is the qty of whitespaces {count}")
    return res

# Function #2 where I get rid of special characters that I used for calc,
# and I'm normalizing the text by correcting mistakes with is=iz
def iz_issue(inp):
    res = re.sub("&+", " ", inp).lower()
    list_query = res.split()
    for i in range(len(list_query)):
        if list_query[i] == 'iz':
            list_query[i] = 'is'
    return list_query

# function #3 that collect all last words of the sentences into the separate list
def last_word(subs):
    res = [i for i in without_iz if subs in i]
    return res


# function #4 Creating new sentence
def new_sentence(inp):
    new_list = []
    res2 = ''
    for n in inp:
        new_list.append(n.split('.')[0])
        res1 = " ".join(new_list)
        res2 = res1.replace('87', '87.')
    return res2

# Function #5 which combine words from text and additional words into a new sentence
def new_sentence1(adds, insert_positions, list_add):
    for i in range(len(adds)):
        index = insert_positions[i]
        element = adds[i]
        list_add.insert(index, element)
    return list_add

# Function #6 Which add my sentence to the text in particular place
def text_add(list_add1):
    without_iz.insert(without_iz.index('paragraph.') + 1, list_add1)
    str_add2 = " ".join(without_iz)
    return str_add2

# function #7 which convert first letters of the sentences into Capital letters and shows final version of the text
def final_text(inp):
    res = [i.lstrip() for i in inp]
    res = [n.capitalize() for n in res]
    res = ". ".join(res)
    return res

#Program
query = ("homEwork:"
         "\n"
         "  tHis iz your homeWork, copy these Text to variable." 
         "\n" 
         "\n" 
         "\n" 
         "\n" 
         "  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS "
         "of each existING SENtence and add it to the END OF this Paragraph." 
         "\n"
         "\n"
         "\n"
         "\n"
         "  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE." 
         "\n"
         "\n"
         "\n"
         "\n"
         "  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL"
         " whitespaces. I got 87.")

without_whitespaces = calc_whitespaces(query)
without_iz = iz_issue(without_whitespaces)
print(f"This is List of Text Without IZ: {without_iz}")
list_of_words = last_word('.')
new_stn = new_sentence(list_of_words)
print(f"This is Words for new sentence: {new_stn}")
list_add = new_stn.split()  # Sample list
adds = ["This is a", "and a", "in the", "and", 'more than']  # Elements to insert
insert_positions = [0, 5, 7, 9, 11]  # Index positions to insert the elements
new_stn1 = new_sentence1(adds, insert_positions, list_add)
print(f"This is what came to my mind:  {new_stn1}")
list_add1 = " ".join(list_add)
x = text_add(list_add1)
print(f"This is Text without Capital Letters: {x}")
norm3 = x.split(".")
the_end = final_text(norm3)
print(f"This is Final Text: {the_end}")
