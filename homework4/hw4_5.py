amount_of_people = 0
total = 0

while True:
    iq = int(input("Please enter your IQ (please enter -1 to finish): "))

    if iq == -1:
        break

    if 30 <= iq <= 300:
        amount_of_people = amount_of_people + 1
        total = total + iq
    else:
        print("IQ can only be be between 30 and 300. Please try again.")

if amount_of_people > 0:
    avg = total / amount_of_people
    print(f"The average IQ in this group is: {avg}")
else:
    print("No valid IQs entered.")


print("one year of python training has been completed...")


new_amount_of_people = 0
new_total = 0

while True:
    new_iq = int(input("Please enter your new IQ after a year (please enter -1 to finish): "))

    if new_iq == -1:
        break

    if 30 <= new_iq <= 300:
        new_amount_of_people = new_amount_of_people + 1
        new_total = new_total + new_iq
    else:
        print("IQ can only be be between 30 and 300. Please try again.")

if new_amount_of_people > 0:
    new_avg = new_total / new_amount_of_people
    print(f"The new average IQ in this group after a year is: {new_avg}")
else:
    print("No valid IQs entered.")

differnce: float = new_avg - avg
print(f"the average IQ of the group increased by {differnce} in a spend of year")
