import json
import pprint


with open ('steam.json') as json_file:
    data = json.load(json_file)

sorted_list = sorted(data, key=lambda k: int(k['appid']), reverse = False)

print(sorted_list)