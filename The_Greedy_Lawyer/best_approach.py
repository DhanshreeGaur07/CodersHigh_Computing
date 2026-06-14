from scheduling_algorithms import fcfs_scheduling
from scheduling_algorithms import sjf_scheduling  
from scheduling_algorithms import earliest_finish
from scheduling_algorithms import hff_scheduling
from scheduling_algorithms import fee_per_hour
from scheduling_algorithms import max_revenue_scheduling

print("\n----- MAXIMUM APPOINTMENTS -----\n")

#------------------------------------------------
# CASE 1 : MAXIMUM APPPOINTMENTS
#------------------------------------------------

# for all appointments Revenue = 100

appointments = [
    ("Adam", 0, 3, 100),
    ("Barbie", 1, 4, 100),
    ("Caroline", 3, 5, 100),
    ("David", 5, 7, 100),
    ("Elara", 6, 8, 100),
    ("Felix", 8, 10, 100),
    ("George", 9, 11, 100),
    ("Hannah", 10, 12, 100),
    ("Ivan", 11, 13, 100),
    ("Java", 12, 14, 100),
    ("Kris", 13, 15, 100),
]

fcfs_appointments, fcfs_revenue = fcfs_scheduling(appointments)
sjf_appointments, sjf_revenue = sjf_scheduling(appointments)
greedy_appointments, greedy_revenue = earliest_finish(appointments)

print(f"FCFS : {len(fcfs_appointments)} appointments and Revenue = ${fcfs_revenue}")
print(f"SJF : {len(sjf_appointments)} appointments and Revenue = ${sjf_revenue}")
print(f"EARLIEST FINISH (OPTIMAL) : {len(greedy_appointments)} appointments and Revenue = ${greedy_revenue}")


print("\n----- MAXIMUM REVENUE -----\n")


#------------------------------------------------
# CASE 2 : MAXIMUM REVENUE
#------------------------------------------------

appointments_revenue = [
    ("Adam", 0, 3, 200),
    ("Barbie", 1, 4, 150),
    ("Caroline", 3, 5, 300),
    ("David", 5, 7, 700),
    ("Elara", 6, 8, 900),
    ("Felix", 8, 10, 1000),
    ("George", 9, 11, 400),
    ("Hannah", 10, 12, 50),
    ("Ivan", 11, 13, 800),
    ("Java", 12, 14, 350),
    ("Kris", 13, 15, 1060),
]

fcfs_revenue_appointments, r1 = fcfs_scheduling(appointments_revenue)
hff_appointments, r2 = hff_scheduling(appointments_revenue)
ratio_appointments, r3 = fee_per_hour(appointments_revenue)
optimal_revenue_appointments, r4 = max_revenue_scheduling(appointments_revenue)

print(f"FCFS Revenue : ${r1}, {len(fcfs_revenue_appointments)} appointments")
print(f"Highest Fee First Revenue : ${r2}, {len(hff_appointments)} appointments")
print(f"Fee per Hour Revenue : ${r3}, {len(ratio_appointments)} appointments")
print(f"OPTIMAL Revenue : ${r4}, {len(optimal_revenue_appointments)} appointments")

print("\nOptimal revenue appointments:")
for appointment in optimal_revenue_appointments:
    print(appointment)
