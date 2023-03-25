#Data Types
print("Hello World"[0]) # bei 0 zu zählen beginnen, Leerzeichen zählen auch mit 0=H,1=e...
#string is string of characters in ""
#Integer   ganze Zahl ohne komma  egal ob positvi oder negativ   um sie zu deklarieren einfach so schreiben bzw in print die ganze rechnung ohne ""
print(123+345)

#große Zahlen kann man mit unterstrichen schön gruppieren. Statt 1.222.334 für eine für einemillionen 222tausend 334 kann man diese Gruppierung mit Unterstrichen im Code machen um die Lesbarkeit zu erhöhen. Zb:   mit Unterstrichen können auch Namen von Variablen unterteilt werden
1_222_334 

#float ist abkürzung für floating point number.... also Zahl mit variablem dezimalpunkt z.B: Pi
3.14

#Boolean haben nur zwei Werte True oder False. Booleans schreibt man auch einfach so ohne ""
True
False

#string, integer, float und boolean sind alles Datentypen

num_char=len(input("What is your name ? "))
new_num_char=str(num_char)
print("Das sind "+new_num_char+" Zeichen.")
print(type(num_char)) #mit type kann man Datentyp prüfen.  Wäre in dem Fall integer, man kann aber auch Konversionen von einem Datentyp in den anderen durchführen (auch type casting genannt) z.B.   new_num_char=str(num_char) 
#Kombinierbar sind grundsätzlich nur gleiche Datentypen aber: integers and floating-point numbers can be mixed in arithmetic. Python 3 automatically converts integers to floats as needed.

# mathematische operationen sind +,-, Multiplikation (x*y) und Division(x/y). Das Ergebnis einer Division ist immer float, ** ist Exponentialrechnung x**y ist x hoch y   ( PEMDAS(LR) = Parentheses, Exponents, Multiplication, Division, Addition, Substraction) quasi punkt vor strich   und links vor rechts
# ()
#**
# *,/
#+,-
print(3*(3+3)/3-3)

#runden mit round(Zahl, Anzahl der Stellen auf die gerundet werden soll)
#Division mit // gibt Integer aus statt float(floor division genannt)
# will ich mit einem Ergebnis weiter rechnen
# result=8/3
#statt result= result /y  schreibe ich result /= y
#Konvertierung von float nach int schneidet alles nach dem Komma weg. Besser ist hier die round(variable oder zahl direkt, Anzahl der Stellen nach dem Komma die gerundet werden soll(kann weg gelassen werden, dann ist das Ergebnis trotzdem float auch wenn die Ausgabe eine ganze Zahl ist ))
x=12.56
print(round(x))
print(type(x))

result=8/3
result*=3
print(result)  #8/3*3

#f-string erlaubt kombination/ automatische Konvertierung von verschiedenen Datentypen z.B. print(f"Dein Ergebnis ist {result}")
print(f"Das Ergebnis ist {result}")

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆
#oder ageInt=int(age)   und age_remain=90-ageInt
age_remain=90-int(age)
age_r_mo=age_remain*12
age_r_we=age_remain*52
age_r_day=age_remain*365
print(f"You have {age_r_day} days, {age_r_we} weeks and {age_r_mo} months left.")
#Write your code below this line 👇
#oder message=f"You have {age_r_day} days, {age_r_we} weeks and {age_r_mo} months left."
# print(message)



