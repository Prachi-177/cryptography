import math

def are_relatively_prime(a, b):
    return math.gcd(a, b) == 1
num1,num2=map(int,input("enter two number").split())

if are_relatively_prime(num1, num2):
    print(f"{num1} and {num2} are relatively prime.")
else:
    print(f"{num1} and {num2} are not relatively prime.")
