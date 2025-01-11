print("Welcome to the Phonebook!\n")
phonebook = {}

while True:
  name = input("Please enter a name (STOP to quit): ")
  if name.upper() == "STOP":
    break
  phone = input("Please enter the number (STOP to quit): ")
  if phone.upper() == "STOP":
    break
  phonebook[name] = phone

sortedPhonebook = dict(sorted(phonebook.items()))

while True:
  print("\nUser Options:")
  print("1. Look Up a Name")
  print("2. Change a Phone Number")
  print("3. Display Entire Phone Book")
  print("4. Quit\n")

  choice = input("Enter your choice (1/2/3): ")

  if choice == "1":
    name = input("Please enter a name (STOP to quit): ")
    if name in sortedPhonebook:
      print(f"{name}'s phone number is: {sortedPhonebook[name]}.")
    else:
      print("Name not found.")

  if choice == "2":
    name = input("Please enter a name: ")
    if name in sortedPhonebook:
      phone = input("Please enter the number (STOP to quit): ")
      sortedPhonebook[name] = phone
    else:
      print("Name not found.")

  if choice == "3":
    print(sortedPhonebook)

  if choice == "4":
    break

  repeat = input(
      "Do you want to perform another operation? (Enter 'STOP' to quit): "
  ).strip().lower()
  if repeat == 'stop':
    break
