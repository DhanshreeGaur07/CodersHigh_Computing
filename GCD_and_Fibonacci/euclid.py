import matplotlib.pyplot as plt
import random

def euclid_gcd(num1, num2) :
    steps = 0
    while num2 != 0 :
        steps += 1
        num1, num2 = num2, num1 % num2
    return steps, num1

n = int(input("Number of iterations : "))

max = 0
ratios = []
steps_data = [] 

for i in range(1, n + 1) :
    for j in range(1, n + 1) :

        steps, gcd = euclid_gcd(i, j)

        ratios.append(i/j)
        steps_data.append(steps)

        # print(f"GCD ({i},{j}) : {gcd}   Steps : {steps}")

        if max < steps :
            max = steps

print("Maximum number of steps taken : ", max)

for i in range(1, n+1) :
    for j in range(1, n+1) :
        steps, gcd = euclid_gcd(i, j)
        if steps == max :
            print(f"({i} , {j})")
            break
        else :
            continue
        break

def print_euclid_steps(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    n = 0
    total_quotient_ratio = 0
    while num2 > 0:
        quotient = num1 // num2
        remainder = num1 % num2

        print(f"{num1} = {num2} * {quotient} + {remainder}")
        total_quotient_ratio += num1/num2
        
        num1, num2 = num2, remainder
        n += 1
    print("Number of steps : ", n)
    print("Average of Ratios : ", total_quotient_ratio/n)

print_euclid_steps(21, 13)
print_euclid_steps(55, 89)

def fibonacci(n) :
    if n <= 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(15) :
    print(fibonacci(i), end=" ")

plt.scatter(ratios, steps_data, alpha=0.5) # Updated to use 'steps_data'
plt.xlabel('Ratios')
plt.ylabel('Steps')
plt.title('Input Ratios vs Number of Steps')
plt.show()