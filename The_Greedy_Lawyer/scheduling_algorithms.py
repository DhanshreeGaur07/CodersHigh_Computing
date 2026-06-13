#---------------------------------------------------
# FIRST COME FIRST SERVE SCHEDULING
#---------------------------------------------------

def fcfs_scheduling(appointments) :

    # appointments = (Name, start, end, revenue)

    # Sort by arrival time
    appointments.sort(key=lambda x: x[1])

    selected_appointments = []
    last_end = 0

    for app in appointments:

        # If the current time is less than or equal to the arrival time
        if last_end <= app[1]:
            selected_appointments.append(app)

            # Update the last end time to the end of this appointment
            last_end = app[2] 

    return selected_appointments



#---------------------------------------------------
# SHORTEST JOB FIRST SCHEDULING
#---------------------------------------------------

def sjf_scheduling(appointments):

    # duration = end - start

    # Sort by start and duration
    appointments.sort(key=lambda x: (x[2]-x[1],x[1]))

    selected_appointments = []
    last_end = 0

    for app in appointments:
        if last_end <= app[1]:
            selected_appointments.append(app)

            # Update the last end time to the end of this appointment
            last_end = app[2]
    
    return selected_appointments



#---------------------------------------------------
# EARLIEST FINISH TIME OR GREEDY OPTIMAL SCHEDULING
#---------------------------------------------------

def earliest_finish(appointments):

    # Sort appointments by their end time in ascending order
    appointments = sorted(appointments, key=lambda x: x[2])

    selected_appointments = []

    last_end = 0

    for app in appointments:

        if app[1] >= last_end:

            selected_appointments.append(app)

            last_end = app[2]

    return selected_appointments