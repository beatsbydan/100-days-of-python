def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


# Days in Month
# isLeap is a function to determine if a year is leap
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def days_in_month(year, month):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month-1]