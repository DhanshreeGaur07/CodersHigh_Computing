import random
import numpy as np
import matplotlib.pyplot as plt

initial_red = 10
initial_black = 10

#number of balls drawn in each simulation
iterations = 100

# number of simulations for Monte Carlo estimation
# independent experiments to average out the randomness
simulations = 10000

avg_red = np.zeros(iterations)
avg_black = np.zeros(iterations)

for _ in range(simulations):

    red = initial_red
    black = initial_black

    for i in range(iterations):

        avg_red[i] += red / (red + black)
        avg_black[i] += black / (red + black)

        if random.random() < red / (red + black):
            red += 1
        else:
            black += 1

print(avg_black)
print(avg_red)

avg_red /= simulations
avg_black /= simulations

plt.plot(avg_red, label="Expected Red Probability")
plt.plot(avg_black, label="Expected Black Probability")
plt.xlabel("Iteration")
plt.ylabel("Expected Probability")
plt.title("Monte Carlo Estimate of Pólya's Urn")
plt.legend()
plt.grid(True)
plt.show()