'''
A sound engineer is testing a microphone while on an outdoor film set. They've set the amplification very low, so it only picks up loud sounds, and are counting the number of shouted words they hear in nearby conversations.

Write a program to ask the user for a sentence and then print how many words are shouted, that is, all uppercase:

Sentence: Where is my dog? ROVER, COME HERE!
Number of shouted words: 3
​
Here's another example:

Sentence: I'm going for a walk to get lunch.
Number of shouted words: 0
'''

sentence = list(input("Sentence: ").split())
loudwords = 0
for word in sentence:
	if word.isupper():
		loudwords += 1

print(f"Number of shouted words: {loudwords}")

