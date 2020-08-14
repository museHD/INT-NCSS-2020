'''
The local pond has invasive lily pads. And they're multiplying!

Each day, they cover 20% more area than they did the previous day. Expressed as an equation, this looks like:

(
area tomorrow
)
=
(
area today
)
+
0.2
×
(
area today
)
 
Write a program that asks for the pond's area and the lily pads' current area. Work out how many days until the lily pads completely cover the pond. Output the result as a whole number of days.

Your program should look like this:

Pond area: 75
Lily pad area: 3
The lily pads will cover the pond in 18 days.
​'''

pond = float(input("Pond area: "))
pad = float(input("Lily pad area: "))

counter = 0
ar_today = pad
while ar_today < pond:
	ar_tmrw = ar_today + 0.2 * ar_today
	counter += 1
	ar_today = ar_tmrw
print(f"The lily pads will cover the pond in {counter} days.")