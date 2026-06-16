def greetings():
    return "Hello, World!"

for i in range(5):
    print(greetings())

def add(a, b):
    return a + b

result = add(3,5)
print(f"The result is {result}")

def multiply(a,b):
    return a*b

result = multiply(4,6)
print(f"The result is {result}")

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
result = factorial(5)
print(f"The result is {result}")


def uppercase_string(s):
    return s.upper()

scanf = input("Enter a string: ")
result = uppercase_string(scanf)
print(f"The uppercase version is: {result}")


s = input("whats your name?")
print(f"hello, {s}")

print(greetings().upper())  