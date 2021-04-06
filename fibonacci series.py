# Fibonacci series : 0, 1, 1, 2, 3, 5, 8, . . .
# Initializing the variables

N = int(input("enter the number of elements in a sequence"))  # take an input number. By default input is a string. Convert it into integer
a = 0
b = 1

# writing a loop for the series of 10 elements

for i in range(N):
    print(a)
    a, b = b, a + b  # calculating the next number(i.e., addition) using previous two numbers


# Now this is the simplest form of code
# lets use generator for the same series

def feb(num):
    a, b = 0, 1

    for i in range(num):
        yield "{} : {}".format(a, b)
        a, b = b, a + b

for i in feb(10):
 print(i)


