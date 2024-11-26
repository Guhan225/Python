def day_of_week(day_number):
    switcher={
            1:"Sunday",
            2:"Monday",
            3:"Tuesday",
            4:"Wednesday",
            5:"Thursday",
            6:"Friday",
            7:"Saturday"
            }
    return switcher.get(day_number,("Invalid"))
print(day_of_week(2))
print(day_of_week(7))