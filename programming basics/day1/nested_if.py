age = int(input("Enter your age : "))
id = input("Do you have an ID: ").lower()

if age >= 18 :
    if id == "yes":
        print ("Allowed")
    else :
        print ("ID Required")
else :
    print ("You are under aged")