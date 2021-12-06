import json 
f = open("data_prova.json")
data = json.load(f)

for i in data["Therapies"]: #Restituisce il nome corrispondente all'id di una certa terapia
    if i["id"] == "Th22":
        print(i["name"])

for i in data["Patients"]: #Restituisce tutti i pazienti che hanno una certa condition
    for x in i["condition"]:
        if x["kind"] == "Cond302":
            print(i["name"])

def Suggest(condition): #Ti tira fuori, con relative percentuali di successo, tutte le terapie che hanno funzionato per una certa condition
    for p in data["Patients"]:
        for c in p["condition"]:
            if c["kind"] == condition:
                pc = c["id"]
                for t in p["trials"]:
                    if t["condition"] == pc:
                        if int(t["successful"][:-1]) > 70:
                            print(t["therapy"])
                            print(t["successful"])


Suggest("Cond120")