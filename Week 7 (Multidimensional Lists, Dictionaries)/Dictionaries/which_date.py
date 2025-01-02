from math import floor

def which_date(some_string):
    months={'January':11,
            'February':12,
            'March':1,
            'April':2,
            'May':3,
            'June':4,
            'July':5,
            'August':6,
            'September':7,
            'October':8,
            'November':9,
            'December':10}
    
    days={'Sunday':0,
            'Monday':1,
            'Tuesday':2,
            'Wednesday':3,
            'Thursday':4,
            'Friday':5,
            'Saturday':6}

    some_list=some_string.split(" ")
    day = int(some_list[1])
    month = int(months[some_list[0]])
    century = int(some_list[2])//100
    year = int(some_list[2])%100

    if month > 10:
        year = year-1
    
    w = (day+floor(2.6*month-0.2)-2*century+year+floor(year/4)+floor(century/4))%7
    for day in days:
        if days[day]==w:
            return day
                  
date = "May 5 1992"
print(which_date(date))
