import sys, click, json
from urllib2 import Request, urlopen, URLError

@click.command()
def main():
	"""
	This scripts prints fun cat facts.
	Call the script and it will ask you
	how many facts you want to know.

	
	After seeing your facts, you are given an option to save them
	so that you can share it with others.

	Enjoy :)

	"""

	# no_of_facts = raw_input('How many facts do you want? ')

	# if no_of_facts == '':
	# 	no_of_facts = '0' 
	# try: 
	# 	if int(no_of_facts) > 100:
	# 		print 'Woah!! too many facts. Can only display maximum of 100 facts'
	# 		no_of_facts = raw_input('Please try again. How many facts do you want?')
	# except:
	# 	print "Oh Oh...That's not a number"
	# 	no_of_facts = raw_input('Please try again. How many facts do you want?')

	while True:
		no_of_facts = raw_input('How many facts do you want? ')
		if no_of_facts == '':
			no_of_facts = '0'
			break
		try: 
			if int(no_of_facts) > 100:
				print '\nWoah!! too many facts. Can only display maximum of 100 facts.\nPlease try again.'
				continue
		except:
			print "\nOh Oh...That's not a number.\nPlease try again.\n"
			continue
		break


	url = 'http://catfacts-api.appspot.com/api/facts?number=' + no_of_facts 
	
	try:
		catfacts = urlopen(url).read()

		facts_only = catfacts[12:-21]
		k = facts_only.split('", "')
		for facts in k:
			print '> ' + facts + '\n'

		save_file = raw_input("Would you like to save these facts? 'Yes' 'No': ")

		if save_file.lower() == 'Yes':
			try:
				file = open('catfacts.txt', 'wb')
				file.write(catfacts)
				file.close()
				print 'Your facts has been saved as catfacts.txt'
			except URLError, e:
				print 'Error code:',e
		else:
			print "Thank You"
	except URLError, e:
		print 'Error code:', e

if __name__ == '__main__':
	main()