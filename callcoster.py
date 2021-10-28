days_of_the_week = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun"]
day_of_the_week = str(input("Enter the day the call started at: "))

if day_of_the_week.capitalize() not in days_of_the_week:
    print("That value is incorrect")
    print("Try one of the following values: ", days_of_the_week)
    day_of_the_week = str(input("Enter the day the call started at: "))


call_started_at_time = input("Enter the time the call started at (hhmm): ")
call_duration = abs(int(input("Enter the duration of the call (in minutes): ")))

user_time_input = [int(num) for num in str(call_started_at_time)]
i = 0
price = round(0, 2)
minute = user_time_input[3]
tenth_minute = user_time_input[2]
hour = user_time_input[1]
twenty_fourth_hour = user_time_input[0]

minute_count40 = 0
minute_count25 = 0
minute_count15 = 0

while i < call_duration:
    if minute != 9:
        minute = minute + 1
    elif minute == 9:
        minute = 0
        if tenth_minute != 5:
            tenth_minute = tenth_minute + 1
        else:
            tenth_minute = 0
            if hour == 9:
                hour = 0
                twenty_fourth_hour = twenty_fourth_hour + 1
            elif twenty_fourth_hour == 2:
                hour = 0
                twenty_fourth_hour = 0
                # if day_of_the_week.capitalize() == "Fri":
                #     day_of_the_week = "Sat"
                # elif day_of_the_week.capitalize() == "Sun":
                #     day_of_the_week = "Mon"
            else:
                hour = hour + 1
    time_str = str(twenty_fourth_hour) + str(hour) + str(tenth_minute) + str(minute)
    minutes = time_str[2:4]
    hours = time_str[0:2]
    # print(time_str)
    if int(hours) >= 8 and int(hours) < 18:
        if day_of_the_week.capitalize() not in days_of_the_week[5:7]:
            minute_count40 = minute_count40 + 1
        else:
            minute_count15 = minute_count15 + 1
    else:
        if day_of_the_week.capitalize() not in days_of_the_week[5:7]:
            minute_count25 = minute_count25 + 1
        else:
            minute_count15 = minute_count15 + 1
    i = i + 1


rate40 = float(0.40)
rate25 = float(0.25)
rate15 = float(0.15)
total = minute_count40 * rate40 + minute_count25 * rate25 + minute_count15 * rate15
totalstr = "This call will cost ${sum:2.2f}"
print(totalstr.format(sum=total))
