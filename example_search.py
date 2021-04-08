# Example script illustrating how to search the resulting database.json file created by scraper.py

import json

# Example searches: (could be anything)
#search = 'MacBook'
#search = 'Apple MacBook Pro 13-Inch "Core i7" 1.7 Touch/2019 2 TB 3'
search = 'MacBookPro15,4'
# search = 'A2159'

with open('database.json') as f:
    data = json.load(f)

for item in data['products']:
	for key, value in item.items():
		if search in value:
			print(item['title'])
			print(item['identifiers'])

			#print(item['specs'])
			for spec in item['specs']:
				#print(spec)
				for element in spec:
					for title, information in element.items():
						print(title + ':', information)
			
			#print(item['prices'])
			for price in item['prices']:
				for country, amount in price.items():
					print(country, amount)
