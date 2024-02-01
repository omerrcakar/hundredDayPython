# tip - calculator

print("Welcome to the tip calculator")

bill = float(input("What was the total bill?\n"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
peoples = int(input("How many people to split to bill?\n"))


tip_percent = tip / 100
tip_amount = bill * tip_percent
total_bill = bill + tip_amount
bill_per_person = total_bill / peoples
sonuc = round(bill_per_person,1)
print(f"Each person should pay : {sonuc}")

# print("Each person should pay :  {:0.1f} $".format(bill_per_person))
