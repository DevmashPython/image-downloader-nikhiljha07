import urllib2
import re
import time

url = raw_input("ENTER THE URL: ")
new = urllib2.urlopen(url)
html= new.read()

nk1 = re.compile('img src=[ "](.*?)"')
imgurl = re.findall(nk1,html)

print imgurl
imgurl=imgurl+['\0']

a=0
output = open('output.txt','a')

while(1):
	output.write(imgurl[a]+"\n")
	a=a+1
	if(imgurl[a]=='\0'):
		break

output.close()





