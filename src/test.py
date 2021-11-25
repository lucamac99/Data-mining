from random import random, seed
from random import randint
import json

file = open("/Users/luca/Documents/GitHub/Data-mining/firstname.txt","r")
list_names = file.readlines()
file.close #lista nomi

file = open("/Users/luca/Documents/GitHub/Data-mining/therapies.txt","r")
list_therapies = file.readlines()
file.close #lista terapie

file = open("/Users/luca/Documents/GitHub/Data-mining/conditions.txt","r")
list_conditions = file.readlines()
file.close #lista malattie

seed(2)

# list_namesdef = []
# for _ in range(10000):
#     value = randint(0,164000) #ridurre ampiezza lista nomi, utile davvero? 
#     list_namesdef.append(list_names[value])

l = []
lc = []
with open("data.json", 'w') as f:
    json.dump(l, f)
#CONTROLLARE DUPLICAZIONE NUMERI RANDOM 
with open("data.json", 'w') as feedsjson:      
    for i in range(320):
        Conditions = {
            "id" : "Cond"+str(i+1), #aggiungere Cond
            "name": str.strip(list_conditions[randint(1,320)])
        }
        l.append(Conditions)
        lc.append(Conditions)
    for i in range(200):
        Therapies = {
            "id" : "Th"+str(i+1), #aggiungere Ther
            "name": str.strip(list_therapies[randint(1,200)])
        }
        l.append(Therapies)
    for i in range(1000):
    #print to json
        lth = []
        lCo =[]       
        nTr = randint(1,10)
        nC = randint(0,3)
        for x in range (nTr):
            t = {
                "id" : "Tr"+str(x+1),
                #"diagnosed" : random data
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
            "trials" : [lth],
            "condition" : [lCo],
        }
        l.append(Patients)
    json.dump(l, feedsjson, indent = 2)

########## CONDITIONS ###########
# l = []
# with open("data_conditions.json", 'w') as f:
#     json.dump(l, f)

# import random
# ln = []
# while len(ln) < 200:
#     numero = random.randint(1,200)
#     if numero not in ln:
#         ln.append(numero)

# for i in range(200):
#     with open("data_conditions.json", 'w') as feedsjson:
#         Conditions = {
#             "id" : "Cond"+str(i+1), #aggiungere Cond
#             "name": str.strip(list_conditions[ln[i]])
#         }
#         l.append(Conditions)
#         json.dump(l, feedsjson, indent =1)

# l = []
# with open("data.json", 'w') as f:
#     json.dump(l, f)

# for i in range(20):
#     with open("data.json", 'w') as feedsjson:
#         Therapies = {
#             "id" : i+1, #aggiungere Ther
#             "name": str.strip(list_therapies[randint(1,100)])
#         }
#         l.append(Therapies)
#         json.dump(l, feedsjson, indent = 1)