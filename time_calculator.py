def add_time(start, duration, day=None):
    new_time = None

    am_pm = start[-2:]
    for i in range(len(start)):
        if start[i] == ':':
            num_1 = start[:i]
            num_2 = start[i+1:i+3]
    
    for i in range(len(duration)):
        if duration[i] == ':':
            dur_hour = duration[:i]
            dur_min = duration[i+1:i+3]
    
    hour_1 = int(num_1)
    hour_2 = int(dur_hour)
    minute_1 = int(num_2)
    minute_2 = int(dur_min)

    if hour_2 == 12:
        hour_2 = 0
    if am_pm == "PM":
        hour_2 += 12
    
    minute = minute_1 + minute_2
    if minute >= 60:
        hour_2 += 1
        minute -= 60
    
    hour = hour_1 + hour_2

    days = hour // 24

    days_list=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    if day:
        pos_day = days_list.index(day.capitalize())
        pos_day = (pos_day+days)%7
        day = days_list[pos_day]
    
    hour = hour % 24

    if hour >= 12:
        hour -= 12
        if hour == 0:
            hour = 12
        new_time = str(hour) + ":" + str(minute).rjust(2,'0') + " PM"
    else:
        if hour == 0:
                hour = 12
        new_time = str(hour) + ":" + str(minute).rjust(2,'0') + " AM"
    if day:
        new_time += ', ' + day
    if days > 0:
        if days == 1:
            new_time += " (next day)"
        else:
            new_time+=" ({} days later)".format(days)

    return new_time

add_time("3:30 PM", "2:12")#expected = "5:42 PM"
add_time("11:55 AM", "3:12")#expected = "3:07 PM"
add_time("9:15 PM", "5:30")#expected = "2:45 AM (next day)"
add_time("11:40 AM", "0:25")#expected = "12:05 PM"
add_time("2:59 AM", "24:00")#expected = "2:59 AM (next day)"
add_time("11:59 PM", "24:05")#expected = "12:04 AM (2 days later)"
add_time("8:16 PM", "466:02")#expected = "6:18 AM (20 days later)"
add_time("5:01 AM", "0:00")#expected = "5:01 AM"
add_time("3:30 PM", "2:12", "Monday")#expected = "5:42 PM, Monday"
add_time("2:59 AM", "24:00", "saturDay")#expected = "2:59 AM, Sunday (next day)"
add_time("11:59 PM", "24:05", "Wednesday")#expected = "12:04 AM, Friday (2 days later)"
add_time("8:16 PM", "466:02", "tuesday")#expected = "6:18 AM, Monday (20 days later)"

'''
### Assignment

Write a function named `add_time` that takes in two required parameters and one optional parameter:
* a start time in the 12-hour clock format (ending in AM or PM) 
* a duration time that indicates the number of hours and minutes
* (optional) a starting day of the week, case insensitive

The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show `(next day)` after the time. If the result will be more than one day later, it should show `(n days later)` after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.
```py
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```

Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.

### Development

Write your code in `time_calculator.py`. For development, you can use `main.py` to test your `time_calculator()` function. Click the "run" button and `main.py` will run.

### Testing 

The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.

### Submitting

Copy your project's URL and submit it to freeCodeCamp.

'''