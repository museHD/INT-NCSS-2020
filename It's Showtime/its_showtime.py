'''
Your band has its very first gig! What songs are you going to play?

Write a program that asks for your band name, and then for a list of space-separated song titles.

Note: Your band only sings songs with one-word titles!

The output should look like this:

Band: The One Word Wonders
Songs: Song Lyric Ballad
Please welcome to the stage, The One Word Wonders!
They will be playing...
🎵 Song
🎵 Lyric
🎵 Ballad
Give it up for The One Word Wonders!
​
Here's another example:

Band: Lady Gaga
Songs: Paparazzi Applause Shallow
Please welcome to the stage, Lady Gaga!
They will be playing...
🎵 Paparazzi
🎵 Applause
🎵 Shallow
Give it up for Lady Gaga!
'''

band = input("Band: ")
songs = list(input("Songs: ").split())

print(f"Please welcome to the stage, {band}!")
print("They will be playing...")
for song in songs:
	print("🎵 " + song)

print(f"Give it up for {band}!")