def weekday_name(day_of_week):
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }

    if day_of_week >= 1 and day_of_week <= 7:
        return days[day_of_week]
    else:
        return None
