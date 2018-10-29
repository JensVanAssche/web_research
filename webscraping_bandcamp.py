from selenium import webdriver
from csv import writer
import os

BANDCAMP_FRONTPAGE = 'https://bandcamp.com/'
clear = lambda: os.system('cls')

class Bandcamp():
	def __init__(self):
		# declareer de driver en zijn opties
		# de log-level optie zorgt ervoor dat niet elk info berichtje in de console verschijnt, enkel de errors
		options = webdriver.ChromeOptions()
		options.add_argument('headless')
		options.add_argument('log-level=2')
		self.driver = webdriver.Chrome(options=options)

		self.search()

	def search(self):
		# ga naar de frontpage
		self.driver.get(BANDCAMP_FRONTPAGE)

		# vraag user input
		clear()
		print('Search for artist:')
		searchInput = input(">>> ")
		print('')
		print('Searching...')
		print('')

		# vul de zoekbalk in op de frontpage met de user input en enter
		self.driver.find_element_by_class_name("you-autocomplete-me").send_keys(searchInput)
		self.driver.find_element_by_css_selector("button[type='submit']").click()

		self.list()

	def list(self):
		# verzamel al de album resultaten in een array
		searchResults = self.driver.find_elements_by_class_name("album")

		print('Albums found:')

		# loop door de album namen en artiestenamen en print ze
		for val, searchResult in enumerate(searchResults):
			title = searchResult.find_element_by_css_selector(".heading a").get_attribute("innerHTML").strip()
			artist = searchResult.find_element_by_class_name("subhead").get_attribute("innerHTML").strip()
			print(val + 1, title, artist)
		print('')

		# user input om een album te kiezen, inclusief errorhandling
		while 1 < 2:
			print('Choose album:')
			chooseInput = int(input(">>> "))
			print('')

			if len(searchResults) > chooseInput - 1:
				print('Playing album...')
				print('')
				break
			else:
				print('Error: Not a valid input')
				print('')

		# klik op het gekozen album en speel meteen af
		searchResults[chooseInput - 1].find_element_by_class_name("artcont").click()
		self.driver.find_element_by_class_name("playbutton").click()
		self.play()

	def play(self):
		# zoek de titel, artiest, album en speeltijd van het nummer
		album = self.driver.find_element_by_class_name("trackTitle").get_attribute("innerHTML").strip()
		artist = self.driver.find_element_by_css_selector("#name-section span[itemProp='byArtist'] a").get_attribute("innerHTML").strip()
		title = self.driver.find_element_by_class_name("title").get_attribute("innerHTML").strip()
		time = self.driver.find_element_by_class_name("time_total").get_attribute("innerHTML").strip()

		# toon deze
		clear()
		print('NOW PLAYING:', title, 'by', artist)
		print('on', album)
		print('length:', time)
		print('')

		# deze variable wordt gebruikt bij het pauseren van nummers
		pause = 0;
		self.input(pause)

	def input(self, pause):
		# user input voor veel opties, gaan elk naar hun eigen functie, inclusief errorhandling
		while 1 < 2:
			print('Commands: stop, pause, next, prev, tracks, play, search, help')
			playerInput = input(">>> ")
			print('')

			if playerInput == 'stop':
				self.stop()
			if playerInput == 'pause':
				self.pause(pause)
			if playerInput == 'next':
				self.next()
			if playerInput == 'prev':
				self.prev()
			if playerInput == 'tracks':
				self.tracklist(pause)
			if playerInput == 'play':
				self.playTrack()
			if playerInput == 'search':
				self.search()
			if playerInput == 'help':
				self.help(pause)
			else:
				print('Error: Not a valid input')
				print('')

	def pause(self, pause):
		# pauseert/speelt het nummer, aan de hand van de pause variable toont het de juiste tekst
		if pause == 0:
			print('Paused player')
			pause = 1
		else:
			print('Start player')
			pause = 0
		print('')
		self.driver.find_element_by_class_name("playbutton").click()
		self.input(pause)

	def next(self):
		# ga naar het volgende nummer
		print('Playing next song...')
		print('')
		self.driver.find_element_by_css_selector("a[aria-label='Next track']").click()
		self.play()

	def prev(self):
		# ga naar het vorige nummer
		print('Playing previous song...')
		print('')
		self.driver.find_element_by_css_selector("a[aria-label='Previous track']").click()
		self.play()

	def tracklist(self, pause):
		# haal de tracklist onderaan de pagina op en toon deze
		print('Tracklist:')
		tracklist = self.driver.find_elements_by_class_name("track_row_view")
		for val, track in enumerate(tracklist):
			title = track.find_element_by_css_selector("span[itemprop='name']").get_attribute("innerHTML").strip()
			print(val + 1, title)
		print('')

		self.input(pause)

	def playTrack(self):
		# kies een nummer uit de tracklist en speel deze af
		print('Tracklist:')
		tracklist = self.driver.find_elements_by_class_name("track_row_view")
		for val, track in enumerate(tracklist):
			title = track.find_element_by_css_selector("span[itemprop='name']").get_attribute("innerHTML").strip()
			print(val + 1, title)
		print('')

		print('Choose number:')
		chooseTrack = int(input(">>> "))
		print('')

		tracklist[chooseTrack - 1].find_element_by_css_selector(".play-col a").click()

		self.play()

	def help(self, pause):
		# toont wat de commands doen, geen extra functionaliteit
		print('COMMANDS:')
		print('STOP: stop & quit the app')
		print('PAUSE: pause and play the current track')
		print('NEXT: go to the next track')
		print('PREV: go to the previous track')
		print('TRACKS: see the tracklist of current album')
		print('PLAY: pick a song from the tracklist')
		print('SEARCH: search for another album')
		print('')

		self.input(pause)

	def stop(self):
		# stopt de driver en sluit het script af
		print('Stopping player...')
		print('')
		self.driver.quit()
		exit()

# roep de classe op
var = Bandcamp()
