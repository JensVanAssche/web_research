# web_research

### New technology:
Voor web reseach wil ik leren hoe ik moet web scrapen met phython. In deze repo komt mij progress te staan.

#### Stap 1: libraries voor python
Veel artikels schrijven over dezelfde libraries voor web scraping, namelijk requests, beautifulsoup en een data manipulator en een csv writer. Deze ga ik dus ook gebruiken.

#### Stap 2: simpele scraper met beautifulsoup
Ik ben begonnen met een tutorial te volgen die de basics van de beautifulsoup library duidelijk maakt. Al snel heb ik door dat de library best krachtig is en veel selectie en zoekmogelijkheden heeft voor html paginas. Ik heb hierwat mee geëxperimenteerd en een aantal van de methodes in comments gezet in webscraping_demo.py. De volgende stap nu is een echte website scrapen.

#### Stap 3: website scrapen en in een csv bestand zetten
Nu ga ik echte site scrapen en bespaalde data in een csv bestand zetten. Waarom in een csv bestand? Omdat dit makkelijk in een database te zetten is en ook te bekijken is met excel.\
In webscraping_blog.py scrape ik blog.scrapinghub.com. Deze heeft een duidelijke posts met titles en links. Ik scrape de title, link en datum van elke post en heb deze in blogposts.csv gezet. In het python bestand heb ik met comments elke lijn code verduidelijkt.

#### Stap 4: javascript omzeilen met selenium
Maar wat met webpages die hun attributen toevoegen met javascript? Een gewone request kan deze niet detecteren. Ik ga dus iets nieuws moeten gebruiken ipv een simpele request.\
De oplossing is Selenium! Selenium is een webdriver die een instance van je webbrowser naar keuze uitvoert voor het de request doet. Hierdoor kan het toch de javascript gegenereerde attributen detecteren. In webscraping_selenium.py heb ik een simpel scriptje geschreven dat de top post van r/all van reddit scraped. Reddit is namelijk zo'n site die veel attributen met javascript toevoegt.\
Enkel Selenium installeren is echter niet voldoende. Je moet nog de webdriver van je browser naar keuze downloaden. Ik heb deze toegankelijk gemaakt via het PATH zodat pyhton hier gemakkelijk aan kan. Pyhton heeft dit nodig om de instance van de browser te maken.

#### Bronnen:
https://realpython.com/python-web-scraping-practical-introduction/ \
https://towardsdatascience.com/an-introduction-to-web-scraping-with-python-bc9563fe8860 \
https://www.crummy.com/software/BeautifulSoup/bs4/doc/ \
https://www.youtube.com/watch?v=4UcqECQe5Kc
https://enginebai.com/2017/04/12/advanced-web-scraping-in-python/
https://selenium-python.readthedocs.io/
https://selenium-python.readthedocs.io/installation.html
https://sites.google.com/a/chromium.org/chromedriver/downloads
