"""

Scraping Numbers from HTML using BeautifulSoup

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://python-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://python-data.dr-chuck.net/comments_234799.html (Sum ends with 33)

You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers. 

"""

import urllib
from BeautifulSoup import *

url = "http://python-data.dr-chuck.net/comments_234799.html"

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve a list of the span tags
tags = soup("span")

sumall = []

for tag in tags : 
	number = tag.contents[0] # Gets all the contents inside <span>
	sumall.append(int(number)) # appends the numbers to sumall list

print sum(sumall)