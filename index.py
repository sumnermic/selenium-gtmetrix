from selenium import webdriver 

website_url = "https://www.google.com/"
driver = webdriver.Firefox()

driver.get("https://gtmetrix.com/")

text_area = driver.find_element_by_css_selector("form.js-form-analyze .js-analyze-form-url")
form_button = driver.find_element_by_css_selector("form.js-form-analyze [type=submit]")
text_area.send_keys(website_url)
