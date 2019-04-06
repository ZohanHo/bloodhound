from django_seed import Seed
from base.models import Contact
import random

seeder = Seed.seeder()

nameList = ["Zohan", "Funky", "blood", "Dick", "Bred", "Bill", "Stive", "Zagara", "Butcher", "Vita"]
phoneList = "38066"

seeder.add_entity(Contact, 10, {
    'name': lambda x:  random.choice(nameList),
    #'name': random.choice(nameList),
    'phone': lambda x:  phoneList + str(random.randint(1000000, 9999999)),
})

if __name__ == "__main__":
    inserted_pks = seeder.execute()



"""
random -со списка

employee = ["junior", "midle", "lead", "pm", "senior"]

newList =[]


for i in range(10):
    name = random.choice(employee)
    newList.append(name)

print(newList)
"""

"""
Рандомно создаеи телефон и выбирает имя

nameList = ["Zohan", "Funky", "blood", "Dick", "Bred", "Bill", "Stive", "Zagara", "Butcher", "Vita"]
phoneList = "38066"


newName =[]
newPhone =[]


for i in range(10):
    nameRandom = {'name': random.choice(nameList)}
    phoneRandom = {'phone': phoneList + str(random.randint(1000000, 9999999))}

    newName.append(nameRandom["name"])
    newPhone.append(phoneRandom["phone"])

print(newName)
print(newPhone)
"""
