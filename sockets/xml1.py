import urllib.request
import xml.etree.ElementTree as ET

url = "http://py4e-data.dr-chuck.net/comments_2134071.xml"
response = urllib.request.urlopen(url)
data = response.read()
tree = ET.fromstring(data)
sum = 0

for comment in tree.findall('.//comment'):
    num = comment.find('count').text
    sum += int(num)  
print('sum:', sum)
