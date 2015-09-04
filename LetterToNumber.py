# Create a variable with all the letters in the alphabet
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Ask the user to type in a letter
letter=input("Please type a letter: ")

# Find the position of the letter in the alphabet
pos=alphabet.find(letter)

# As the first position is 0, we need to add 1
pos += 1

#display the number back to the user
print(pos)