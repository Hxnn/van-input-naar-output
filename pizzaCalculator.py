# Yavuz Alici, Opdracht: Pizza Calculator
PriceM = 12.99
PriceI = 14.50
PriceL = 17.99

print("Welcome to Hinn's! Enjoy your stay at your amazing restaurant! ")
howmanyM = int(input("How many Medium pizza's would you like? : "))

howmanyI = int(input("How many Italian pizza's would you like? : "))

howmanyL = int(input("How many Large pizza's would you like? : "))

TotaalprijsM = PriceM * howmanyM
print('Your total is: '+str(TotaalprijsM) + ' Euro and you ordered ' +str(howmanyM) + " Pizza's")

TotaalprijsI = PriceI * howmanyI
print('Your total is: '+str(TotaalprijsI) + ' Euro and you ordered ' +str(howmanyI) + " Pizza's")

TotaalprijsL = PriceL * howmanyL
print('Your total is: '+str(TotaalprijsL) + ' Euro and you ordered ' +str(howmanyL) + " Pizza's")


