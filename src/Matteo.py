from random import random
from random import seed
import random #mi serve per creare le date, ho provato a importare solo random.randrange ma mi dà errore, cosi invece va
from random import randint
import datetime
import json

file = open("/Users/Matteo/Desktop/Python/first_names.txt","r")
list_names = file.readlines()
file.close #lista nomi

file = open("/Users/Matteo/Desktop/Python/therapies.txt","r")
list_therapies = file.readlines()
file.close #lista terapie

file = open("/Users/Matteo/Desktop/Python/conditions.txt","r")
list_conditions = file.readlines()
file.close #lista malattie

seed(2)

lreg = ["Abruzzo", "Basilicata", "Calabria", "Campania", "Emilia", "Friuli", "Lazio", "Liguria", "Lombardia", "Marche", "Molise", "Piemonte", "Puglia", "Sardegna", "Sicilia", "Sardegna", "Toscana", "Trentino", "Umbria", "Val d'Aosta", "Veneto"]
lsex = ["M","F"]
l = [] ##lista finale con tutto
lc = [] ##lista delle conditions, non mi ricordo perché l'abbiamo creata però hahaha
with open("data.json", 'w') as f:
    json.dump(l, f)
#CONTROLLARE DUPLICAZIONE NUMERI RANDOM 
with open("data.json", 'w') as feedsjson: 
    l.append("{")
    l.append("Condition: ")
    for i in range(320):
        Conditions = {
            "id" : "Cond"+str(i+1), 
            "name": str.strip(list_conditions[randint(1,320)])
        }
        l.append(Conditions)
        lc.append(Conditions)
    l.append("],")
    l.append("Therapies: [")
    for i in range(200):
        Therapies = {
            "id" : "Th"+str(i+1), 
            "name": str.strip(list_therapies[randint(1,200)])
        }
        l.append(Therapies)
    l.append("],")
    l.append("Patients: [")
    for i in range(1000):
    #print to json <-- ??
        lth = []
        lCo =[] 
        nTr = randint(1,10)
        nC = randint(0,3)
        for x in range (nTr):

            ###creare date random###

            start_date1 = datetime.date(2010, 1, 1) #data inizio
            end_date1 = datetime.date(2020, 1, 1)

            time_between_dates = end_date1 - start_date1
            days_between_dates = time_between_dates.days
            random_number_of_days = random.randrange(days_between_dates)
            random_date1 = start_date1 + datetime.timedelta(days=random_number_of_days)
            
            start_date2 = random_date1 #data fine
            end_date2 = datetime.date(2020, 1, 1)

            time_between_dates = end_date2 - start_date2
            days_between_dates = time_between_dates.days
            random_number_of_days = random.randrange(days_between_dates)
            random_date2 = start_date2 + datetime.timedelta(days=random_number_of_days)
            


            t = {
                "id" : "Tr"+str(x+1),
                 "start" : str(random_date1),
                 "end" : str(random_date2), 
                "condition": lc[randint(1,300)]["name"],
                "therapy": str.strip(list_therapies[randint(1, 200)]),
                "successful": str(randint(1,100))+"%"
            }
            lth.append(t)
        for y in range (nC):
            n = randint(1,300)
            c = {
                "id" : lc[n]["id"],
                "name" : lc[n]["name"]
            }
            lCo.append(c)
        Patients = {
            "id" : str(i+1), 
            "name" : str.strip(list_names[randint(1, 100000)]), 
            "sex" : str.strip(lsex[random.randint(0,1)]),
            "regione" : str.strip(lreg[randint(0,19)]),
            "eta'" : randint(1,3), #1 = 18-34, 2 = 35-60, 3 = >65
            "trials" : lth,
            "condition" : lCo,
        }
        l.append(Patients)
    l.append("}")
    json.dump(l, feedsjson, indent = 2)

########## CONDITIONS ###########
# l = []
# with open("data_conditions.json", 'w') as f:
# json.dump(l, f)

# import random
# ln = []
# while len(ln) < 200:
# numero = random.randint(1,200)
# if numero not in ln:
# ln.append(numero)

# for i in range(200):
# with open("data_conditions.json", 'w') as feedsjson:
# Conditions = {
# "id" : "Cond"+str(i+1), #aggiungere Cond
# "name": str.strip(list_conditions[ln[i]])
# }
# l.append(Conditions)
# json.dump(l, feedsjson, indent =1)

# l = []
#