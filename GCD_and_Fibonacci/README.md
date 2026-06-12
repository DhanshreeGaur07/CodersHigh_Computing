# Euclid's GCD Algorithm and Fibonacci Analysis

## Overview

This project implements Euclid's Greatest Common Divisor (GCD) algorithm and analyzes its computational behavior.

The project demonstrates:

- Computation of the GCD of two integers.
- Counting the number of iterations (steps) required.
- Empirical identification of worst-case input pairs.
- Verification that consecutive Fibonacci numbers produce the maximum number of iterations.
- Visualization of the relationship between input pair ratio and the number of Euclid algorithm steps.

---

## Theory

Euclid's Algorithm computes the Greatest Common Divisor (GCD) of two integers using repeated modulo operations.

For two numbers `a` and `b`:

```
while b != 0:
    a, b = b, a % b
```

The algorithm terminates when the remainder becomes zero.

---

## Worst Case

According to **Lamé's Theorem**, the maximum number of iterations occurs when the inputs are **consecutive Fibonacci numbers**.

Example:

| Pair | Steps |
|------|------:|
| (13, 8) | 5 |
| (21, 13) | 6 |
| (34, 21) | 7 |
| (55, 34) | 8 |
| (89, 55) | 10 |

The ratio of consecutive Fibonacci numbers approaches the **Golden Ratio (≈1.618)**.

---

## Features

- Euclid's GCD implementation
- Step counting
- Worst-case input search
- Fibonacci number generation
- Scatter plot of ratio vs steps

---

## Project Files

```
GCD_and_Fibonacci/
│
├── Euclid_GCD_Algorithm.ipynb
├── euclid.py
└── README.md
```

---

## Requirements

- Python 3.x
- matplotlib

Install matplotlib:

```bash
pip install matplotlib
```

---

## Running the Program

```bash
python euclid.py
```

---

## Sample Output

```
Maximum number of steps taken : 10

First pair that takes maximum number of steps :
(89, 55)

Fibonacci Numbers
0
1
1
2
3
5
8
13
21
34
55
89
```

---

## Graph

The scatter plot illustrates the relationship between

```
Input Pair Ratio (a/b)
```

and

```
Number of Euclid Algorithm Steps
```

The graph shows that the maximum number of steps occurs near the Golden Ratio (≈1.618), confirming that consecutive Fibonacci numbers represent the worst-case inputs.

---

## Time Complexity

Euclid's Algorithm:

```
O(log(min(a,b)))
```

Worst-case search:

```
O(n² log n)
```

---

## Conclusion

The experimental results confirm Lamé's theorem.

The pair **(89,55)** requires the maximum number of iterations among all pairs between **10 and 99**, demonstrating that consecutive Fibonacci numbers produce the worst-case performance of Euclid's GCD algorithm.
