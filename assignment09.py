print("Welcome to the Phonebook!\n")

# Initialize your phonebook dictionary

# User Input Loop
while True:
  # Ask the user to enter a name (or 'STOP' to end - in which case break       out of the loop)

  break

# Ask the user to enter a phone number (or 'STOP' to end - in which case     break out of the loop)

# Append the new key-value pair (name & number) to the dictionary

# Outisde the first loop
# Sort the dictionary - Replace 'dictionaryName' with what your phonebook dictionary is named
sortedPhonebook = dict(sorted(dictionaryName.items()))

# User Options Loop
while True:
  print("\nUser Options:")
  print("1. Look Up a Name")
  print("2. Change a Phone Number")
  print("3. Display Entire Phone Book")
  print("4. Quit\n")

  choice = input("Enter your choice (1/2/3): ")

  # If choice is 1, ask the user to enter a name
  # If the name is in the dictionary, print the phone number
  # If the name is not in the dictionary, print 'Name not found'

  # If choice is 2, ask the user to enter a name
  # If the name is in the dictionary, ask the user to enter a new phone         number
  # If the name is not in the dictionary, print 'Name not found'
  # Replace the old phone number with the new one

  # If choice is 3, print the entire dictionary

  # If choice is 4, break out of the loop

  # Repeat or Quit
  repeat = input(
      "Do you want to perform another operation? (Enter 'STOP' to quit): "
  ).strip().lower()
  if repeat == 'stop':
    break
