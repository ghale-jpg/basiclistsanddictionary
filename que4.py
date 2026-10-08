sentence = input("Enter a sentence: ")
clean_sentence = " ".join(sentence.split())
lower_sentence = clean_sentence.lower()
words = lower_sentence.split()

word_count = len(words)
python_count = lower_sentence.count("python")

if words:
    longest_word = max(words, key=len)
else:
    longest_word = ""

print("Clean sentence:", clean_sentence)
print("Word count:", word_count)
print("Python count:", python_count)
print("Longest word:", longest_word)