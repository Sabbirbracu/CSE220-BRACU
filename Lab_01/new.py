import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the hospital page
url = 'https://www.german-hospital-directory.com/app/portrait/f8c539c20e2f4f26/start'

# Send a GET request to the hospital page
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the desired data fields from the hospital page
name = soup.find('h1').text.strip()

address_elements = soup.find_all('div', class_='address-element')
if len(address_elements) >= 2:
    street = address_elements[0].text.strip()
    postcode_town = address_elements[1].text.strip()
else:
    street = ""
    postcode_town = ""

phone_element = soup.find('span', itemprop='telephone')
phone = phone_element.text.strip() if phone_element else ""

fax_element = soup.find('span', itemprop='faxNumber')
fax = fax_element.text.strip() if fax_element else ""

email_element = soup.find('span', itemprop='email')
email = email_element.text.strip() if email_element else ""

website_element = soup.find('a', itemprop='url')
website = website_element['href'] if website_element else ""

# Create a list to hold the extracted data
data = [
    ['Name', 'Street', 'Postcode / Town', 'Phone', 'Fax', 'Email', 'Website'],
    [name, street, postcode_town, phone, fax, email, website]
]

# Specify the output CSV file path
csv_file_path = 'hospital_data.csv'

# Save the data as CSV
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)

print('Data has been saved to', csv_file_path)
