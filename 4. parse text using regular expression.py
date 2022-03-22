#parse text using regular expression and tokenize them using re.split 
# Import library
import re
#run the split query
text = re.split('\s+','I like this book.')
print(text)
