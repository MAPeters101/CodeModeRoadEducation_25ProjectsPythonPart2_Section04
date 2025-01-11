print("Welcome to the Phonebook!\n")

# Initialize your phonebook dictionary
phonebook = {}

# User Input Loop
while True:
  # Ask the user to enter a name (or 'STOP' to end - in which case break out of the loop)
  name = input("Please enter a name (STOP to quit): ")
  if name.upper() == "STOP":
    break

  # Ask the user to enter a phone number (or 'STOP' to end - in which case break out of the loop)
  phone = input("Please enter the number (STOP to quit): ")
  if phone.upper() == "STOP":
    break

  # Append the new key-value pair (name & number) to the dictionary
  phonebook[name] = phone

# Outisde the first loop
# Sort the dictionary - Replace 'dictionaryName' with what your phonebook dictionary is named
sortedPhonebook = dict(sorted(phonebook.items()))

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
  if choice == "1":
    name = input("Please enter a name (STOP to quit): ")
    if name in sortedPhonebook:
      print(f"{name}'s phone number is: {sortedPhonebook[name]}.")
    else:
      print("Name not found.")

  # If choice is 2, ask the user to enter a name
  # If the name is in the dictionary, ask the user to enter a new phone number
  # If the name is not in the dictionary, print 'Name not found'
  # Replace the old phone number with the new one
  if choice == "2":
    name = input("Please enter a name: ")
    if name in sortedPhonebook:
      phone = input("Please enter the number (STOP to quit): ")
      sortedPhonebook[name] = phone
    else:
      print("Name not found.")

  # If choice is 3, print the entire dictionary
  if choice == "3":
    print(sortedPhonebook)

  # If choice is 4, break out of the loop

  # Repeat or Quit
  repeat = input(
      "Do you want to perform another operation? (Enter 'STOP' to quit): "
  ).strip().lower()
  if repeat == 'stop':
    break
