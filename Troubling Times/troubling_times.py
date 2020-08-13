'''
Your little cousin is getting stuck learning their times tables. ✖️😫

You offer to write a program to help them practise multiplication!

Write a program that asks which times table your cousin would like to practise, and then print the times table for numbers from 1 to 12, like this:

Times table: 3
Ok, give it a go!
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
3 x 11 = 33
3 x 12 = 36
Good work, little cuz!
'''
table = int(input("Times table: "))

print("Ok, give it a go!")
for i in range(1,13):
	print(f"{table} x {i} = {table*i}")

print("Good work, little cuz!")