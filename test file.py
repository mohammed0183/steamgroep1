import json


x = int(input('welke getal '))
with open ('steam.json') as json_file:
    data = json.load(json_file)

for i in data:
    if i['appid'] == x:
        print(i['appid'])
        print(i['name'])
        print(i['release_date'])
        print(i['english'])
        print(i['developer'])
        print(i['publisher'])
        print(i['platforms'])

        break

