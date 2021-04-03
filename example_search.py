import json

#search = 'MacBook'
#search = 'Apple MacBook Pro 13-Inch "Core i7" 1.7 Touch/2019 2 TB 3'
search = 'MacBookPro15,4'

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
				for component, info in spec.items():
					print('Component:', component)
					print('Specs:', info)
			
			#print(item['prices'])
			for price in item['prices']:
				for country, amount in price.items():
					print(country, amount)