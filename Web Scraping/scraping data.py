from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, features="html.parser")

# print(soup)
# print(soup.find_all('table')[1])

# print(soup.find('table', class_ = 'wikitable sortable'))

table = soup.find_all('table')[0]
# print(table)


world_titles = table.find_all('th')
# print(world_titles)

world_table_titles = [title.text.strip() for title in world_titles]
# print(world_table_titles)

import pandas as pd
df = pd.DataFrame(columns = world_table_titles)

# print(df)


column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    # print(individual_row_data)

    length = len(df)
    df.loc[length] = individual_row_data
    print(df)

    df.to_csv(r'D:/DATA ANALYSIS/PYTHON/Web scraping project/Companies.csv', index = False)


