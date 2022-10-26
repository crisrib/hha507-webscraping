# Import packages
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Get bloomberg page
original = requests.get('https://top10.netflix.com/tv')
original
original.text

# Create BeautifulSoup object 
soup = BeautifulSoup(original.text,'html.parser')
print(soup.prettify())

netflixTop = soup.find_all('tr')

output_top = []
for i in netflixTop : # for x in y
    print (i.text)
    output_top.append(i.text)

list1 = netflixTop
len(output_top)

# Create dictionary
dictionary = {'neflixTop': list1}

# Save dataframe to csv
df = pd.DataFrame(list1)
df.to_csv('netflix.csv')