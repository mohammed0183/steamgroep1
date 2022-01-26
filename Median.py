import json
json_filename = 'steam.json'
with open(json_filename, 'r') as inside:
     data = json.load(inside)



# Using list comprehension
# Get values of particular key in list of dictionaries
res = [ sub['appid'] for sub in data ]

# printing result
def median(res):
    res.sort() # lst word gesorteerd
    lengte = len(res)
    if len(res) % 2 == 0: # kijken of de lijst even is zo ja , dan moeten we 2 medianen gebruiken
        first_median = res[lengte // 2] # Eerste median
        second_median = res[lengte // 2 - 1] # Tweede median
        mediaan = (first_median + second_median) / 2 # hier heb je het gemiddelde van de mediaanen
    else:
        mediaan = res[lengte // 2] #dit is wanneer een lijst oneven is, dan is het gewoon gedeelt door 2
    return float(mediaan)
print(median(res))



# als de lengte van de lijst gedeeld door 2 gelijk is an 0
# dan is de eerste variabele lengte van de lijst gedeeld door 2
# en de 2de variable is de lengte van de lijst gedeeeld door 2 -1
# het gemiddedelde van deze 2 variable is de mediaan
# wanneer een lijst on even is is de mediaan de legte van de lijst gedeeld door 2