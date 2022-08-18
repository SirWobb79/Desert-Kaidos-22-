import random

miles = 0
p = 0

#Introduction
print("Welcome to Desert! You have to walk through an infinite desert.")
print("\nIf you want any chance of getting the furthest, try \nthinking before you act.")
print("\nYou have 4 basic actions:")
print("\n1: Walk 1/2 mi (-25 Thirst, -12 Hunger, -10 Energy)\n2: Drink from canteen and eat (+30 Thirst +30 Hunger, -60 Supplies)\n3: Sleep for the night (+90 to +120 Energy etc.)\n4: Get more supplies (+50 Supplies)\n\nYou have travelled", miles, "miles.\n\nYou have slept for a total of", p, "hours.")

#Base stats
h = 100
t = 100
e = 100
s = 200
walk = "1"
consume = "2"
sleep = "3"
stock = "4"

for x in range(1000000000):
    
    print("\nHunger:", h, "\nThirst:", t,  "\nEnergy:", e,  "\nSupplies:", s)
    print("\nAction ", x, ":")
    a = input("\nWhat do you want to do?\n(Walk 1/Eat & Drink 2/Rest 3/Add Supplies 4) ")
    o = random.randint(9, 12)
    
    if a == walk:
        print("\nYou walked 1/2 mi.")
        t -= 25
        h -= 12
        e -= 10
        miles += 0.5
        
    elif a == consume:
        if s <= 60:
            s -= 0
            print("\nYou can't do this action now, you need supplies.")
        else:
            print("\nYou stopped to eat and drink.")
            t += 30
            h += 30
            s -= 60
        
    elif a == sleep:
        print("\nYou slept for", o, "hrs.")
        p += o
        
        if o == 9:
            e += 90
            t -= 9
            h -= 5
            
        elif o == 10:
            e += 100
            t -= 10
            h -= 6
            
        elif o == 11:
            e +=110
            t -= 11
            h -= 7
            
        elif o == 12:
            e += 120
            t -= 12
            h -= 8
            
    elif a == stock:
        print("\nYou called for supplies and got them.")
        s += 50
        
    print("-------------------")
    print("\n1: Walk 1/2 mi (-25 Thirst, -25 Hunger, -10 Energy)\n2: Drink from canteen and eat (+30 Thirst +30 Hunger, -60 Supplies)\n3: Sleep for the night (+90 to +120 Energy depending on hrs slept)\n4: Get more supplies (+50 Supplies)\n\nYou have travelled", miles, "miles.\n\nYou have slept for a total of", p, "hours.")
   
    #This is if either the Hunger, Thurst, or Energy reach 0
    if h <= 0:
        break
        
    if t <= 0:
        break
        
    if e <= 0:
        break
        
print("\nGame Over!")