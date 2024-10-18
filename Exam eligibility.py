medical_cause=input("Do you have a medical cause ? Yes or No: ")
attendence=int(input("Enter your Attendance: "))

if medical_cause=='Yes':
    print("You are allowed to take this exam")
else:
    if attendence>=75:
        print("You are allowed to take this exam")
    else:
        print("You are NOT allowed to take this exam")