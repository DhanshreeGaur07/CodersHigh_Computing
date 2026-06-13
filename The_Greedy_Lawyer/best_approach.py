from scheduling_algorithms import fcfs_scheduling
from scheduling_algorithms import sjf_scheduling  
from scheduling_algorithms import earliest_finish


# Function to Calculate Total revenue from a list of appointments

def calculate_revenue(appointments):
    return sum(app[3] for app in appointments)


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


#---------------------------------------------------
# COMPARING ALL APPROACHES
#---------------------------------------------------

methods = {
    "First Come First Serve": fcfs_scheduling,
    "Shortest Job First": sjf_scheduling,
    "Earliest Finish Time": earliest_finish
}

for name, algorithm in methods.items() :

    result = algorithm(appointments)
    print("\n",name)

    for r in result:
        print(r)

    print("Appointments =",len(result))

    print("Revenue = $",calculate_revenue(result))

    # selected_appointments = algorithm(appointments)
    # revenue = calculate_revenue(selected_appointments)

    # print(f"{name} selected appointments: {selected_appointments}")
    # print(f"{name} total revenue: {revenue}\n")