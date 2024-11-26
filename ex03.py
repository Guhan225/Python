a=int(input("Enter the year: "))
if(a%400==0 & a%100==0):
    print("Leap Year")
elif(a%400==0 & a%100!=0):
    print("Leap Year")
else:
    print("Not a leap year")    