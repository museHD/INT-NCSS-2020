'''
Your family is going on a driving holiday! Holidays are fun! But driving? Not so much.

You want to know when you're getting to the next stop, so you keep asking your family an important question... Are we there yet?

Write a program that asks this question over and over again until you get an answer that includes the word 'yes' (with any capitalisation) anywhere in the input. Print out 'Aww...' if you're not there yet and print 'Hooray!!!' when you finally arrive!

Here's an example:

Let's go!
Are we there yet? No
Aww...
Are we there yet? Ah I don't think so
Aww...
Are we there yet? Nope not yet
Aww...
Are we there yet? Ummm oh yes here we are
Hooray!!!
'''
print("Let's go!")

running = True

while running:
	ans = input("Are we there yet? ")
	if "yes" not in ans.lower():
		print("Aww...")
	else:
		print("Hooray!!!")
		running = False