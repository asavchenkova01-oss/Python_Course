sentence = 'milk bread eggs milk eggs eggs bread chocolate'

words = sentence.split()
counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1
    
for word, count in counts.items():
    print(f"{word}:{count}")
