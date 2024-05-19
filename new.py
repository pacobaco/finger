from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import sqlite3

# Set up the WebDriver
driver = webdriver.Chrome('/path/to/chromedriver')

# Define the URL
url = 'https://www.bop.gov/inmateloc/'

# Open the URL
driver.get(url)
time.sleep(2)

# Perform the search
first_name = driver.find_element(By.ID, 'inmNameFirst')
last_name = driver.find_element(By.ID, 'inmNameLast')

# Example search
first_name.send_keys('John')
last_name.send_keys('Doe')
last_name.send_keys(Keys.RETURN)
time.sleep(5)

# Parse the results
soup = BeautifulSoup(driver.page_source, 'html.parser')
inmate_rows = soup.select('selector-for-inmate-row')

# Connect to SQLite database
conn = sqlite3.connect('inmates.db')
cursor = conn.cursor()

# Extract and insert data
for row in inmate_rows:
    name = row.select_one('selector-for-name').text
    register_number = row.select_one('selector-for-register-number').text
    age = int(row.select_one('selector-for-age').text)
    race = row.select_one('selector-for-race').text
    sex = row.select_one('selector-for-sex').text
    release_date = row.select_one('selector-for-release-date').text
    location = row.select_one('selector-for-location').text

    # Insert data into the database
    cursor.execute('''
        INSERT INTO inmates (name, register_number, age, race, sex, release_date, location)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (name, register_number, age, race, sex, release_date, location))

# Commit changes and close the connection
conn.commit()
conn.close()

# Close the WebDriver
driver.quit()
