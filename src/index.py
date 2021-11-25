names = open("/Users/luca/Documents/GitHub/Data-mining/firstname.txt", "r")
#print(f.readlines())

from random import seed
from random import randint
import json
# seed random number generator
seed(1)
# generate some integers
#for _ in range(50):
	#value = randint(0, 160000)
	#print(value)

conditions = open("/Users/luca/Documents/GitHub/Data-mining/conditions.txt", "r")

therapies = open("/Users/luca/Documents/GitHub/Data-mining/therapies.txt", "w")

data = {
    "name" : names[randint(1, 100000)],
    "conditions" : conditions[randint(1, 600)]
}

print(data)

#print to json
with open("data.json", "w") as write_file:
    json.dump(data, write_file)