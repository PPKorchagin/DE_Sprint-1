import json
from datetime import time
from time import sleep

import requests
from bs4 import BeautifulSoup

URL = "https://spb.hh.ru/search/vacancy?text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&from=suggest_post&page="


pagenum=0
httpc=200

HEADERS = {
    # "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

while True:
    print("processing page %d"%pagenum)
    resp = requests.get(URL+str(pagenum), headers=HEADERS)

    if resp.status_code != 200:
        print("error: ", resp.status_code)
        break

    soup = BeautifulSoup(resp.text, "html.parser")

    # print(soup.prettify())

    items = soup.find_all("div", class_="vacancy-serp-item__layout")

    data = []

    for item in items:
        title_tag = item.find("a", class_="serp-item__title")
        url = title_tag['href']
        title = title_tag.text
        city = item.find("div", {"data-qa": "vacancy-serp__vacancy-address"}).text
        salary_tag = item.find("span", {"data-qa": "vacancy-serp__vacancy-compensation"})
        if salary_tag != None:
            salary = salary_tag.text
        else:
            salary = "Salary unknown"

        page = requests.get(url, headers=HEADERS)
        if page.status_code != 200:
            experience = "?"
        else:
            page_soup = BeautifulSoup(page.text, "html.parser")
            experience = page_soup.find("span", {"data-qa": "vacancy-experience"}).text

        item = {
            "title": title,
            "work experience": experience,
            "salary": salary,
            "region": city
        }
        data.append(item)
        # print(f"{title} {city} {salary} {experience}")

        sleep(3)
        pagenum+=1

with open("res.json", "w") as rf:
    print(data)
    str = json.dumps(data, indent=4)
    rf.write(str)
