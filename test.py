import matplotlib.pyplot as plt
import json

dictionary = json.load(open('steam.json', 'r'))
xAxis = [ sub['median_playtime'] for sub in dictionary ]
yAxis = [ sub['name'] for sub in dictionary ]
plt.grid(True)

## LINE GRAPH ##
plt.plot(xAxis,yAxis, color='maroon', marker='o')
plt.xlabel('variable')
plt.ylabel('value')

## BAR GRAPH ##
fig = plt.figure()
plt.bar(xAxis,yAxis, color='maroon')
plt.xlabel('variable')
plt.ylabel('value')

plt.show()