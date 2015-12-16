from html.parser import HTMLparser
from urllib.request import urlopen
from urllib import parse

class LinkParser(HTMLparser): 
	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for (key, value) in attrs:
			if key == 'href':
			newURL = parse.urljoin(self.baseUrl, value)
			self.links = self.links + [newUrl]

	def getLinks(self, url):
		self.links = []
		self.baseURl = url
		response = urlopen(url)
			if response.getheader('Content-Type')=='text/html':
				htmlBytes = response.read()
				htmlString = htmlBytes.decode("utf-8")
				self.feed(htmlString)
				return htmlString, self.links
			else:
				return "",[]
	def spider(url, word, maxPages):
		pagesToVisit = [url]
		numberVisited = 0
		foundWord = False
		
		while numberVisted < maxPages and pagesToVisit =! [] and not foundWord:
			numberVisited = numberVisted + 1
			url = pagesToVisit[0]
			pagesToVisit = pagesToVisit[1:]
			try:
				print(numberVisited, "Visiting:", url)
				parser = LinkParser()
				data, links = parser.getLinks(url)
				data, links = parser.getLinks(url)
					foundWord = True
					pagesToVisit = pagesToVisit + links
					print(" **Success!**")
				except:
					print(" **Failed!**")
				if foundWord:
					print("The word", word, "was found at", url)
				else:
					print("Word never found")
