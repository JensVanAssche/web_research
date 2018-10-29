# web_research

### New technology: Webscraping
Voor web reseach wil ik leren hoe ik moet web scrapen met python. In deze repo komt mijn progress te staan.

#### Stap 1: libraries voor python (bron 1, 2, 3 en 4)
Veel artikels schrijven over dezelfde libraries voor web scraping, namelijk requests, beautifulsoup en een csv writer. Deze ga ik dus ook gebruiken. Ik ga beginnen met een tutorial over beautifulsoup.

#### Stap 2: simpele scraper met beautifulsoup (bron 1)
Ik ben begonnen met een tutorial te volgen die de basics van de beautifulsoup library duidelijk maakt. Beautifulsoup is een van de meestgebruikte libraries voor het parsen van HTML en wordt dus veel gebruikt bij webscraping. Al snel heb ik door dat de library best krachtig is en veel selectie en zoekmogelijkheden heeft voor HTML paginas. \
Het is ook simpel en intuitief te gebruiken. Je moet de library importen, declaren in een variable als HTML parser en het een HTML pagina geven. In webscraping_demo.py geef ik de variable een statisch html_doc dat mee in het scriptje zit. Maar normaal zou je een url geven om een webpage te scrapen. \
Vervolgens kan je elementen uit de HTML selecteren via verschillende selectiemethodes. Ik heb wat met de selectiemethodes geëxperimenteerd en er een aantal in comments gezet in webscraping_demo.py als overzicht. De volgende stap nu is een echte website scrapen.

#### Stap 3: website scrapen en in een csv bestand zetten (bron 1 en 3)
Nu ga ik een echte website scrapen en de verkregen data in een csv bestand zetten. Waarom in een csv bestand? Omdat dit makkelijk in een database te zetten is en ook te bekijken is met excel. \
Een online website scrapen is niet veel verschillend van wat ik hiervoor deed. Als extra stap moet je een request doen naar de url van de website. Die url moet je dan parsen met beautifulsoup en je bent vertrokken! \
In webscraping_blog.py scrape ik blog.scrapinghub.com. Deze heeft duidelijke posts met titles en links. Ik scrape de title, link en datum van elke post en heb deze geschreven naar blogposts.csv. In het python bestand heb ik met comments elke lijn code verduidelijkt.

#### Stap 4: javascript omzeilen met selenium (bron 5, 6 en 7)
Maar wat met webpages die hun attributen toevoegen met javascript? Een request spreekt de sourcecode aan van een site en kan deze attributen dus niet detecteren. Ik ga dus iets nieuws moeten gebruiken in plaats van een simpele request. \
De oplossing is Selenium! Selenium is een webdriver die een instance van je webbrowser naar keuze uitvoert voor het de request doet. Hierdoor kan het de javascript gegenereerde attributen detecteren. In webscraping_selenium.py heb ik een simpel scriptje geschreven dat de top post van r/all van reddit scraped. Reddit is namelijk een site die veel attributen met javascript toevoegt. \
Enkel Selenium installeren is echter niet voldoende. Je moet nog de webdriver van je browser naar keuze locaal downloaden. Ik heb deze op mijn pc toegankelijk gemaakt via het PATH zodat python hier gemakkelijk aan kan. Python heeft dit nodig om de instance van de browser te maken.

#### Stap 5: headless driver en deprecation (bron 8 en 9)
Hierna begon ik wat rond te zoeken voor nog interessante dingen om te doen met Selenium. Ik vond een artikel dat uitlegd hoe Selenium sneller en effectiever werkt met een headless driver. Dat betekend wanneer de driver wordt geopend er geen letterlijke browser open moet maar dit allemaal achter de schermen gebeurt. Dit maakt Selenium inderdaad een pakje sneller sinds de browser niet moet laden en dergelijken. \
Ik ging aan de slag met de headless driver die het artikel voorstelde: PhantomJS (te installeren via npm). Dit werkte wel, maar de console liet mij weten dat de library depricated is, dus niet meer ondersteunt door Selenium. Ookal werkte PhantomJS wel, ik vond dit niet de beste driver om te gebruiken dan. \
Ver moest ik niet zoeken om te weten te komen dat de drivers van de grote browsers zoals Chrome en Firefox, ook een headless optie ondersteunen. Hier moest ik niets extra voor installeren sinds ik de chromedriver al heb geconfigureerd in de vorige stap. In webscraping_selenium_headless.py heb ik zowel mijn PhantomJS scriptje als mijn headless Chrome scriptje geschreven. Dit is puur als voorbeeld om te tonen dat het werkt, het scriptje zelf doet niets nuttig.

#### Bronnen:
[1. Introductie Youtube video](https://www.youtube.com/watch?v=4UcqECQe5Kc) \
[2. BeautifulSoup documentatie](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) \
[3. Introductie artikel 1](https://towardsdatascience.com/an-introduction-to-web-scraping-with-python-bc9563fe8860) \
[4. Introductie artikel 2](https://realpython.com/python-web-scraping-practical-introduction/) \
[5. Selenium artikel](https://enginebai.com/2017/04/12/advanced-web-scraping-in-python/) \
[6. Selenium installatie documentatie](https://selenium-python.readthedocs.io/installation.html) \
[7. Chrome driver download](https://sites.google.com/a/chromium.org/chromedriver/downloads) \
[8. Headless Selenium met PhantomJS](https://realpython.com/headless-selenium-testing-with-python-and-phantomjs/) \
[9. Headless Selenium met Chrome](https://stackoverflow.com/questions/48537028/selenium-how-to-use-headless-chrome-on-aws)
