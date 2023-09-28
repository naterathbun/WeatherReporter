import http.client

apiKey = 'x'
urlBase = 'https://weatherapi-com.p.rapidapi.com/current.json?q='
apiHost = 'weatherapi-com.p.rapidapi.com'

connection = http.client.HTTPSConnection(apiHost)

headers = {
    'X-RapidAPI-Key': apiKey,
    'X-RapidAPI-Host': apiHost
}

zipCode = '60565' # for testing

fullUrl = urlBase + zipCode
connection.request("GET", fullUrl, headers=headers)

res = connection.getresponse()
data = res.read()

print(data.decode("utf-8"))