import requests
from bs4 import BeautifulSoup
from csv import writer

# request de website die je wilt scrapen
response = requests.get('https://blog.scrapinghub.com/')
# parse de html van die site
soup = BeautifulSoup(response.text, 'html.parser')

# first, get all the posts from the page, by class
posts = soup.find_all(class_='post-item')

# start met naar een csv file te schrijven
# blogposts.csv is de naam v d file, w betekend write to file, newline zorgt ervoor dat er geen dubbele enters gebeuren in het bestand
# ik definieer ook een csv_write variabele die de writer library gaat gebruiken voor de csv_file
# er moeten ook headers in het bestand, dus 'headers' definieert deze en worden als eerste in het bestand geschreven met csv_writer.writerow
with open('blogposts.csv', 'w', newline='') as csv_file:
	csv_writer = writer(csv_file)
	headers = ['Title', 'Link', 'Date']
	csv_writer.writerow(headers)

	# vervolgens loop ik door de posts en scrape de titels, links en data en write deze ook post per post in het bestand
	for post in posts:
		title = post.find('h2').get_text()
		link = post.find('a')['href']
		date = post.select('.date a')[0].get_text()
		csv_writer.writerow([title, link, date])

# en eindig met een confirmatie in de console
print('done')