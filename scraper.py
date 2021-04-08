from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json
import pandas as pd
import re
import requests
import urllib3

def getsystems(session, ua):
	url = 'https://everymac.com/systems/apple/index-apple-specs-applespec.html'
	headers = {
		'User-Agent': ua.random
	}
	try:
		r = session.get(url, headers=headers, verify=False)
		print('GET System Spec URLS')
		soup = BeautifulSoup(r.text, 'html.parser')
		url_list = []
		for element in soup.findAll('a'):
			try:
				if re.search('/systems/apple/', element.get('href')):
					url_list.append(element.get('href'))
			except:
				pass
		return url_list
	except:
		print('Error: Unable Acquire List')

def getmodels(session, url_chunk, ua):
	url = 'https://everymac.com' + url_chunk
	headers = {
		'User-Agent': ua.random
	}
	try:
		r = session.get(url, headers=headers, verify=False)
		print('GET Models for:', url_chunk)
		soup = BeautifulSoup(r.text, 'html.parser')
		modelslist = []
		for element in soup.findAll('a'):
			try:
				if re.search(url_chunk, element.get('href')) and 'faq' not in element.get('href'):
					modelslist.append(element.get('href'))
			except:
				pass
		return modelslist
	except:
		print('Error: Unable Acquire Models for:', url_chunk)

def getspecs(session, model_url, ua):
	url = 'https://everymac.com' + model_url
	headers = {
		'User-Agent': ua.random
	}
	try:
		# Initialize Variables
		currency = False
		count = 1
		combined = []
		master = {
			'title': None,
			'identifiers': [],
			'specs': [],
			'prices': []
		}

		r = session.get(url, headers=headers, verify=False)
		print('GET Specs for:', model_url)
		soup = BeautifulSoup(r.text, 'html.parser')
			
		# Acquire Title
		title = soup.find('div', {'id': 'contentcenter'}).find('h3').text
		if 'Specs' in title:
			title = title.replace('Specs', '')
		master['title'] = title

		# Acquire Identifiers
		identifiers = soup.find('div', {'id': 'contentcenter'}).find('p', {'class': 'specstop'}).text
		identifiers_fixed = identifiers.split(' - ')
		identifiers_final = []
		for item in identifiers_fixed:
			#new = item.replace(' ', '').replace('Identifiers:', '')
			new = item.replace('Identifiers:', '')
			identifiers_final.append(new)
			
		master['identifiers'].extend(identifiers_final)

		dfs = pd.read_html(r.text)
			
		for df in dfs:
			# Spec
			if 3 in df.columns:
				if 'Canada' in df[0][0]:
					currency = True
			
				if currency == False:
					# add specs to combined
					combined.append({str(df[0][0]).replace(':', ''): str(df[1][0])})
					combined.append({str(df[2][0]).replace(':', ''): str(df[3][0])})
						
				else:
					# Once currency = True, counter no longer used
					# add currency to master
					master['prices'].append({str(df[0][0]).replace(':', ''): str(df[1][0])})
					master['prices'].append({str(df[2][0]).replace(':', ''): str(df[3][0])})
				
			# Details
			else:
				# add spec details to combined
				combined.append({str(df[0][0]).replace(':', ''): str(df[1][0])})
				count += 1

			# Append to Master:
			if count % 2 == 0:
				# if cound divisible by 2, is even, which means details section for the previous iteration
				# add combined specs & details to master then reset combined for next iteration
				master['specs'].append(combined)
				
				# Re-Initialize dictionary
				combined = []
				count = 1
			
		#print(master)
		return master
	except:
		print('Error: Unable Acquire Specs for:', model_url)

# main program
def main(session, ua):
	# 1. get base system types (i.e. macbooks, macbook pros)
	# 2. then get all models for seach system type
	# 3. then grab specs for each model type

	#Initialize database
	database = {
		'products': []
	}

	# initialize skips - registers already acquired to avoid duplicates
	skip_systems = []
	skip_models = []
	skip_systems.append('/systems/apple/')
	skip_models.extend(['/systems/apple/ipod/', '/systems/apple/iphone/', '/systems/apple/ipad/'])
	
	systems = getsystems(session, ua)
	for system in systems:
		if system not in skip_systems:

			# Special Case #1
			if system == '/systems/apple/20th_mac/specs/20th-anniversary-mac.html':
				specs = getspecs(session, system, ua)
				database['products'].append(specs)
				skip_models.append(model)
			# Special Case #2
			if system == '/systems/apple/messagepad/stats/emate_300.html':
				#specs = getspecs(session, system)
				#database['products'].append(specs)
				skip_models.append(model)

			models = getmodels(session, system, ua)
			for model in models:
				if model not in skip_models:
					specs = getspecs(session, model, ua)
					database['products'].append(specs)
					skip_models.append(model)

		skip_systems.append(system)
	
	with open('database.json', 'w') as f:
  		json.dump(database, f, indent=4)

# Initialize UserAgent
ua = UserAgent()

urllib3.disable_warnings()
session = requests.Session()

main(session, ua)
print('Acquisistion Complete')