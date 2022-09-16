My_Number = int(input("Please provide the number to be reversed: "))
reverse_Number = 0
while(My_Number > 0):
 Reminder = My_Number %10
 reverse_Number = (reverse_Number *10) + Reminder
 My_Number = My_Number //10
print("mirror of the provided number is = %d" %reverse_Number)
