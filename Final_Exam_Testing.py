l = [(1,"Tue"), (1,"Fri"), (1,"Thu"), (1,"Sat"), (1,"Sun"), (1,"Wed"), (3,"Mon")]
def sorting_by_days(tuple_day1, tuple_day2):
    """This method teaches the sorting algorithim how to sort days by chronological order"""
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    day1_offset = days.index(tuple_day1[1])
    day2_offset = days.index(tuple_day2[1])
    if day1_offset <= day2_offset:
        return 1
    return -1

days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
print (sorted(l, key = lambda day: days.index(day[1])))