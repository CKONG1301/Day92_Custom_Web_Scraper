import requests
from bs4 import BeautifulSoup
import csv


# Get the dish name. Replace space with '+'.
dish = input('Enter the dish name: ').upper().replace(' ', '+')
URL = 'https://www.allrecipes.com/search/results/'
query = {
    "search": f"{dish}"
    }
# Request from allrecipes site.
response = requests.get(url=URL, params=query)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')
# Get name of recipe.
names_list =[]
all_names = soup.select(".card__detailsContainer h3")
for item in all_links:
    name = item.text.replace('\n', '').strip(' ')
    names_list.append(name)
# Get link of recipe.
link_list = []
all_links = soup.select(".card__detailsContainer a")
for item in all_links:
    link = item['href']
    if 'http' not in link:
        link = f"https://{link}"
    link_list.append(link)
# Save name and link to csv file.
with open('recipe.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Dish', 'Url'])
    for n in range(len(names_list)):
        csvwriter.writerow([names_list[n], link_list[n]])
        