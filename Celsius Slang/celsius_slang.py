def to_celsius(f):
  # Calculate the temperature in Celsius
  # Write the rest of your program here

  # Calculate the temperature in Celsius
  cel = (f - 32)*5/9
  return round(cel, 1)



# Write the rest of your program here

far = float(input("Temp (F): "))

cel = to_celsius(far)
if cel < 5:
  print(f"{cel} C - Crikey it's cold!")
elif cel < 20:
  print(f"{cel} C - Getting a bit nippy!")
elif cel < 35:
  print(f"{cel} C - You beaut beach weather!")
elif cel >= 35:
  print(f"{cel} C - Strewth, it's a scorcher!")
  