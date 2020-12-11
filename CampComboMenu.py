def tax(taxAmount,total):
    theTotalAmount=total*(1+taxAmount/100)
    #theTotalAmount=20     *(1+7/100)
    return theTotalAmount
print("Welcome to the Krust Krab")
orderedItems=[]
orderList=[]
total=0                 #accumalitive variable
sandwichSelected=False  #flag variable
beverageSelected=False
sideSelected=False
ui=input("Say done to end your order ")
order=[]
sandwich=input("What sandwich would you like: Krabby Patty(kp)-$1.25, Salty Sea Dog(sd)-$1.25, Footlong(f)-$2.00, Sailor's Suprise(ss)-$3.00,or Golden Loaf(gl)-$2.00 ")
if (sandwich=="kp" or sandwich=="sd" or sandwich=="f" or sandwich=="ss" or sandwich=="gl"):
  sandwichSelected=True
  if sandwich=="kp":
    meal=input("Would you like to make it a meal y or n")
    if meal=="y":
      meal=input("Would you like a single(s), double(d), or triple(t) meal ")
    if meal=="s":
       total+=3.50
    elif meal=="d":
      total+=3.75
    elif meal=="t":
      total+=4
  else:
    total+=1.25
  sandwich=input("Would you like to make it a double for $.75, y or n ")
  if sandwich=="y"or sandwich=="Y":
    sandwich=input("Would you ike to make it a triple for $1, y or n ")
    if sandwich=="y"or sandwich=="Y":
        total+=3.00
    else:
        total+=2.00
  else:
    total+=1.25

elif sandwich=="sd":
  total+= 1.25
elif sandwich=="f":
  total+= 2.00
elif sandwich=="ss":
  total+=3.00
elif sandwich=="gl":
  sandwich=input("Would you like sauce for $.50 y or n ")
  if sandwich=="y":
    total+=2.50
  else:
    total+=2.00
if sandwich=="kp":
  cheese=input("Would you like cheese on your krabby patty for $.25 y or n ")
  if cheese=="y":
    total+=.25
orderedItems.append(sandwich)#adds items to the order list
print(sandwich)

beverage= input("would you like a drink, y or n? ")
if (beverage=="y"):
  beverage =input("Would you like a Kelp Shake(ks) or a Seafoam Soda(ss)")
  beverageSelected=True 
  print("you said",beverage) #print(string,string,string,string)
  if beverage=="ks":
    total+= 2.00
  elif beverage=="ss":
    beverage=input("Would you like a small(s)-$1.00, medium(m)-$1.25, or large(l)-$1.50")
    if beverage=="s":
      total+=1.00
    elif beverage=="m":
      total+=1.25
    elif beverage=="l":
      total+=1.50
orderedItems.append(beverage)


  #iteration 3 for asking for fries
side=input("Would you like some a side y or n ")
if (side=="y"):
  side= input("Would you like Coral Bits(cb) or Kelp Rings(kr)-$1.50")     
  sideSelected=True
  if side=="kr":
    total+=1.50
  elif side=="cb":
    side=input("Would you like a small(s), medium(m), or large(l) ")
    if (side=="s"):
      total+=1
    elif(side=="m"):
        total+=1.25
    elif(side=="l"):
      total+=1.50
orderedItems.append(side)
  #iteration 4
  #if you do not convert input to an int ()it will be a sequence or a string
sauce=int(input("how many salty sauce packets would you like "))
sauce=sauce*.50
total+= sauce
orderedItems.append(sauce)

  #but you could combine the top two lines into one
    #and looks for 2 true statements
      #if variable == true and variable==true and variable==true
#print("Your total is",total)
#print('Your order is a {0} sandwich, a {1} drink, a {2} fry, and {3} ketchup packet(s) \nfor a total of {4} '.format(sandwhich,beverage,fries,ketchup,total))

orderList.append(orderedItems)
print(orderList)

ui=input("Would you like to add(a) another order, edit(e) your order, delete(d) an order, or say done to finish your order ")
if ui=="a":
  order=[]
elif ui=="d":
  ui=int(input("What order number would you like to remove "))
  orderList.remove(ui)
if ui=="done":
  print(orderList)
  print("Subtotal:",total)
  print("Tax:",tax(7,total))

#print('${:,.2f}' .format(total)) #string formatting