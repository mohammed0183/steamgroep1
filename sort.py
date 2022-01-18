
# import urllib library
from urllib.request import urlopen

# import json
import json
# store the URL in url as
# parameter for urlopen
url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=C808AFD79C4F1A523682FF587DFC4481&steamids=76561198992221003"

# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
with open(response, 'r') as inside:
            data = json.load(inside)

data_json = json.dumps(data, indent=2)

# print the json response
print(data_json)