#nice one. spot on.

myList = []
x = 0

# Accept an integer as input() five times.
while x < 5:
    myInput = int(input("Enter a number: "))
    myList.append(myInput)
    x = x + 1

# Display the length of the list.    
print(len(myList))

# Display the first and the last integers in the list.
print(myList[0], myList[-1])

# Add the integers in the list.
totalSum = 0
for i in range(len(myList)):
    totalSum += myList[i]
print(totalSum)
