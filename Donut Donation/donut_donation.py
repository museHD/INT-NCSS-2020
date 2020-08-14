'''
The local sports centre is having a fundraiser to buy a donut machine! Selling donuts to fans will fund the running of the centre. Businesses who pledge money get their name on the wall!

Write a program that will help track of how much money has been raised, and who all the donors are for the wall.

Your program should keep asking who the next donor is until no business name is entered. When a name is entered, ask for how much they want to pledge, update the total amount raised, record the name if this is their first donation, and say a suitable thanks!

Here's an example of how your program should work:

Thanks all for coming to donut donation day!
Who's next to donate? Kate's Kakes
How much are you donating? 45.25
Thanks Kate's Kakes! A first donation of $45.25!
Who's next to donate? Fred's Fruit
How much are you donating? 37.50
Thanks Fred's Fruit! A first donation of $37.50!
Who's next to donate? Kate's Kakes
How much are you donating? 22.50
Another generous donation from Kate's Kakes of $22.50!
Who's next to donate? 
That's it folks! We raised $105.25!
All thanks to our delicious donors:
🍩 Fred's Fruit
🍩 Kate's Kakes
Thanks all for coming to donut donation day!
Who's next to donate? Kate's Kakes
How much are you donating? 45.25
Thanks Kate's Kakes! A first donation of $45.25!
Who's next to donate? Fred's Fruit
How much are you donating? 37.50
Thanks Fred's Fruit! A first donation of $37.50!
Who's next to donate? Kate's Kakes
How much are you donating? 22.50
Another generous donation from Kate's Kakes of $22.50!
Who's next to donate? 
That's it folks! We raised $105.25!
All thanks to our delicious donors:
🍩 Fred's Fruit
🍩 Kate's Kakes
​
When all the donations are done, print out the total amount raised. Then, print out all the donors in alphabetical order.
'''
print("Thanks all for coming to donut donation day!")
total = 0
donors = []
name = input("Who's next to donate? ")
while name != '':
	money = float(input("How much are you donating? "))
	if name not in donors:
		print(f"Thanks {name}! A first donation of ${money}.")
		donors.append(name)
	elif name in donors:
		print(f"Another generous donation from {name} of ${money}.")
	
	total = money + total
	name = input("Who's next to donate? ")

print(f"That's it folks! We raised ${total}!")
print("All thanks to our delicious donors:")
for donor in donors:
	print(f"🍩 {donor}")