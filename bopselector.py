from bs4 import BeautifulSoup

# Assuming `page_source` contains the HTML of the results page
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Extract information
inmates = soup.select('selector-for-inmate-info')
for inmate in inmates:
    name = inmate.select_one('selector-for-name').text
    id = inmate.select_one('selector-for-id').text
    print(f'Name: {name}, ID: {id}')
