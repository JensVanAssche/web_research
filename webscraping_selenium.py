# ipv request, gebruik ik de webdriver van selenium
from selenium import webdriver
from bs4 import BeautifulSoup

# get url en execute die url door de driver
url = "https://www.reddit.com/r/all"
driver = webdriver.Chrome(executable_path="chromedriver")
driver.get(url)

# ik zoek de eerste post op r/all, en met innerHTML krijg ik de volle html van die post
# zonder innerHTML werkt selenium niet
content_element = driver.find_element_by_class_name("Post")
content_html = content_element.get_attribute("innerHTML")

# vervolgens kan ik met beautiful soup de html parsen en weer specifieke zoekopdrachten uitvoeren zoals ik al heb geleerd
soup = BeautifulSoup(content_html, "html.parser")
print(soup)

# sluit de driver
driver.close()