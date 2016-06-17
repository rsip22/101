import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
if len(url) < 1 : url = 'http://python-data.dr-chuck.net/comments_234796.xml'

print 'Retrieving ', url
uh = urllib.urlopen(url)
data = uh.read()

tree = ET.fromstring(data) # parses XML from a string directly into an Element

sumall = []

for count in tree.iter('count'): # iterate recursively over all the sub-tree below it 
	sumall.append(int(count.text)) # gets the text inside the tag, transforms it into integer and adds to the list

print 'Retrieved ', len(data), ' characters'
print 'Count: ' + str(len(sumall))
print 'Sum: ' + str(sum(sumall))