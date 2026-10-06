marks = int(input("Enter your marks: "))
print("Your marks are:", marks)

if marks >= 90 and marks <= 100:
    print("Excellent")
elif marks >= 75 and marks <= 89:
    print("Very good")
elif marks >= 60 and marks <= 74:
    print("Good")
elif marks >= 40 and marks <= 59:
    print("Pass")
elif marks >= 0 and marks <= 39:
    print("Fail")
else:
    print("Invalid")