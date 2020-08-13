popular_names = ['Oliver', 'Charlotte', 'Noah', 'Olivia', 'William', 'Mia', 'Jack', 'Amelia', 'Zoe', 'Leo', 'Isla', 'Lucas', 'Ava', 'Henry', 'Chloe', 'Thomas', 'Grace', 'James', 'Ethan', 'Ella']

def describe_name(name):
  description = ''
  # Find the description words for the name
  if 'z' in name.lower():
    description = description + 'groovy '
  # Check for the other descriptions after this
  if name in popular_names:
    description = description + 'popular '
  if len(name) <= 4:
    description = description + 'short '
  if len(name) >= 7:
    description = description + 'long '
  return description

# Write the rest of your program after this

names = list(input("Enter names: ").split())
counter = 0
for name in names:
  if describe_name(name) != '':
    print(f"{name} is a {describe_name(name)}name.")
    counter += 1
print(f"Interesting names: {counter}")
