# Brace yourself, the cube is coming!
from shutil import copyfile
from random import randint, choice
import json
ROOMS = 200
OUT_DIR = "cube/"
TEMPLATES = ["cube_assets/quadrat_t1.json","cube_assets/quadrat_t2.json","cube_assets/quadrat_t3.json"]

for x in range(0,ROOMS):
    template = choice(TEMPLATES)
    output = OUT_DIR + str(x) + ".json"
    copyfile(template, output)

    #tile post processing
    with open(output, 'r') as file:
        room = json.load(file)
        for layer_i in range(0, len(room['layers'])):
            if room['layers'][layer_i]['name'].startswith('exit'):
                room['layers'][layer_i]['properties'][0]['value'] = str(randint(0,ROOMS)) + '.json'

    with open(output, 'w') as file:
        json.dump(room, file)

## generate an exit
exit = randint(0,200)
exit_door = randint(1,4)

with open(OUT_DIR+str(exit)+".json", 'r') as file:
    room = json.load(file)
for layer_i in range(0, len(room['layers'])):
    if room['layers'][layer_i]['name'] == 'exit' + str(exit_door):
        room['layers'][layer_i]['properties'][0]['value'] = '../main.json'

with open(OUT_DIR+str(exit)+".json", 'w') as file:
    json.dump(room, file)

print("Exitroom:", exit, "Exitlayer", exit_door)
