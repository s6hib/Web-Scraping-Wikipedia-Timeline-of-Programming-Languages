import requests
from bs4 import BeautifulSoup
import pandas as pd

# Make a request to the website
url = "https://en.wikipedia.org/wiki/Timeline_of_programming_languages"
response = requests.get(url)

# Parse the whole HTML page using BeautifulSoup
soup = BeautifulSoup(response.text, 'lxml')

# Find the table in the HTML
table = soup.find('table', {'class': 'wikitable'})

# Find all rows in the table
rows = table.find_all('tr')

data = []
for row in rows[1:]:  # Skip the first row (header)
    cols = row.find_all('td')  # Find all columns in the row
    if len(cols) >= 2:  # Check if the row contains at least two columns
        year = cols[0].text.strip()
        language = cols[1].text.strip()
        data.append([year, language])  # Append the year and the language name to data

# Convert the data to DataFrame
df = pd.DataFrame(data, columns=['Year', 'Language'])

# Save the data to a CSV file
df.to_csv('programming_languages.csv', index=False)
