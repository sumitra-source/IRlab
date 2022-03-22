# import the necessary libraries
import nltk
import string
import re

# remove punctuation
def remove_punctuation(text):
	translator = str.maketrans('', '', string.punctuation)
	return text.translate(translator)

input_str = "Hey, did you know that the summer break is coming? Amazing right !! It's only 5 more days !!"
print(remove_punctuation(input_str))
