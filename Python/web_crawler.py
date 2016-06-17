"""
In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find. 

Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Deecan.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: M

"""
import urllib
from BeautifulSoup import *

url = raw_input("Enter URL: ")
if len(url) < 1 : url = "http://python-data.dr-chuck.net/known_by_Deecan.html"

position = raw_input("Enter link position: ")
times = raw_input("How many times to repeat: ")

def web_crawler(url, position, times) :
	counter = 0
	links = list()

	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)

	while counter < int(times) :
		soup = BeautifulSoup(html)

		for link in soup.findAll('a', href=True):
			links.append(link.get('href', None))

		newUrl = links[int(position)-1]
		print newUrl
		html = urllib.urlopen(newUrl).read()
		links[:]=[]
		
		counter += 1
		
	print "Final URL is: ", newUrl

web_crawler(url, position, times)