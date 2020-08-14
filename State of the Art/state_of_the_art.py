'''
The art magazine you work for is merging with another magazine. Your boss wants three name proposals for the new merged company that are puns on the word art.

Write a program that keeps asking for names until it's collected three containing the string 'art' (with any capitalisation). It should then print the list of names in reverse alphabetical order, because your boss is eccentric.

Here's an example of how your program should work:

Magazine name: Apart
Magazine name: Pop Tart
Magazine name: Fatalistic
Magazine name: Creative Artery
Proposals: ['Pop Tart', 'Creative Artery', 'Apart']
​'''

runWhile = True
proposals = []
while runWhile:
	name = input("Magazine name: ")
	if 'art' in name.lower():
		proposals.append(name)
	if len(proposals) == 3:
		runWhile = False
proposals.sort()
proposals.reverse()
print(f"Proposals: {proposals}")