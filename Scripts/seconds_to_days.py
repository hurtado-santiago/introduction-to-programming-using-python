Seconds = input ("Positive Integer: ")
if True:
    days = int (Seconds)//86400
    hours = (int (Seconds) - (86400*days))//3600 
    minutes = (int (Seconds) - (86400*days) - (3600*hours))//60
    seconds = (int (Seconds) - (86400*days) - (3600*hours) - (60*minutes))
    print (days, "days", hours, "hours", minutes, "minutes", seconds, "seconds")

