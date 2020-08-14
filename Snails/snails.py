racers = ['Dash', 'Speedy', 'Lightning', 'Flash', 'Sonic']
print(f"And the line up is: {racers}")
sleep = input("Who's gone to sleep? ")
if sleep not in racers:
  print("All snails still awake.")
else:
  print(f"{sleep} has been disqualified!")
  racers[racers.index(sleep)] = "Disqualified"
print(f"Remaining racers: {racers}")