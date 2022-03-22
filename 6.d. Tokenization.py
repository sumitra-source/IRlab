import nltk
sentence_data = "The First sentence is about Python. The Second: about Django. You can learn Python,Django and Data Ananlysis here. "
nltk_sentence_tokens = nltk.sent_tokenize(sentence_data)
nltk_word_tokens = nltk.word_tokenize(sentence_data)
print ("Word tokens are ")
print(nltk_word_tokens)
print ("Sentence tokens are ")
print(nltk_sentence_tokens)

