'''Let's make a program that detects if a user's input is a notable nickname!

A notable nickname is a name that is at least 5 characters long and starts with the letter N.

Here's an example of how your program should work:

Type a nickname: Noddy
That nickname is notable!
Names that are shorter than 5 characters long or don't start with N are not so notable:

Type a nickname: Bazza
That nickname is not so notable!
Your program should ask the user for input and then use a function to help you decide if it is notable. We've started by defining a function for you, called is_notable.

Finish the function and call it in your program.

Here are some examples of how your function should work:

When called like this:	
is_notable('Noddy')	
is_notable('Bazza')	

 
the function should return:
'notable'
'not so notable'
'''

def is_notable(name):
	if name[0] == 'N' and len(name) >= 5:
		print("That nickname is notable!")
	else:
		print("That nickname is not so notable!")

is_notable(input("Type a nickname: "))