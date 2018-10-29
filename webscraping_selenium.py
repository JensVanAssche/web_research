# ipv request, gebruik ik de webdriver van selenium
from selenium import webdriver
from bs4 import BeautifulSoup
from csv import writer

# get url en voer de url uit door de driver
url = "https://www.reddit.com/r/all"
driver = webdriver.Chrome(executable_path="chromedriver")
driver.get(url)

# ik haal eerst alle posts binnen van de frontpage, allPosts wordt hiermee een array
allPosts = driver.find_elements_by_class_name("Post");

# start een csv file, zie webscraping_blog.py voor meer details
with open('redditposts.csv', 'w', newline='', encoding="utf-8") as csv_file:
	csv_writer = writer(csv_file)
	# headers voor in het document
	headers = ['title', 'subreddit', 'user', 'comments', 'time', 'link', 'upvotes']
	# schrijf de headers al in het document
	csv_writer.writerow(headers)

	# loop door de array allPosts, ga post per post af
	for post in allPosts:
		# gebruik innerHTML om de html te krijgen, anders is het nog een driver query
		postHTML = post.get_attribute("innerHTML")
		# parse deze html met beautifulsoup
		soup = BeautifulSoup(postHTML, "html.parser")

		# deze if statement haalt advertenties uit de posts, want advertenties zijn niet te onderscheiden van gewone posts via de classes
		# een advertentie heeft geen subreddit, dus daarop check ik elke post
		if soup.find(attrs={'data-click-id': 'subreddit'}) is None:
			# als het een advertentie is, skip de if statement en loop naar de volgende post
			continue
		else:
			# haal alle data die ik wil uit een post met beautifulsoup
			title = soup.find(class_="s56cc5r-0").get_text()
			subreddit = soup.find(attrs={'data-click-id': 'subreddit'})['href']
			user = soup.find(class_="_2tbHP6ZydRpjI44J3syuqC").get_text()
			comments = soup.find(class_="FHCV02u6Cp2zYL0fhQPsO").get_text()
			time = soup.find(attrs={'data-click-id': 'timestamp'}).get_text()
			# deze if statement voer ik uit omdat sommige posts naar externe paginas verwijzen en anderen niet
			# ik probeer eerst naar een link te zoeken die naar een externe pagina gaat. zoniet, pak de link die naar de redditpost zelf gaat
			if soup.find(class_='b5szba-0') is not None:
				link = soup.find(class_='b5szba-0')['href']
			else:
				link = soup.find(class_='SQnoC3ObvgnGjWt90zD9Z')['href']
			upvotes = soup.find(class_="_1rZYMD_4xY3gRcSS3p8ODO").get_text()
			# write de data van een post in 1 rij in het document
			csv_writer.writerow([title, subreddit, user, comments, time, link, upvotes])

# nadat alles goed is verlopen, print succes berichtje in de console
print('Successfully wrote hot posts of r/all to redditposts.csv')

# sluit de driver
driver.close()