import random
from random import seed, randint
import datetime
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

def BeetweenDate(startDate, endDate):
    time_between_dates = endDate - startDate
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date1 = start_date1 + datetime.timedelta(days=random_number_of_days)
    return random_date1

def FutureDate(pastDate):
    random_number_of_days = random.randrange(randint(1,50))
    futureDate = pastDate + datetime.timedelta(days=random_number_of_days)
    return futureDate

# list_namesdef = []
# for _ in range(10000):
#     value = randint(0,164000) #ridurre ampiezza lista nomi, utile davvero? 
#     list_namesdef.append(list_names[value])

lreg = ["Abruzzo", "Basilicata", "Calabria", "Campania", "Emilia", "Friuli", "Lazio", "Liguria", "Lombardia", "Marche", "Molise", "Piemonte", "Puglia", "Sardegna", "Sicilia", "Sardegna", "Toscana", "Trentino", "Umbria", "Val d'Aosta", "Veneto"]
lsex = ["M","F"]
l = [] #lista finale con tutto
lc = [] #lista delle conditions, per il sort nei pazienti
lTh = []
lFinale = []
lPatients = []
with open("data.json", 'w') as f:
    json.dump(l, f)
#CONTROLLARE DUPLICAZIONE NUMERI RANDOM 
with open("data_prova.json", 'w') as feedsjson:
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
        lTh.append(Therapies)
    for i in range(1000):
    #print to json
        ltr = []
        lCo =[]       
        #nTr = randint(1,10)
        nC = randint(1,3)
        lcured = []
        lStartDate = []
        lEndDate= []

        ######## Creazione Conditions ########
        for y in range (nC):
            n = randint(0,319)
            lcured.append(True)
            if(randint(1,4)==1):
                lcured.pop(len(lcured)-1)
                lcured.append(False)

            start_date1 = datetime.date(2010, 1, 1) #data inizio
            end_date1 = datetime.date(2020, 1, 1)

            time_between_dates = end_date1 - start_date1
            days_between_dates = time_between_dates.days
            random_number_of_days = random.randrange(days_between_dates)
            random_date1 = start_date1 + datetime.timedelta(days=random_number_of_days)
            lStartDate.append(random_date1)

            random_date2 = None
            if(lcured[y] == True):
                start_date2 = random_date1 #data fine
                end_date2 = datetime.date(2020, 1, 1)

                time_between_dates = end_date2 - start_date2
                days_between_dates = time_between_dates.days
                random_number_of_days = random.randrange(days_between_dates)
                random_date2 = start_date2 + datetime.timedelta(days=random_number_of_days)
            lEndDate.append(random_date2)
            c = {
                "id" : "pc"+str(y+1),
                "diagnosted" : str(random_date1),
                "cured" : str(random_date2),
                "kind" : lc[n]["id"],
                "name" : lc[n]["name"]
            }
            lCo.append(c)

        ######## Creazione Trials ########
        x=0
        for f in range (nC):
            boolea = True
            appoggio_start = lStartDate[f]
            appoggio_end = lEndDate[f]
            if(lcured[f]):
                while boolea:
                    x = x+1
                    successRate = randint(0,100) 
                    startDateTrial = FutureDate(appoggio_start)
                    endDateTrial = FutureDate(startDateTrial)
                        
                    #startDateTrial = BeetweenDate(appoggio_start, appoggio_end)
                    #endDateTrial = BeetweenDate(startDateTrial, appoggio_end)
                    if(successRate>70):
                        boolea = False
                        lCo[f]["cured"]= str(endDateTrial)
                        #endDateTrial = lEndDate[f]
                    t = {
                        "id" : "Tr"+str(x),
                        "start" : str(startDateTrial),
                        "end" : str(endDateTrial), 
                        "condition": "pc"+str(f+1),
                        "therapy": str.strip(list_therapies[randint(1, 200)]),
                        "successful": str(successRate)+"%"
                    }
                    ltr.append(t)
                    
                    appoggio_start = endDateTrial
            else:
                appoggio_end = FutureDate(appoggio_start)
                for u in range(randint(0,8)):
                    x = x+1
                    successRate = randint(0,70)    
                    startDateTrial = FutureDate(appoggio_start)
                    endDateTrial = FutureDate(startDateTrial)
                    #startDateTrial = BeetweenDate(appoggio_start, appoggio_end)
                    #endDateTrial = BeetweenDate(startDateTrial, appoggio_end)
                    t = {
                        "id" : "Tr"+str(x),
                        "start" : str(startDateTrial),
                        "end" : str(endDateTrial), 
                        "condition": "pc"+str(f+1),
                        "therapy": str.strip(list_therapies[randint(1, 200)]),
                        "successful": str(successRate)+"%"
                    }
                    ltr.append(t)
                    appoggio_start = endDateTrial
        
        Patients = {
            "id" : str(i+1), 
            "name" : str.strip(list_names[randint(1, 100000)]), #così non si duplicano mai i nomi, è un problema?
            "sex" : str.strip(lsex[random.randint(0,1)]),
            "regione" : str.strip(lreg[randint(0,20)]),
            "eta'" : randint(1,100),
            "conditions" : lCo,
            "trials" : ltr,         
        }
        l.append(Patients)
        lPatients.append(Patients)
    Data = {
        'Conditions' : lc,
        'Therapies' : lTh,
        'Patients' : lPatients,
    }
    json.dump(Data, feedsjson, indent = 2)



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