from urllib.request import urlopen

def application(environ, start_response):
	request = str(environ['REQUEST_URI']).split("?")
	url = request[1]
	word = request[2]
	html = gethtml(url)
	output = match(word,html)

	response_headers = [('Content-type', 'text/plain'),
	('Content-Length', str(len(output)))]
	status = '200 OK'
	start_response(status, response_headers)

	return [bytes(output, 'utf-8')]

def gethtml(url):
	html = urlopen(url)
	return str(html.read())

def match(word,html):
	if html.find(word)>=0:
		return 'si'
	else: 
		return 'no'


