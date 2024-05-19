from bs4 import BeautifulSoup

# Assuming driver.page_source contains the HTML of the results page
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Define the selectors based on the actual HTML structure
inmate_rows = soup.select('selector-for-inmate-row')

for row in inmate_rows:
    name = row.select_one('selector-for-name').text
    register_number = row.select_one('selector-for-register-number').text
    age = row.select_one('selector-for-age').text
    race = row.select_one('selector-for-race').text
    sex = row.select_one('selector-for-sex').text
    release_date = row.select_one('selector-for-release-date').text
    location = row.select_one('selector-for-location').text

    print(f"Name: {name}")
    print(f"Register Number: {register_number}")
    print(f"Age: {age}")
    print(f"Race: {race}")
    print(f"Sex: {sex}")
    print(f"Release Date: {release_date}")
    print(f"Location: {location}")
    print("\n")  # Add a newline for readability between records
