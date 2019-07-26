from car import Car

car1 = Car("KA013060",5)
car2 = Car("KA013060",5)
car3 = Car("KA013060",5)
car4 = Car("KA013060",5)
car5 = Car("KA013060",5)
car1.start()
car2.start()
car3.start()
car1.change()
car1.change()
car2.change()
lst = [car1,car2,car3,car4,car5]

c = len(list(filter(lambda x:x.is_started and x.gear,lst)))
print(c)