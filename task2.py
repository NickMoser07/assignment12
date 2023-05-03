numbers = []
while True:
    prompt = input("Enter a number or press enter to finish: ")
    if prompt == "":
        break
    numbers.append(int(prompt))
max = numbers[0]
sum = 0
for i in numbers:
    sum += i
    if i > max:
        max = i
print("Numbers entered:", numbers)
print("Number of values entered:" + str(len(numbers)))
print("Maximum value entered:" + str(max))
print("Minimum value entered:" + str(min(numbers)))
print("Sum of all values:" + str(sum))
print("Average value:" + str(sum/len(numbers)))