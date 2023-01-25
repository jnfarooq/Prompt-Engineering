from bs4 import BeautifulSoup
import json

# open local index.html file
with open("index.html", "r") as file:
    soup = BeautifulSoup(file, "html.parser")

# find all div with class="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16"
items = soup.find_all("div", {"class": "sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16"})

# create an empty list to store the data
data = []

# for each div from the above list
for item in items:
    try:
        # find img with class="s-image" then link=img.src
        link = item.find("img", {"class": "s-image"})["src"]
    except:
        # except link=''
        link = ''

    try:
        # find span with class="a-size-medium a-color-base a-text-normal" then title=span.text
        title = item.find("span", {"class": "a-size-medium a-color-base a-text-normal"}).text
    except:
        # except title=''
        title = ''

    try:
        # find span with class="a-icon-alt" then rating=span.text
        rating = item.find("span", {"class": "a-icon-alt"}).text
    except:
        # except rating=''
        rating = ''

    try:
        # find span with class="a-price-whole" then price=span.text
        price = item.find("span", {"class": "a-price-whole"}).text
    except:
        # except price=''
        price = ''

    # append the link, title, rating and price into the data list
    data.append({"link": link, "title": title, "rating": rating, "price": price})

# dump the data into a data.json file
with open("data.json", "w") as json_file:
    json.dump(data, json_file)
