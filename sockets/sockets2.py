import urllib.request
from bs4 import BeautifulSoup
url = 'http://py4e-data.dr-chuck.net/known_by_Marni.html'
count = 7
pos = 18

for i in range(count):
    html = urllib.request.urlopen(url).read()
    sauce = BeautifulSoup(html, 'html.parser')
    tags = sauce.find_all('a')
    link = tags[pos - 1].get('href', None)
    print(f"Next link {i + 1}: {tags[pos - 1].text}")
    url = 'http://py4e-data.dr-chuck.net/' + link

print(f"last: {tags[pos - 1].text}")
