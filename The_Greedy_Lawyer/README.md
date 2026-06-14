# Lawyer Appointment Scheduling using Greedy and Dynamic Programming

## Overview

This project implements and compares different scheduling algorithms for selecting lawyer consultancy appointments. The objective is to maximize the number of appointments when every consultation has the same fee and to maximize total revenue when consultation fees vary.

The project demonstrates how different greedy strategies perform on the same dataset and compares them with the optimal algorithm for each scenario using visualizations and Gantt charts.

---

## Problem Statement

A lawyer offers consultancy appointments only on **Mondays**. Clients submit their appointment requests before **Friday**, specifying:

* Appointment start time
* Appointment end time (or duration)
* Consultation fee (for the extended problem)

Since appointments cannot overlap, the lawyer must choose a subset of appointments.

---

### Questions Addressed

* Different approaches for selecting appointments.
* The optimal algorithm for maximizing appointments.
* Comparison of greedy algorithms producing the same number of appointments.
* Extension of the problem when consultation fees differ.
* Best algorithm for maximizing total revenue.

---

## Project Structure

```
.
├── scheduling_algorithms.py     # Case 1: Equal fee scheduling algorithms
├── best_approach.py             # Case 2: Revenue maximization algorithms
├── README.md
```

---

## Algorithms Implemented

### Case 1 – Equal Consultation Fee

Every appointment pays **$100**.

**Objective**

Maximize the number of appointments scheduled, thereby maximizing revenue.

Since every appointment has the same consultation fee, maximizing revenue is equivalent to maximizing the number of appointments.

Algorithms implemented:

* First Come First Serve (FCFS)
* Shortest Job First (SJF)
* Earliest Finish Time (Greedy Optimal)

The Earliest Finish Time algorithm is the optimal solution for the Interval Scheduling Problem.

---

### Case 2 – Variable Consultation Fee

When appointments have different consultation fees, maximizing the number of appointments no longer guarantees maximum revenue.

Algorithms implemented:

* FCFS with Revenue
* Highest Fee First
* Highest Fee per Hour
* Weighted Interval Scheduling (Dynamic Programming)

Weighted Interval Scheduling provides the optimal solution for maximizing total consultation fees.

---

## Features

* Implementation of multiple scheduling algorithms
* Comparison of algorithm performance
* Appointment selection visualization
* Gantt charts for schedule comparison
* Revenue comparison for different strategies
* Support for both equal-fee and variable-fee appointment scheduling

---

## Comparison

### Equal Fee

| Algorithm            | Goal                                                          |
| -------------------- | ------------------------------------------------------------- |
| FCFS                 | Schedule appointments in arrival order                        |
| SJF                  | Prefer shorter appointments                                   |
| Earliest Finish Time | Maximize the number of non-overlapping appointments (Optimal) |

### Variable Fee

| Algorithm                    | Goal                               |
| ---------------------------- | ---------------------------------- |
| FCFS Revenue                 | Revenue using arrival order        |
| Highest Fee First            | Prefer expensive appointments      |
| Fee per Hour                 | Prefer higher earning rate         |
| Weighted Interval Scheduling | Maximum possible revenue (Optimal) |

---

## Visualizations

The project includes visual analysis of scheduling algorithms, including:

* Gantt Charts
* Appointment Timeline Comparison
* Number of Appointments Selected
* Revenue Comparison (Variable Fee Case)

These visualizations help compare algorithm performance and understand scheduling decisions.

---

## Time Complexity

### Equal Fee

| Algorithm            | Time Complexity |
| -------------------- | --------------- |
| FCFS                 | O(n log n)      |
| SJF                  | O(n log n)      |
| Earliest Finish Time | O(n log n)      |

### Variable Fee

| Algorithm                    | Time Complexity |
| ---------------------------- | --------------- |
| FCFS Revenue                 | O(n log n)      |
| Highest Fee First            | O(n log n)      |
| Fee per Hour                 | O(n log n)      |
| Weighted Interval Scheduling | O(n log n)      |

---

## Learning Outcomes

This project demonstrates concepts from:

* Greedy Algorithms
* Interval Scheduling
* Dynamic Programming
* Weighted Interval Scheduling
* Algorithm Analysis
* Time Complexity
* Data Visualization using Python

---

## Conclusion

For equal consultation fees, the Earliest Finish Time algorithm guarantees the maximum number of appointments and therefore the maximum revenue.

When consultation fees vary, greedy methods are no longer sufficient. Weighted Interval Scheduling using Dynamic Programming guarantees the maximum possible revenue by selecting the most profitable set of non-overlapping appointments.

This project illustrates how changing the optimization objective—from maximizing appointments to maximizing revenue—requires a different algorithmic approach.

---