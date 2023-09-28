import http.client
import json

apiKey = 'x'
urlBase = 'https://weatherapi-com.p.rapidapi.com/current.json?q='
apiHost = 'weatherapi-com.p.rapidapi.com'

connection = http.client.HTTPSConnection(apiHost)
headers = {'X-RapidAPI-Key': apiKey, 'X-RapidAPI-Host': apiHost}

zipCode = input('Enter a 5 digit US zip code:')

fullUrl = urlBase + zipCode

connection.request("GET", fullUrl, headers=headers)
response = connection.getresponse()
data = response.read()

weatherReport = json.loads(data.decode("utf-8"))

print('Weather Report for ' + weatherReport["location"]["name"] + ', ' + weatherReport["location"]["region"] + ':')
print('=========================================')
print('Conditions: ' + weatherReport['current']['condition']['text'])
print('Temperature: ' + str(weatherReport['current']['temp_f']) + ' Degrees F, but feels like ' + str(weatherReport['current']['feelslike_f']))
print('Humidity: ' + str(weatherReport['current']['humidity']) + '%')
print('Winds: ' + str(weatherReport['current']['wind_mph']) + ' mph out of the ' + weatherReport['current']['wind_dir'] + ' with gusts up to ' + str(weatherReport['current']['gust_mph']) + ' mph')
print('Barometric Pressure: ' + str(weatherReport['current']['pressure_in']) + ' in.')