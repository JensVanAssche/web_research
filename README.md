# web_research

### New technology: Webscraping
Voor web reseach wil ik leren hoe ik moet web scrapen met python. In deze repo komt mij progress te staan.

#### Stap 1: libraries voor python
Veel artikels schrijven over dezelfde libraries voor web scraping, namelijk requests, beautifulsoup en een csv writer. Deze ga ik dus ook gebruiken. Ik ga beginnen met een tutorial over beautifulsoup.

#### Stap 2: simpele scraper met beautifulsoup
Ik ben begonnen met een tutorial te volgen die de basics van de beautifulsoup library duidelijk maakt. Beautifulsoup is een van de meestgebruikte libraries voor het parsen van HTML en wordt dus veel gebruikt bij webscraping. Al snel heb ik door dat de library best krachtig is en veel selectie en zoekmogelijkheden heeft voor HTML paginas. \
Het is ook simpel en intuitief te gebruiken. Je moet de library importen, declaren in een variable als HTML parser en het een HTML pagina geven. In webscraping_demo.py geef ik de variable een statisch html_doc dat mee in het scriptje zit. Maar normaal zou je een url geven om een webpage te scrapen. \
Vervolgens kan je elementen uit de HTML selecteren via verschillende selectiemethodes. Ik heb wat met de selectiemethodes geëxperimenteerd en er een aantal in comments gezet in webscraping_demo.py als overzicht. De volgende stap nu is een echte website scrapen.

#### Stap 3: website scrapen en in een csv bestand zetten
Nu ga ik een echte website scrapen en de verkregen data in een csv bestand zetten. Waarom in een csv bestand? Omdat dit makkelijk in een database te zetten is en ook te bekijken is met excel.\
Een online website scrapen is niet veel verschillend van wat ik hiervoor deed. Als extra stap moet je een request doen naar de url van de website. Die url moet je dan parsen met beautifulsoup en je bent vertrokken! \
In webscraping_blog.py scrape ik blog.scrapinghub.com. Deze heeft duidelijke posts met titles en links. Ik scrape de title, link en datum van elke post en heb deze geschreven naar blogposts.csv. In het python bestand heb ik met comments elke lijn code verduidelijkt.

#### Stap 4: javascript omzeilen met selenium
Maar wat met webpages die hun attributen toevoegen met javascript? Een request spreekt de sourcecode aan van een site en kan deze attributen dus niet detecteren. Ik ga dus iets nieuws moeten gebruiken in plaats van een simpele request. \
De oplossing is Selenium! Selenium is een webdriver die een instance van je webbrowser naar keuze uitvoert voor het de request doet. Hierdoor kan het de javascript gegenereerde attributen detecteren. In webscraping_selenium.py heb ik een simpel scriptje geschreven dat de top post van r/all van reddit scraped. Reddit is namelijk een site die veel attributen met javascript toevoegt. \
Enkel Selenium installeren is echter niet voldoende. Je moet nog de webdriver van je browser naar keuze locaal downloaden. Ik heb deze op mijn pc toegankelijk gemaakt via het PATH zodat python hier gemakkelijk aan kan. Python heeft dit nodig om de instance van de browser te maken.

#### Bronnen:
https://realpython.com/python-web-scraping-practical-introduction/ \
https://towardsdatascience.com/an-introduction-to-web-scraping-with-python-bc9563fe8860 \
https://www.crummy.com/software/BeautifulSoup/bs4/doc/ \
https://www.youtube.com/watch?v=4UcqECQe5Kc \
https://enginebai.com/2017/04/12/advanced-web-scraping-in-python/ \
https://selenium-python.readthedocs.io/ \
https://selenium-python.readthedocs.io/installation.html \
https://sites.google.com/a/chromium.org/chromedriver/downloads
