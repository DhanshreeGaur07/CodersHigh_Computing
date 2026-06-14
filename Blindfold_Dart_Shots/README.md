# Blindfold Dart Simulation using Monte Carlo Methods

## Assignment

A shooter fires **100 shots** at a circular target of **radius = 1 unit**. None of the shots are perfect; every shot lands **uniformly at random inside the circular target**.

The objective is to estimate the **expected minimum distance from the center** over many repeated experiments.

In simple terms:

> If we throw 100 darts (or fire 100 bullets) at a circular target and every shot lands randomly inside the target, what is the expected distance of the closest shot from the center?

---

# Objectives

- Simulate random shots inside a unit circle.
- Find the minimum distance from the center in each experiment.
- Repeat the experiment many times using Monte Carlo simulation.
- Estimate the expected minimum distance.
- Study how increasing the number of shots affects the estimate.
- Study how increasing the number of experiments improves convergence.
- Compare empirical results with theoretical probability.

---

# Additional Questions Explored

### 1. How does changing the number of shots affect the result?

Increasing the number of shots increases the probability that at least one shot lands very close to the center. Therefore,

- More shots → Smaller expected minimum distance.

---

### 2. What is the effect of increasing the number of experiments?

Increasing the number of experiments improves the accuracy of the Monte Carlo estimate.

As the number of experiments grows, the running average converges to the true expected value according to the **Law of Large Numbers**.

---

### 3. Relationship between number of shots and number of experiments

- **Number of shots (n)** : controls the underlying probability distribution.
- **Number of experiments (N)** : controls the accuracy of the estimation.

Increasing shots changes the expected minimum distance.
Increasing experiments only reduces statistical error.

---

### 4. Is there a simpler 2D version?

Yes.
Instead of throwing darts inside a circular target, consider random points on a **line segment**.

The problem becomes finding the minimum distance to one endpoint.

---

### 5. Difference between the 2D and 3D versions

In two dimensions (circle):

- Probability depends on **area**
- Cumulative distribution:

$$ F(r)=r^2 $$

In three dimensions (sphere):

- Probability depends on **volume**

$$ F(r)=r^3 $$

Therefore the expected minimum distance decreases more rapidly in higher dimensions.

---

# Project Structure

```
Blindfold_Dart_Simulation/
│
├── dart_experiment.html   # Monte Carlo simulation
├── live_plot.py           # Live convergence graph
├── README.md
└── requirements.txt
```

---

# Methodology

For each experiment:

1. Generate **n** random points uniformly inside the unit circle.
2. Compute the distance of every point from the center.
3. Record the minimum distance.
4. Repeat for many experiments.
5. Compute the running average.

---

# Mathematical Model

Each shot lands randomly inside a **unit circle** (radius = 1).

## Step 1: Distance from the Center

If a shot lands at coordinates **(x, y)**, its distance from the center is calculated using the distance formula:

$$ d=\sqrt{x^2+y^2} $$

where:

- d = distance from the center
- (x, y) = coordinates of the shot

---

## Step 2: Closest Shot

For every experiment, **n** shots are fired.

The minimum distance is simply the closest shot to the center:

$$ D =\min(d_1,d_2,d_3,\ldots,d_n) $$

For example,

| Shot | Distance |
|------|----------|
| 1 | 0.61 |
| 2 | 0.18 |
| 3 | 0.47 |
| 4 | 0.09 |
| 5 | 0.73 |

The minimum distance is

$$ D=0.09 $$

---

## Step 3: Repeat Many Experiments

Since every experiment is random, we repeat it many times.

The expected minimum distance is the average of all the minimum distances:

$$ \boxed {E(M)= \frac{\text{Sum of all minimum distances}} {\text{Number of experiments}}} $$

---

## Step 4: Relationship Between Shots and Minimum Distance

As the number of shots increases, the probability of one shot landing close to the center also increases.

- Increasing the number of shots from **100 to 400** (4× more shots) approximately halves the expected minimum distance.
- Increasing the shots from **400 to 1600** (again 4× more shots) halves the distance once more.

This indicates that the relationship is **not linear**.

Instead, it follows an **inverse square-root relationship**.

Therefore, the expected minimum distance decreases approximately according to :

$$ E(M) \propto \frac{k}{\sqrt n} $$

Using the values obtained from the simulation, the proportionality constant is calculated as : 

$$ \boxed{ E(M)\approx\frac{0.886}{\sqrt n}} $$

where:

- E(M) = Expected minimum distance
- n = Number of shots fired

This formula was confirmed through the Monte Carlo simulations performed in this project.

---

# Observations

The simulations show that:

- Increasing the number of shots reduces the expected minimum distance.
- Increasing the number of experiments stabilizes the estimate.
- The empirical values closely match the theoretical prediction.
- The convergence follows the Law of Large Numbers.

---

# Conclusion

The relationship indicates that the expected closest shot to the center decreases proportionally to the inverse square root of the number of shots fired.

Therefore,

- Doubling the number of shots does **not** halve the expected minimum distance.
- To reduce the expected minimum distance by half, approximately **four times as many shots** are required.

The Monte Carlo simulation validates this theoretical result, demonstrating excellent agreement between empirical observations and probability theory.

---

# Technologies Used

- Python 3
- NumPy
- Matplotlib
- Monte Carlo Simulation
- Probability Theory
- Statistical Analysis

---