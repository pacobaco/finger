from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (ensure you have the correct path to your WebDriver)
driver = webdriver.Chrome('/path/to/chromedriver')

# Define the URL
url = 'https://www.bop.gov/inmateloc/'

# Open the URL
driver.get(url)

# Give the page some time to load
time.sleep(2)

# Find the search input elements and perform the search
first_name = driver.find_element(By.ID, 'inmNameFirst')
last_name = driver.find_element(By.ID, 'inmNameLast')

# Example search (modify as needed)
first_name.send_keys('John')
last_name.send_keys('Doe')

# Submit the search form
last_name.send_keys(Keys.RETURN)

# Wait for results to load
time.sleep(5)

# Extract results (customize based on actual page structure)
results = driver.find_elements(By.CSS_SELECTOR, 'selector-for-results')

# Print results (or save them as needed)
for result in results:
    print(result.text)

# Close the WebDriver
driver.quit()
