import re

# fixing IZ issues in the text
def iz(query):
    iz_list = query.split()
    for a in range(len(iz_list)):
        if iz_list[a] == 'iz':
            iz_list[a] = 'is'
    fixed_query = " ".join(iz_list)
    return fixed_query


#Normalization any kind of the text to Sentence view
def norm(fixed_query):
    normal_string = '. '.join(list(map(lambda x: x.strip().capitalize(), fixed_query.split('.'))))
    return normal_string


#Get the last word of each sentence
# Compile the regular expression pattern
def new_sent(normal_string):
    pattern = r'\S+(?=\s*$)'
    regex = re.compile(pattern)
# Collect matched words into a list
    matched_words = []
# Apply the regular expression to each string in the list
    list_query = normal_string.split('.')
    for string in list_query:
        match = regex.search(string)
        if match:
            matched_word = match.group(0)
            matched_words.append(matched_word)
# Create a sentence from the collected matched words
    new_sentence = " ".join(matched_words)
    return new_sentence
#print("Collected Sentence:", sentence)


#Function adds any string after particular word
def insert_sentence_after_word(normal_string, target_word, new_sentence):
    # Find the index of the target word in the existing text
    index = normal_string.find(target_word)
    # If the target word is found, insert the new sentence after it
    if index != -1:
        index += len(target_word)
        modified_text = normal_string[:index] + " " + new_sentence + normal_string[index:]
        return modified_text
    else:
        return normal_string

#Get count of whitespaces
def count_whitespace_characters(fixed_query):
    count = 0
    for char in fixed_query:
        if char.isspace():
            count += 1
    return count


query = """homEwork:

  tHis iz your homeWork, copy these Text to variable.




  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.




  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.




  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


target_word = 'Paragraph.'
fixed_query = iz(query)
normal_string = norm(fixed_query)
new_sentence = new_sent(normal_string)
modified_text = insert_sentence_after_word(normal_string, target_word, new_sentence)
total_whitespace = count_whitespace_characters(normal_string)
print("Total whitespace characters:", total_whitespace)
print("Final text:", modified_text)
