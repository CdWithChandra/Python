#Python program to implement ternary operator
from selectors import SelectSelector

word=input("Enter a word/line:")
res="Vowel word" if ('a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word) else "Not vowel word"
print("{} is {}".format(word,res))