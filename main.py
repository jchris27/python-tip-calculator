#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
# 10% tip = 1.10
# 12% tip = 1.12
# 15% tip = 1.15

# n = 3.175546788
# number = '%.2f' % round(n, 2) # Gives you '5.6'
# print(number)

intro = "Welcome to the TIP CALCULATOR!!!"
print(intro)

bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_percentage = tip / 100
final_tip = tip_percentage * bill + bill
bill_per_person = final_tip / people
final_amount = "{:.2f}".format(bill_per_person) #special format to round off 2 decimal places

print(f"Each person should pay: ${final_amount}")
# print(f"Each person should pay ${'%.2f.' % round(final_tip,2)}")

