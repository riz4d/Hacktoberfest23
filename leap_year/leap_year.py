"""What is a leap year? To be a leap year, the year number must be divisible by four – except for end-of-century years, which must be divisible by 400.
    ~https://www.rmg.co.uk.
"""

year = input("Please give a year: ")

if (int(year) % 4) != 0:
    print("This is not a leap year")
elif (int(year) % 400) == 0:
    print("This is a leap year")
elif ((int(year) % 4) == 0) and ((int(year) % 100) != 0):
    print("This is a leap year")
else:
    print("This is not a leap year")