# Part A
# Write a script that that has two menu options
# Write
# Read
# If option 1. Is chosen, a single string should be inputted and appended to a file
# If option 2. Is chosen, the file should be displayed

print("Enter \'1' to write or \'2' to read: ")
option = int(input("Enter your option: "))

if option == 1:
    myString = input("Enter a sentence: ")
    myFile = open("file.txt", "w")
    myFile.write(myString)
    myFile.close()
elif option == 2:
    try:
        myFile = open("file.txt", "r")
        print(myFile.read())
    except FileNotFoundError:
        print("File not found. Creating file.")
        myFile = open("file.txt", "x")
else:
    print("That is not a valid option. Try again.")

# Part B
# Add a check under option 2 for the existence of the file. If the file does not exist, it should be created.

# Part C
# Add formatting to option 2 such that the text is center aligned in an 80 character window.