def add_time(start, duration, day=None):


    week_days = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday" ]
    

    #new time
    start_time = start.split(" ")[0]
    new_hour = int(start_time.split(":")[0]) + int(duration.split(":")[0])

    new_minutes = int(start_time.split(":")[1]) + int(duration.split(":")[1])
    if new_minutes > 59:
        new_hour += 1
        new_minutes = new_minutes - 60
    if new_minutes < 10:
        new_minutes = "0" + str(new_minutes)
   
    #days later/AMPM
    days_bool = False
    days_later = 0

    if new_hour > 11:
        if "PM" in start:
            days_later += int(new_hour / 24) + 1
            days_bool = True
            ampm = int(new_hour - 24*(days_later - 1))
            if ampm > 11:
                clock = "AM"
            else:
                clock = "PM"
                    
        if "AM" in start:
            days_later = int(new_hour / 24)
            days_bool = True
            ampm = int(new_hour - 24*days_later)
            if ampm > 11:
                clock = "PM"
            else:
                clock = "AM" 
    else:
        if "PM" in start:
            clock = "PM"
        if "AM" in start:
            clock = "AM"

    if new_hour > 12:
        if new_hour % 12 != 0:
            new_hour = new_hour % 12
        if new_hour % 12 == 0:
            new_hour = 12
        
    new_time = str(new_hour) + ":" + str(new_minutes)

    #days message
    days_message = ""
    counting_days = False
    if days_later >= 1:
        counting_days = True
    if counting_days is True:
        if days_later > 1 and days_later != 0:
            days_message = "(" + str(days_later) + " days later" + ")"
        elif days_later == 1:
            days_message = "(next day)"


    if day != None:
        which_day = week_days.index(day.lower())
        show_day = week_days[(which_day + days_later) % 7]

    output = (new_time + " " + clock + (", " + show_day.capitalize() if not day is None else "") + (" " + days_message if days_bool else "")).rstrip()
    
    return output