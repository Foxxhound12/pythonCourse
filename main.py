print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You can ride the rollercoaseter!")
  age=int(input("what is your age ? "))
  if age <= 18 : 
  #Nennt man nested if Statement (= if else unter       anderem if. Wird nur geprüft wenn erstes if=true)
    print("You have to pay 7$!")
  else:
    print("You have to pay 12$!")
else:
  print("You can not ride the rollercoaster!")

  #Version 2 mit 3 Beträgen

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You can ride the rollercoaseter!")
  age=int(input("what is your age ? "))
  if age < 12 : 
    print("You have to pay 5$!")
  elif age <= 18 : #elif kann man unbegrenzt                             zwischen if und else verwenden,                      also so lange ein gewisse                            Konditionen geprüft werden                           sollen. Entpricht nested else,                       also if und else nach else:.
    print("You have to pay 7$!")
  else:
    print("You have to pay 12$!")
else:
  print("You can not ride the rollercoaster!")

#Schaltjahr Code Challenge:
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year%4 == 0 and year%100 != 0:
    print("Leap year.")
elif year%4 != 0:
    print ("Not leap year.")
elif year%4 == 0 and year%100 == 0:
    if year%400 == 0:
        print("Leap year.")
    else:
        print("Not leap year.")      

    

#Rollercoaster Version 3 mit Foto und immer nur Gesamtbetrag

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You can ride the rollercoaster!")
  age=int(input("what is your age ? "))
  pic=input("Do you want a Foto taken for 3$ extra ? Y or N?")
  if age < 12 and pic == "N" : 
    print("You have to pay 5$!")
  elif age < 12 and pic == "Y":
    print("You have to pay 8$!")
  elif age <= 18 and pic == "N": 
    print("You have to pay 7$!")
  elif age <= 18 and pic == "Y":
     print("You have to pay 10$!")
  elif age > 18 and pic == "N" :
    print("You have to pay 12$!")
  elif age > 18 and pic == "Y" :
    print("You have to pay 15$!")
else: 
  print("You can not ride the rollercoaster!")
  

#Version 4 mit beiden Beträgen (besser als Einzeln weil auch der Zwischenschritt(Grundpreis) aufgezeigt und mit print() ausgegeben wird. In Vers. 3 sieht man nur den Gesamtpreis.)
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You can ride the rollercoaseter!")
  age=int(input("what is your age ? "))
  if age < 12 : 
    bill=5
    print("Child tickets are 5$!")
  elif age <= 18 :
    bill=7
    print("Youth tickets are 7$!")
  else:
    bill=12
    print("Adult tickets are 12$!")
  pic=input("Do you want a picture taken? Y or N? ")
  if pic=="Y":
    bill +=3
  print(f"Your total bill is {bill}$.")
else:
  print("You can not ride the rollercoaster!")

#Pizza Order Code Challenge:
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#oder variable definieren bill=0 und in den if Statements für die Größe dann bill += 15 usw.
if size == "S":
    bill=15
elif size == "M":
    bill=20
else:
    bill=25
if add_pepperoni == "Y":
    if size == "S":
        bill +=2    
    else:
        bill +=3   
if extra_cheese == "Y":
    bill +=1
print(f"Your final bill is: ${bill}.")

#Version 5 mit Gratis Ticket für Midlife Crisis 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You can ride the rollercoaseter!")
  age=int(input("what is your age ? "))
  if age < 12 : 
    bill=5
    print("Child tickets are 5$!")
  elif age <= 18 :
    bill=7
    print("Youth tickets are 7$!")
  elif age >= 45 and age <= 55:
    bill=0
    print("You are likely to have a midlife-crisis so your ride is $0")
  else:
    bill=12
    print("Adult tickets are 12$!")
  pic=input("Do you want a picture taken? Y or N? ")
  if pic=="Y":
    bill +=3
  print(f"Your total bill is {bill}$.")
else:
  print("You can not ride the rollercoaster!")

#LoveCalculator mein erste und zu komplizierte Lösung, da Denkfehler: man such true aus beiden namen und das ist die ziffer links und love aus beiden namen ist ziffer rechts. Daher kann man schon vorher eine string concatenation durchführen um den Code effizienter und kürzer zu gestalten.
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower=name1.casefold()
name2_lower=name2.casefold()

T1=name1_lower.count("t")
R1=name1_lower.count("r")
U1=name1_lower.count("u")
E1=name1_lower.count("e")
Count1L=T1+R1+U1+E1

L1=name1_lower.count("l")
O1=name1_lower.count("o")
V1=name1_lower.count("v")
E1=name1_lower.count("e")
Count1R=L1+O1+V1+E1

T2=name2_lower.count("t")
R2=name2_lower.count("r")
U2=name2_lower.count("u")
E2=name2_lower.count("e")
Count2L=T2+R2+U2+E2

L2=name2_lower.count("l")
O2=name2_lower.count("o")
V2=name2_lower.count("v")
E2=name2_lower.count("e")
Count2R=L2+O2+V2+E2

CompleteL=Count1L+Count2L
CompleteR=Count1R+Count2R


Lovescore=int(str(CompleteL)+str(CompleteR))

if Lovescore <10 or Lovescore >90:
    print(f"Your score is {Lovescore}, you go together like coke and mentos.")
elif Lovescore > 40 and Lovescore < 50:
    print(f"Your score is {Lovescore}, you are alright together.")
else:
    print(f"Your score is {Lovescore}.")


#LoveCalculator Version 2 (besser und effizienter und Klammern um die Konditionen der if statements: (x<y) and (x>y) anstatt nur x<y and x>y um die Übersichtlichkeit zu verbessern)

# 🚨 Don't change the code below 👇
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lower=name1.casefold()
name2_lower=name2.casefold()
name_comb=name1_lower+name2_lower

T=name_comb.count("t")
R=name_comb.count("r")
U=name_comb.count("u")
E=name_comb.count("e")
CountL=T+R+U+E

L=name_comb.count("l")
O=name_comb.count("o")
V=name_comb.count("v")
E=name_comb.count("e")
CountR=L+O+V+E

Lovescore=int(str(CountL)+str(CountR))

if (Lovescore <10) or (Lovescore >90):
    print(f"Your score is {Lovescore}, you go together like coke and mentos.")
elif (Lovescore >= 40) and (Lovescore =< 50):
    print(f"Your score is {Lovescore}, you are alright together.")
else:
    print(f"Your score is {Lovescore}.")
