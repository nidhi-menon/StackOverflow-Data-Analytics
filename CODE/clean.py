import re
import csv
import json
import sys
from pyreadability.readability import Readability

def cleanhtml(raw_html):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext

def main():
	reload(sys)  
	sys.setdefaultencoding('utf8')
	with open('output58900_68900.csv', 'rb') as f:
		reader = csv.reader(f)
		writer = csv.writer(open('data58900_68900.csv', 'w'))
		# headers = reader.next()
		# headers.append("Cleaned Post")
		# headers.append("Readability")
		# headers.append("Number of code fragments")
		# headers.append("Word count")
		# headers.append("Number of external links")
		# writer.writerow(headers)
		for row in reader:

			# row[1] = row[1].encode('ascii', 'ignore').decode('ascii')

			no_of_code_frag = row[1].count("<code>")

			no_of_external_links = row[1].count("href")

			cleantext = cleanhtml(re.sub('<code>.*?</code>','',row[1], flags=re.DOTALL))

			# cleantext = cleantext.replace('\n','')
			# cleantext = cleantext.replace('\t','')

			word_count = len(row[1].split())

			row.append(cleantext)
			# print "Hello"
			r = Readability(cleantext)
			row.append(r.flesch_kincaid)
			row.append(no_of_code_frag)
			row.append(word_count)
			row.append(no_of_external_links)
			# print r.smog
			# num_words = 0
			# for line in cleanhtml(row[1]):
				# words = str(line).split(" ")
				# num_words += len(words)
				# row.append(num_words)
			writer.writerow(row)

if __name__ == "__main__":
	main()