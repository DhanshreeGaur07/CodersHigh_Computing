import matplotlib.pyplot as plt

from scheduling_algorithms import (
    fcfs_scheduling,
    sjf_scheduling,
    fee_per_hour,
    earliest_finish,
    hff_scheduling,
    max_revenue_scheduling
)

save_path = r"..\charts\\"

#---------------------------------------------------
# SAMPLE DATASET
#---------------------------------------------------

appointments_equal = [
    ("A", 1, 4, 100),
    ("B", 3, 5, 100),
    ("C", 0, 6, 100),
    ("D", 5, 7, 100),
    ("E", 3, 8, 100),
    ("F", 5, 9, 100),
    ("G", 6, 10, 100),
    ("H", 8, 11, 100),
    ("I", 8, 12, 100),
    ("J", 2, 13, 100),
    ("K", 12, 14, 100)
]

appointments_fee = [
    ("A", 1, 4, 300),
    ("B", 3, 5, 250),
    ("C", 0, 6, 800),
    ("D", 5, 7, 350),
    ("E", 3, 8, 900),
    ("F", 5, 9, 500),
    ("G", 6, 10, 450),
    ("H", 8, 11, 700),
    ("I", 8, 12, 650),
    ("J", 2, 13, 1200),
    ("K", 12, 14, 400)
]

#---------------------------------------------------
# GANTT CHART
#---------------------------------------------------
def gantt_chart(schedule, title):

    plt.figure(figsize=(10,4))

    for i, app in enumerate(schedule):

        name = app[0]
        start = app[1]
        end = app[2]

        plt.barh(
            y=i,
            width=end-start,
            left=start,
            height=0.5
        )

        plt.text(
            start+(end-start)/2,
            i,
            name,
            ha='center',
            va='center',
            color='white',
            fontsize=10,
            fontweight='bold'
        )

    plt.yticks(range(len(schedule)), [app[0] for app in schedule])
    plt.xlabel("Time")
    plt.ylabel("Appointments")
    plt.title(title)
    plt.grid(axis='x')
    plt.tight_layout()
    plt.savefig(save_path + title.replace(" ","_")+".png")
    plt.show()
    plt.close()


#---------------------------------------------------
# BAR CHART
#---------------------------------------------------

def comparison_chart(labels, values, title, ylabel):

    plt.figure(figsize=(8,5))

    bars = plt.bar(labels, values)

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2,
            height,
            str(height),
            ha="center",
            va="bottom"
        )

    plt.title(title)
    plt.ylabel(ylabel)


    plt.tight_layout()
    plt.savefig(save_path + title.replace(" ","_")+".png")
    plt.show()
    plt.close()


#---------------------------------------------------
# APPOINTMENT TIMELINE
#---------------------------------------------------

def timeline_plot(appointments):

    plt.figure(figsize=(10,4))

    for app in appointments:

        plt.hlines(
            y=app[0],
            xmin=app[1],
            xmax=app[2],
            linewidth=6
        )

    plt.xlabel("Time")
    plt.ylabel("Appointment")
    plt.title("Appointment Timeline")

    plt.grid(True)

    plt.tight_layout()
    plt.savefig(save_path + "Appointment_Timeline.png")
    plt.show()
    plt.close()


#---------------------------------------------------
# DURATION DISTRIBUTION
#---------------------------------------------------

def duration_distribution(appointments):

    durations=[a[2]-a[1] for a in appointments]

    plt.figure(figsize=(7,5))

    plt.hist(durations,bins=5, edgecolor="black")

    plt.title("Appointment Duration Distribution")
    plt.xlabel("Duration")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.savefig(save_path + "Duration_Distribution.png")
    plt.show()
    plt.close()


#---------------------------------------------------
# CASE 1
#---------------------------------------------------

fcfs, fcfs_equal_revenue = fcfs_scheduling(appointments_equal.copy())

sjf, sjf_equal_revenue = sjf_scheduling(appointments_equal.copy())

greedy, greedy_equal_revenue = earliest_finish(appointments_equal.copy())

gantt_chart(fcfs,"FCFS Gantt Chart")
gantt_chart(sjf,"SJF Gantt Chart")
gantt_chart(greedy,"Earliest Finish Gantt Chart")

comparison_chart(
    ["FCFS","SJF","Greedy"],
    [
        len(fcfs),
        len(sjf),
        len(greedy)
    ],
    "Number of Appointments Selected",
    "Appointments"
)


#---------------------------------------------------
# CASE 2
#---------------------------------------------------

fcfs_schedule, fcfs_rev = fcfs_scheduling(appointments_fee.copy())

highest_schedule, highest_rev = hff_scheduling(appointments_fee.copy())

ratio_schedule, ratio_rev = fee_per_hour(appointments_fee.copy())

optimal_schedule, optimal_rev = max_revenue_scheduling(appointments_fee.copy())

gantt_chart(fcfs_schedule,"FCFS Revenue Gantt")

gantt_chart(highest_schedule,"Highest Fee First Gantt")

gantt_chart(ratio_schedule,"Fee Per Hour Gantt")

gantt_chart(optimal_schedule,"Optimal Revenue Gantt")

comparison_chart(
    [
        "FCFS",
        "Highest Fee",
        "Fee/Hour",
        "Optimal"
    ],
    [
        fcfs_rev,
        highest_rev,
        ratio_rev,
        optimal_rev
    ],
    "Revenue Comparison",
    "Revenue ($)"
)


#---------------------------------------------------
# DATASET VISUALIZATION
#---------------------------------------------------

timeline_plot(appointments_equal)

duration_distribution(appointments_equal)

print("\nAll visualizations generated successfully!")
