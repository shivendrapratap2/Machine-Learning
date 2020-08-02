from bs4 import BeautifulSoup
from requests import get
import pandas as pd
from time import sleep
from random import randint

urls = ['https://m.imdb.com/list/ls068010962/', 'https://m.imdb.com/list/ls068010962/?page=2']
home_page = 'https://m.imdb.com'

celebs_info = list()

for url in urls:
	response = get(url)
	html_soup = BeautifulSoup(response.text, 'html.parser')
	data_containers = html_soup.find_all('div', class_ = 'media')
		
	for container in data_containers:

		info_dict = dict()
		name = container.find('a', class_ = 'btn-full').span.h4.text
		info_dict['name'] = name

		image = container.find('span', class_ = 'pull-left poster-wrap').a.img['src']
		info_dict['image'] = image

		P_trait = container.find('a', class_ = 'btn-full')['href']
		aboutLink = home_page+P_trait

		# getting personal data
		print("Getting Data of ", aboutLink)
		about = get(aboutLink)
		html_about_soup = BeautifulSoup(about.text, 'html.parser')

		about_data_containers = html_about_soup.find("section", {"id": "did-you-know"})
		if about_data_containers is not None:
			dyk_data = [data.text for data in about_data_containers.find_all("p")]
			dyk_header = [header.text for header in about_data_containers.find_all("h3")]

			for info in zip(dyk_data, dyk_header):
				data, header = info
				info_dict[header] = data

		traits_containers = html_about_soup.find("section", {"id": "personal-details"})
		if traits_containers is not None:
			traits_data = []
			traits_header = [header.text for header in traits_containers.find_all("h3")]
			for header in traits_containers.find_all("h3"):
				if header.find_next() == header.find_next("p"):
					traits_data.append(";".join([data.text.replace('\n', '') for data in header.find_next("p").find_all('span')]))
				else:
					traits_data.append(header.find_next("span").text.replace('\xa0', ''))
			
			for info in zip(traits_data, traits_header):
				data, header = info
				info_dict[header] = data
		else:
			print('traits_container is None for %s', info_dict['name'])

		awards_containers = html_about_soup.find("section", {"id": "awards"})		
		if awards_containers is not None:
			awards_data = [data.text for data in awards_containers.find_all("span")]
			awards_header = [header.text for header in awards_containers.find_all("h2")]

			for info in zip(awards_data, awards_header):
				data, header = info
				info_dict[header] = data
		else:
			print('awards_container is None for %s', info_dict['name'])

		# append info_dict
		celebs_info.append(info_dict)

print("Total personal data: ", len(celebs_info))

with open('celebsData.txt', 'w+') as f:
	f.write(str(celebs_info))

df = pd.DataFrame(data= None)
for i, info_dict in enumerate(celebs_info):
	temp_df = pd.DataFrame(info_dict, index= [i])
	df = pd.concat([df, temp_df], axis= 1)

df.to_csv('celebsData.csv', index= False)
