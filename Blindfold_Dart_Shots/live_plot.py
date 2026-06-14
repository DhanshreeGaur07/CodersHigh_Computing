import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# PARAMETERS
# -----------------------------
NUM_EXPERIMENTS = 1000
SHOT_COUNTS = [10, 50, 100, 500, 1000, 5000]

# Running averages
running_avg = {shots: [] for shots in SHOT_COUNTS}

plt.style.use("ggplot")
plt.ion()

fig, ax = plt.subplots(figsize=(10,6))

# -----------------------------
# SIMULATION
# -----------------------------
for exp in range(1, NUM_EXPERIMENTS + 1):

    ax.clear()

    for shots in SHOT_COUNTS:

        # Uniform random points inside unit circle
        theta = np.random.uniform(0, 2*np.pi, shots)
        radius = np.sqrt(np.random.uniform(0, 1, shots))

        x = radius * np.cos(theta)
        y = radius * np.sin(theta)

        distances = np.sqrt(x**2 + y**2)

        minimum = np.min(distances)

        # r = np.sqrt(np.random.random(shots))
        # minimum = np.min(r)

        if exp == 1:
            running_avg[shots].append(minimum)
        else:
            prev = running_avg[shots][-1]
            avg = prev + (minimum - prev) / exp
            running_avg[shots].append(avg)

        ax.plot(
            range(1, exp + 1),
            running_avg[shots],
            linewidth=2,
            label=f"{shots} shots"
        )

    ax.set_title("Blindfold Dart Simulation\nRunning Average of Minimum Distance")
    ax.set_xlabel("Experiment Number")
    ax.set_ylabel("Expected Minimum Distance")
    ax.grid(True)
    ax.legend(loc="upper right")

    plt.pause(0.01)

plt.ioff()
plt.show()