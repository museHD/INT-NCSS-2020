slang = {'phone': 'dog and bone', 'queen': 'baked bean', 'suit': 'whistle and flute', 'money': 'bees and honey', 'dead': 'brown bread', 'mate': 'china plate', 'shoes': 'dinky doos', 'telly': 'custard and jelly', 'boots': 'daisy roots',  'road': 'frog and toad', 'head': 'loaf of bread', 'soup': 'loop the loop', 'walk': 'ball and chalk', 'fork': 'roast pork', 'goal': 'sausage roll', 'stairs': 'apples and pears', 'face': 'boat race'}

sentence = input("Sentence: ")

words = sentence.split()

for word in words:
	low_word = word.lower()
	if low_word in slang:
		words[words.index(word)] = slang.get(low_word)
	else:
		pass

output = ' '.join(words)
print(output)