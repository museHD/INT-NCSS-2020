breads = {}

while len(breads) < 5:

	name = input("Name: ")
	bread = input("What kind of bread are you bringing? ")
	
	if breads.get(bread,0) == 0:
		breads[bread]=name
		print(f"{name} is bringing a {bread}!")
	elif breads.get(bread,0) != 0:
		print("Someone else is bringing that already.")

print("The party is organised! Here's what's on the menu:")

for thisbread, thisname in breads.items():
	print(f"{thisbread}: {thisname}")