import requests
from bs4 import BeautifulSoup

def scrape_population(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        country_elements = soup.find_all('div', class_='country-name')
        population_elements = soup.find_all('div', class_='population-size')
        countries = [country.text.strip() for country in country_elements]
        populations = [population.text.strip() for population in population_elements]

        result = dict(zip(countries, populations))

        return result
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None

url_to_scrape = 'https://www.scrapethissite.com/pages/simple/'
scraped_data = scrape_population(url_to_scrape)

if scraped_data:
    for country, population in scraped_data.items():
        print(f"Country: {country}, Population: {population}")
           