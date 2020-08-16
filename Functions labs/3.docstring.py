def readable_timedelta(days):
    # insert your docstring here
    '''Calculates how many weeks and days in a int days.
    weeks: calculates the number of weeks
    remainder: calculates the number of days
    '''
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)