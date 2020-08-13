'''
Write a program to cheer for your favourite sports teams!

Your program should ask the user to input their team name and then print out a cheer like this:

Team: Dolphins
Give me a D!
Give me a O!
Give me a L!
Give me a P!
Give me a H!
Give me a I!
Give me a N!
Give me a S!
What does that spell? DOLPHINS!
​
Here's another example:

Team: Tigers
Give me a T!
Give me a I!
Give me a G!
Give me a E!
Give me a R!
Give me a S!
What does that spell? TIGERS!
'''

team = input('Team: ')

for letter in team:
	print(f'Give me a {letter.upper()}!')
	
print(f'What does that spell? {team.upper()}!')