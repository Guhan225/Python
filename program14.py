def days_in_month(month):
    switcher={
            'Jan':31,
            'Feb':28,
            'Mar':31,
            'Apr':30,
            'May':31,
            'Jun':30,
            'Jul':31,
            'Aug':31,
            'Sep':30,
            'Oct':31,
            'Nov':30,
            'Dec':31
            }
    return switcher.get(month,"Invalid")
print(days_in_month('Jan'))
print(days_in_month('Feb'))