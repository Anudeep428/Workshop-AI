item="Fried rice"#string
price=40 #integer
rating=4.5 #float
is_veg=True #boolean
print(type(price))
print(type(rating))
print(type(is_veg))
print(type(item))
print(item)
print(price)
print(item,"cost = ",price)
menu =["Dosa","Idli","Samosa"]
print(type(menu))
print(menu[2])
print(menu[1])
menu.append("Vada")
menu[1] = "puri"
menu[2] = "Egg puff"
print(menu)
menu.remove("Dosa")
print(menu)
working_days = ("Monday","Tuesday","Wednesday","Thursday","Friday")
print(working_days[2])
prices = {
    "Dosa" : 40,
    "Idli" : 30,
    "Samosa":15
}
prices["Vada"]=25
print(prices)
#print(prices["Dosa"])
#print(prices["Samosa"])