day = input("Enter the day: ").lower()

if day == "saturday" or day == "sunday":
    print("weekend")
elif day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
    print("weekday")
else:
    print("Invalid day.")