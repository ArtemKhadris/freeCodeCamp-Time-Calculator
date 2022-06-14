def add_time(start, duration, *args):

    # start params
    start = start.split()
    [start_hour, start_min] = start[0].split(':')
    start_apm = start[1]
    [dur_hour, dur_min] = duration.split(':')
    end_apm, passed_days = start_apm, 0
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # time of end
    end_hour = int(start_hour) + int(dur_hour)
    end_min = int(start_min) + int(dur_min)

    # counting ending time minutes    
    if end_min >= 60:
        end_hour += 1
        end_min -= 60

    end_min = '0' + str(end_min) if len(str(end_min)) < 2 else str(end_min)

    # counting ending time hours, and coef for AM PM
    if end_hour >= 12:
        switch = end_hour // 12    # how many times have switched am/pm
        rem = end_hour % 12        # remainder of hour
        if rem != 0:
            end_hour = rem
        else:
            end_hour //= switch

        if switch > 1:             # counting how many days have passed
            if start_apm == 'PM':
                passed_days = (switch - 1) // 2 + 1
            else:
                passed_days = switch // 2
        elif switch == 1:
            if start_apm == 'PM':
                passed_days = 1

        if start_apm == 'AM':      # counting am/pm of the ending time
            if switch % 2 == 0:
                end_apm = 'AM'
            else:
                end_apm = 'PM'
        else:
            if switch % 2 == 0:
                end_apm = 'PM'
            else:
                end_apm = 'AM'

    if args:                       # if we have begin day
        start_day = args[0].title()
        if passed_days > 0:
            ind = week.index(start_day)
            ind += passed_days % 7
            if passed_days > 6:
                ind -= 7
            end_day = week[ind]
        else:
            end_day = start_day.title()
    end_hour = str(end_hour)

    if passed_days > 1:
        hmdp = '('+str(passed_days)+' days later)'   # hmdp - How Many Days have Passed
    elif passed_days == 1:
        hmdp = '(next day)'
    else:
        hmdp = ''

    if args:
        time_end = end_hour +":"+ end_min +" "+ end_apm +", "+ end_day +" "+ hmdp
    else:
        time_end = end_hour +":"+ end_min +" "+ end_apm +" "+ hmdp

    return(time_end.strip())