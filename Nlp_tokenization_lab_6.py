import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize

text = "Hello World! I can't stop."
print(word_tokenize(text))
print(sent_tokenize(text))





