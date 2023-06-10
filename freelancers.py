import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest


freelancer_name = []
freelancer_price = []
freelancer_country = []
page = 1

while True:
    
    URL = requests.get(f"https://www.freelancer.com/freelancers/skills/web-development/{page}")
    src = URL.content

    soup = BeautifulSoup(src, "lxml")

    name = soup.find_all("a",{"class":"find-freelancer-username"})
    price = soup.find_all("span", {"class":"user-hourly-rate freelancer-hourlyrate"})
    country = soup.find_all("img",{"class":"flag-icon"})


    for i in range(len(name)):
        freelancer_name.append(name[i].text.strip().replace("\n",""))
        freelancer_price.append(price[i].text)
        freelancer_country.append(country[i].attrs['alt'])
    print(f"{page}-Finished")
    page += 1
    if page > 3:
        break
    
        

system = [freelancer_name, freelancer_price, freelancer_country]
ex = zip_longest(*system)

with open("/Users/mark maher/Documents/freelancer_WebDevlopment.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(["Name", "Rate Hour", "Country"])
    wr.writerows(ex)



