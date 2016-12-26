from nltk import pos_tag, word_tokenize
import nltk

text = word_tokenize("And now for something completely different")
ans = nltk.pos_tag(text)
print ans
