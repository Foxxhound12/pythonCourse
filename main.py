#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill=float(input("Welcome to the tip calculator!\nHow much is your bill ? "))
percentage=int(input("How much percent do you want to tip? 10,12 or 15? "))
persons=int(input("Between how many people do you want to split the bill ? "))

result=(bill/100*percentage+bill)/persons
result="{:.2f}".format(round(result, 2)) 
#oder auf 2 mal aufgeteilt: 
#result=round(result,2)
#result="{:.2f}".format(result)
print(f"Each person has to pay: ${result}")
#print(f"Each person has to pay: ${'{:.2f}'.format(round(result, 2))}")
#print(f"Each person should pay: ${result:.2f}")  !!!!!hier wird automatisch gerundet