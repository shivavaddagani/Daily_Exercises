# Exercise 1 :
## Number guessing game
import random
number = random.randint(10,30)
print(number)
while True:
    inputnum = int(input("enter a number between 10 -30"))
    if number == inputnum :
        print("correct")
        break
    elif number < inputnum :
        print("too high")
    elif number > inputnum :
        print("too low")

# Exercise 2 : Defining sum fucntion

def sum(*x):
    total=0
    for i in x:
        total = total + i
    return total

print("the sum of the input numbers is {}".format(sum(1,2,3)))

## The above function is a simple example of how we can use Python’s "splat" operator (aka ) * \
# to allow a function to receive any number of arguments

# Exercise 3: Average runtime
i = 0
avg = 0
while True:

    userinput = input("Enter 10 km run time or q to exit")

    if userinput == 'q':
        print("Average of {}, over {} runs".format((avg / i), i))
        break
    else:
        i = i + 1
        avg = avg + int(userinput)


0.1+0.2

# Exercise 5 : Hexadecimal numbers
N = input("enter a number for hex function")
d = 0
h = input("Enter a hex number to convert to decimal: ")
for power, digit in enumerate(reversed(h)):
 d += int(digit, 16) * (16 ** power)
 print(d)

# Exercise
