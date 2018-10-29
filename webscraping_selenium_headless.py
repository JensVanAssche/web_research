from selenium import webdriver

# phantomjs voorbeeld, depricated

# driver = webdriver.PhantomJS(executable_path='C:/Users/Jens/AppData/Roaming/npm/node_modules/phantomjs-prebuilt/lib/phantom/bin/phantomjs')
# driver.get("https://duckduckgo.com/")
# driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
# driver.find_element_by_id("search_button_homepage").click()
# print (driver.current_url)
# driver.quit()


# headless chrome voorbeeld

# declareer headless optie
options = webdriver.ChromeOptions()
options.add_argument('headless')

# declareer driver met headless optie
driver = webdriver.Chrome(options=options)
# voer simpel scriptje uit
driver.get("https://duckduckgo.com/")
driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
driver.find_element_by_id("search_button_homepage").click()
print (driver.current_url)
driver.quit()