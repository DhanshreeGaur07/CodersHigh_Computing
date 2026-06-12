# Pólya's Urn Model Simulation

## Overview

This project implements the **Pólya's Urn Model**, a well-known probabilistic model that demonstrates the concept of **reinforcement**—where outcomes that occur more frequently become increasingly likely in the future. The repository contains two implementations:

* **Single Simulation of Pólya's Urn**
* **Monte Carlo Simulation for Expected Probability**

The project is designed to help beginners understand stochastic processes, probability, and simulation techniques through simple Python implementations and graphical visualizations.

---

# What is the Pólya's Urn Model?

Imagine an urn containing **red** and **black** balls.

At each iteration:

1. A ball is selected randomly.
2. The selected ball is placed back into the urn.
3. One additional ball of the **same color** is added.

Since the chosen color gains an extra ball, its chance of being selected again increases. This creates a **reinforcement effect**, where colors that are selected more often become even more likely to be selected in future iterations.

---

# Mathematical Representation

Let:

* **R** = Number of red balls
* **B** = Number of black balls

The probability of drawing each color is calculated as:

* Probability of Red:

[
P(\text{Red}) = \frac{R}{R+B}
]

* Probability of Black:

[
P(\text{Black}) = \frac{B}{R+B}
]

After each draw:

* If a red ball is selected, **R = R + 1**
* If a black ball is selected, **B = B + 1**

The probabilities are updated after every iteration based on the new composition of the urn.

---

# Project Structure

```text
Polya-Urn-Model/
│
├── single_simulation.py
├── monte_carlo_estimate.py
├── README.md
└── requirements.txt
```

---

# Project Files

## 1. `single_simulation.py`

This program performs **one complete simulation** of the Pólya's Urn process.

### Features

* Initializes the urn with a specified number of red and black balls.
* Calculates the probability of drawing each color before every iteration.
* Randomly selects a ball.
* Reinforces the selected color by adding another ball of the same color.
* Displays how the urn composition changes over time.
* Plots the probability of drawing each color across all iterations.

This simulation shows how a single random experiment evolves.

---

## 2. `monte_carlo_simulation.py`

This program estimates the **expected probability** using **Monte Carlo Simulation**.

Instead of running the experiment once, it repeats the entire simulation thousands of times and averages the probabilities obtained at each iteration.

### Features

* Performs multiple independent simulations.
* Computes the average probability at every iteration.
* Produces smoother probability curves.
* Demonstrates the expected long-term behavior of the Pólya's Urn Model.

---

# What is Monte Carlo Simulation?

Monte Carlo Simulation is a computational method used to study systems involving randomness.

Instead of relying on a single experiment, the process is repeated many times. The results from all simulations are then averaged to estimate the expected outcome.

In this project, Monte Carlo Simulation helps reduce the effect of randomness from individual runs and provides a more reliable estimate of the probability of drawing each color.

---

# Installation

Clone the repository:

```bash
git clone https://github.com/DhanshreeGaur07/CodersHigh_Computing.git
```

Move to the project directory:

```bash
cd Polya_Urn_Model
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

# Requirements

The project uses the following Python libraries:

* numpy
* matplotlib
* random

---

# Running the Programs

Run the single simulation:

```bash
python single_simulation.py
```

Run the Monte Carlo simulation:

```bash
python Monte_Carlo_Estimate.py
```

---

# Expected Output

The programs generate:

* The probability of drawing a red ball at each iteration.
* The probability of drawing a black ball at each iteration.
* A graph showing how these probabilities evolve over time.
* In the Monte Carlo simulation, an additional graph showing the **expected probabilities** averaged across many independent simulations.

---

# Key Learning Outcomes

By completing this project, you will understand:

* Basic probability concepts.
* Random sampling using Python.
* Reinforcement processes.
* Stochastic (random) simulations.
* Monte Carlo Simulation.
* Probability visualization using Matplotlib.
* The difference between a **single simulation** and an **expected outcome** obtained from multiple simulations.

---

# Author

This project was developed as an educational implementation of the **Pólya's Urn Model** and **Monte Carlo Simulation** to demonstrate reinforcement-based probabilistic processes using Python.