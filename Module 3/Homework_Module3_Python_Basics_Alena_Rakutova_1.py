import re
query = """homEwork:

  tHis iz your homeWork, copy these Text to variable.




  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.




  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.




  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

#Normalization
normal = '. '.join(list(map(lambda x: x.strip().capitalize(), query.split('.'))))



# Compile the regular expression pattern
pattern = r'\S+(?=\s*$)'
regex = re.compile(pattern)

# Collect matched words into a list
matched_words = []

# Apply the regular expression to each string in the list
list_query = normal.split('.')
for string in list_query:
    match = regex.search(string)
    if match:
        matched_word = match.group(0)
        matched_words.append(matched_word)

# Create a sentence from the collected matched words
sentence = " ".join(matched_words)
#print("Collected Sentence:", sentence)


#Include new sentence into the text
updated_text = ''
# Find the index of the target word in the existing text
target_word = "Paragraph."
index = query.find(target_word)

# If the target word is found, insert the new sentence after it
if index != -1:
    index += len(target_word)
    modified_text = normal[:index] + " " + sentence + normal[index:]
    modified_text = modified_text
else:
    modified_text = normal


#fixing IZ issues
iz = modified_text.split()
for a in range(len(iz)):
    if iz[a] == 'iz':
        iz[a] = 'is'
fixed_text = " ".join(iz)
print('Final Text:',fixed_text)


#Get count of whitespaces
count = 0
for char in fixed_text:
   if char.isspace():
       count += 1
count = count
print("Total whitespace characters:",count)

