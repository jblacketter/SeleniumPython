from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://revelar-qa-portal-practitioner.azurewebsites.net/login")

email_field = driver.find_element_by_id("login-email")
password_field = driver.find_element_by_id("login-password")

# enter search keyword and submit
email_field.send_keys("revbeme@dispostable.com")
password_field.send_keys("Welcome1@")

search_field.submit()

# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name method
lists= driver.find_elements_by_class_name("_Rm")

# get the number of elements found
print ("Found " + str(len(lists)) + " searches:")

# iterate through each element and print the text that is
# name of the search

i=0
for listitem in lists:
   print (listitem.get_attribute("innerHTML"))
   i=i+1
   if(i>10):
      break

# close the browser window
driver.quit()