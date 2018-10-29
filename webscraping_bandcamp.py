from selenium import webdriver
from csv import writer
import os

BANDCAMP_FRONTPAGE = 'https://bandcamp.com/'
clear = lambda: os.system('cls')

class Bandcamp():
	def __init__(self):
		options = webdriver.ChromeOptions()
		options.add_argument('headless')
		options.add_argument('log-level=2')
		self.driver = webdriver.Chrome(options=options)

		self.search()

	def search(self):
		self.driver.get(BANDCAMP_FRONTPAGE)

		clear()
		print('Search for artist:')
		searchInput = input(">>> ")
		print('')
		print('Searching...')
		print('')

		self.driver.find_element_by_class_name("you-autocomplete-me").send_keys(searchInput)
		self.driver.find_element_by_css_selector("button[type='submit']").click()

		searchResults = self.driver.find_elements_by_class_name("album")
		self.list(searchResults)

	def list(self, searchResults):
		print('Albums found:')

		for val, searchResult in enumerate(searchResults):
			title = searchResult.find_element_by_css_selector(".heading a").get_attribute("innerHTML").strip()
			artist = searchResult.find_element_by_class_name("subhead").get_attribute("innerHTML").strip()
			print(val + 1, title, artist)
		print('')

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

		searchResults[chooseInput - 1].find_element_by_class_name("artcont").click()
		self.driver.find_element_by_class_name("playbutton").click()
		self.play()

	def play(self):
		album = self.driver.find_element_by_class_name("trackTitle").get_attribute("innerHTML").strip()
		artist = self.driver.find_element_by_css_selector("#name-section span[itemProp='byArtist'] a").get_attribute("innerHTML").strip()
		title = self.driver.find_element_by_class_name("title").get_attribute("innerHTML").strip()
		time = self.driver.find_element_by_class_name("time_total").get_attribute("innerHTML").strip()

		clear()
		print('NOW PLAYING:', title, 'by', artist)
		print('on', album)
		print('length:', time)
		print('')

		pause = 0;
		self.input(pause)

	def input(self, pause):
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
		print('Playing next song...')
		print('')
		self.driver.find_element_by_css_selector("a[aria-label='Next track']").click()
		self.play()

	def prev(self):
		print('Playing previous song...')
		print('')
		self.driver.find_element_by_css_selector("a[aria-label='Previous track']").click()
		self.play()

	def tracklist(self, pause):
		print('Tracklist:')
		tracklist = self.driver.find_elements_by_class_name("track_row_view")
		for val, track in enumerate(tracklist):
			title = track.find_element_by_css_selector("span[itemprop='name']").get_attribute("innerHTML").strip()
			print(val + 1, title)
		print('')

		self.input(pause)

	def playTrack(self):
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
		print('Stopping player...')
		print('')
		self.driver.quit()
		exit()

var = Bandcamp()