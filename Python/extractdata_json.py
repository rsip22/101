"""
In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below.

Actual data: http://python-data.dr-chuck.net/comments_234800.json (Sum ends with 73)

"""

import urllib
import json

url = raw_input('Enter location: ')
if len(url) < 1 : url = 'http://python-data.dr-chuck.net/comments_234800.json'

print 'Retrieving', url

uh = urllib.urlopen(url)
data = uh.read()

info = json.loads(data)
print 'Retrieved', len(data), 'characters'

sumall = []

for item in info['comments'] :
  number = item['count']
  sumall.append(number)

print 'Count:', len(sumall)
print 'Sum:', sum(sumall)