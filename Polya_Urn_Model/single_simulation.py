import random
import matplotlib.pyplot as plt

# Initial balls
red = 10
black = 10

iterations = 10000

print(f"Initial State -> Red: {red}, Black: {black}\n")

for i in range(1, iterations + 1):

    # Current probabilities
    p_red = red / (red + black)
    p_black = black / (red + black)

    print(f"Iteration {i}")
    print(f"Probability(Red)   = {p_red:.4f}")
    print(f"Probability(Black) = {p_black:.4f}")

    # Draw a ball
    if random.random() < p_red:
        red += 1
        print("Drawn: RED")
    else:
        black += 1
        print("Drawn: BLACK")

    print(f"Updated Urn -> Red={red}, Black={black}")
    print("-" * 40)

red_prob = []
black_prob = []

for _ in range(iterations):

    red_prob.append(red / (red + black))
    black_prob.append(black / (red + black))

    if random.random() < red / (red + black):
        red += 1
    else:
        black += 1

plt.plot(red_prob, label="Red Probability")
plt.plot(black_prob, label="Black Probability")
plt.xlabel("Iteration")
plt.ylabel("Probability")
plt.title("Pólya's Urn Process")
plt.legend()
plt.grid(True)
plt.show()