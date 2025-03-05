word="word"
char_tokens=list(word)
print(char_tokens)

sentence="hello,world"
import string
cleaned_sentence="".join(char for char in sentence if char not in string.punctuation and char !=' ')
char_tokens=list(cleaned_sentence)
print(char_tokens)

para="This is winter season"
word_tokens=para.split()
print(word_tokens)

para="This is winter season.The snow is so white"
words_tokens=para.split(".")
print(words_tokens)
