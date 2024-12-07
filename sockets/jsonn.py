import urllib.parse, urllib.request, urllib.error
import json

location = input("Enter location: ")    
apiBase = 'http://py4e-data.dr-chuck.net/opengeo?'
params = {"q": location}
url = apiBase + urllib.parse.urlencode(params)
print("Retrieving", url)

response = urllib.request.urlopen(url)
data = response.read().decode()
print(f"Retrieved {len(data)} characters")


try:
    jsonData = json.loads(data)
except json.JSONDecodeError as e:
    print("Error parsing JSON:", e)
    exit()

plusCode = jsonData['features'][0]["properties"]['plus_code']

if plusCode:
    print("Plus code", plusCode)
else:
    print("No plus code found")
