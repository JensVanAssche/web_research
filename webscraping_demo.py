from bs4 import BeautifulSoup

html_doc = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Webscraping Demo</title>
</head>
<body>
  <div id="header">
    <h1 class="title">Welcome to my webscraper demo</h1>
    <p class="subtitle">By Jens Van Assche for web research in python</p>
  </div>
  <div id="section-1">
    <h2 data-hello="sectiontitle">First section</h2>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
  </div>
  <div id="section-2">
    <h2 data-hello="sectiontitle">Second section</h2>
    <ul class="item-list">
      <li class="item">Item 1</li>
      <li class="item">Item 2</li>
      <li class="item">Item 3</li>
    </ul>
  </div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

## direct
# print(soup.body)
# print(soup.head)
# print(soup.head.title)

## find(), finds the first item
# el = soup.find('div')

## find_all() or findAll(), finds all items and returns array
# el = soup.find_all('div')
# el = soup.find_all('div')[1]

# el = soup.find(id='section-1')
# el = soup.find(class_='section-1')
# el = soup.find(attrs={'data-hello': 'sectiontitle'})

## select, returns array
# el = soup.select('#section-1')
# el = soup.select('#section-1')[0]
# el = soup.select('.item')[0]

## get_text(), get content in tags
# el = soup.find(class_='item').get_text() # only displays first item

# for item in soup.select('.item'): # gets all the items
# 	print(item.get_text())

## navigation
# el = soup.body.contents[1].contents[1].find_next_sibling() # [0] returns a linebreak, [1] returns first element, this returns .subtitle
# el = soup.find(id='section-2').find_previous_sibling() # this returns #section-1
# el = soup.find(class_='item').find_parent() # this returns ul
# el = soup.find('h2').find_next_sibling('p') # this returns the paragraph in section-1

print(el)