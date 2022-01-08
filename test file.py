import json

x = input('welke getal ')
with open ('steam.json') as json_file:
    data = json.load(json_file)

    print(data[x]['name'])
