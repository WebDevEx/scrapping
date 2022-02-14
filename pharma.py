import requests
from bs4 import BeautifulSoup
import csv



nm_list = []
add_list = []

for p in range(221):
    print(p)
    url = "https://XXX/search-register/?type=0&page="+str(p)+"&search="

    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')
    ab = soup.find_all(class_='avatar-content')

    for i in ab:
        #print(soup.find("h5").text)
        #print(soup.find("small").text)
        nm_list.append(i.find("h5").text)
        add_list.append(i.find("small").text)


    #print(nm_list)
    #print(add_list)

with open('numbers.csv', 'w', newline='') as csvfile:
        fieldnames = ['col1', 'col2']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i, j in zip(nm_list, add_list):
            writer.writerow({'col1': i, 'col2': j})

print("All done!")    