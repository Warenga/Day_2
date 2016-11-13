import sys

from urllib2 import Request, urlopen, URLError

def main(argv):

	no_of_facts = raw_input('How many facts do you want?')

	url = 'http://catfacts-api.appspot.com/api/facts?number=' + no_of_facts 
	
	try:
		catfacts = urlopen(url).read()
		facts_only = catfacts[12:-21]
		k = f.split('", "')
		for facts in k:
			print '> ' + facts + '\n'

	except URLError, e:
		print 'Error code:', e

if __name__ == '__main__':
	main(sys.argv)