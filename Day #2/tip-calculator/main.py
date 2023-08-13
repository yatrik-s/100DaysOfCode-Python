print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? Rs.")

total_bill_as_float = float(total_bill)

tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip_as_int = int(tip)

number_of_people = input("How many people to split the bill? ")
number_of_people_as_int = int(number_of_people)

tip_percentage = tip_as_int/100
tip_amount = total_bill_as_float * tip_percentage
total_amount = total_bill_as_float + tip_amount
amount_per_person = total_amount / number_of_people_as_int
amount_per_person = round(amount_per_person, 2)
print(f"Each persone should pay: Rs.{amount_per_person}")
