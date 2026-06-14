#---------------------------------------------------
# FIRST COME FIRST SERVE SCHEDULING
#---------------------------------------------------

from bisect import bisect_right


def is_compatible(appointment, selected_appointments):
    start = appointment[1]
    end = appointment[2]

    for selected in selected_appointments:
        selected_start = selected[1]
        selected_end = selected[2]

        if start < selected_end and end > selected_start:
            return False

    return True


def fcfs_scheduling(appointments) :

    # appointments = (Name, start, end, revenue)

    # Sort by arrival time
    appointments = sorted(appointments, key=lambda x: x[1])

    selected_appointments = []
    last_end = 0
    revenue = 0

    for app in appointments:

        # If the current time is less than or equal to the arrival time
        if last_end <= app[1]:
            selected_appointments.append(app)
            revenue += app[3]

            # Update the last end time to the end of this appointment
            last_end = app[2] 

    return selected_appointments, revenue



#---------------------------------------------------
# SHORTEST JOB FIRST SCHEDULING 
#---------------------------------------------------

def sjf_scheduling(appointments):

    # duration = end - start

    # Sort by start and duration
    appointments = sorted(appointments, key=lambda x: (x[2]-x[1], x[1]))

    selected_appointments = []
    revenue = 0

    for app in appointments:
        if is_compatible(app, selected_appointments):
            selected_appointments.append(app)
            revenue += app[3]
    
    return sorted(selected_appointments, key=lambda x: x[1]), revenue



#---------------------------------------------------
# HIGHEST FEE FIRST SCHEDULING
#---------------------------------------------------

def hff_scheduling(appointments):

    # Sort by fee in descending order
    appointments = sorted(appointments, key=lambda x: (-x[3], x[1]))

    selected_appointments = []
    revenue = 0

    for app in appointments:
        if is_compatible(app, selected_appointments):
            selected_appointments.append(app)
            revenue += app[3]
    
    return sorted(selected_appointments, key=lambda x: x[1]), revenue



#---------------------------------------------------
# EARLIEST FINISH TIME OR GREEDY OPTIMAL SCHEDULING
#---------------------------------------------------

def earliest_finish(appointments):

    # Sort appointments by their end time in ascending order
    appointments = sorted(appointments, key=lambda x: x[2])

    selected_appointments = []
    revenue = 0
    last_end = 0

    for app in appointments:

        if app[1] >= last_end:

            selected_appointments.append(app)
            revenue += app[3]

            last_end = app[2]

    return selected_appointments, revenue



#---------------------------------------------------
# HIGHEST FEE PER HOUR FIRST SCHEDULING
#---------------------------------------------------

def fee_per_hour(appointments):

    appointments = sorted(
        appointments,
        key=lambda x: (
            -(x[3]/(x[2]-x[1])),
            x[1]
        )
    )

    selected_appointments = []
    revenue = 0

    for app in appointments:

        if is_compatible(app, selected_appointments):

            selected_appointments.append(app)
            revenue += app[3]

    return sorted(selected_appointments, key=lambda x: x[1]), revenue



#---------------------------------------------------
# OPTIMAL MAXIMUM REVENUE SCHEDULING
#---------------------------------------------------

def max_revenue_scheduling(appointments):

    # Weighted interval scheduling:
    # choose the non-overlapping appointments with the highest total revenue.
    appointments = sorted(appointments, key=lambda x: x[2])
    end_times = [app[2] for app in appointments]

    compatible_indexes = []
    for app in appointments:
        previous_index = bisect_right(end_times, app[1]) - 1
        compatible_indexes.append(previous_index)

    total_appointments = len(appointments)
    max_revenue = [0] * (total_appointments + 1)

    for i in range(1, total_appointments + 1):
        appointment = appointments[i - 1]
        include_revenue = appointment[3] + max_revenue[compatible_indexes[i - 1] + 1]
        exclude_revenue = max_revenue[i - 1]
        max_revenue[i] = max(include_revenue, exclude_revenue)

    selected_appointments = []
    i = total_appointments

    while i > 0:
        appointment = appointments[i - 1]
        include_revenue = appointment[3] + max_revenue[compatible_indexes[i - 1] + 1]

        if include_revenue > max_revenue[i - 1]:
            selected_appointments.append(appointment)
            i = compatible_indexes[i - 1] + 1
        else:
            i -= 1

    selected_appointments.reverse()

    return selected_appointments, max_revenue[total_appointments]
