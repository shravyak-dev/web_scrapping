import requests
import pandas as pd
from bs4 import BeautifulSoup

response = requests.get("https://www.flipkart.com/search?q=mi%20mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

# print(response)

soup = BeautifulSoup(response.content,'html.parser')
# print(soup)

names = soup.find_all('div',class_ ='RG5Slk')
# print(names)
name = []
for i in names[0:10]:
    d = i.get_text()
    name.append(d)
# print(name)


prices = soup.find_all('div',class_ = 'hZ3P6w DeU9vF')
# print(prices)
price = []
for i in prices[0:10]:
    d = i.get_text()
    price.append(d)
# print(price)

ratings = soup.find_all('div',class_ = 'MKiFS6')
# print(ratings)
rate = []
for i in ratings[0:10]:
    d = i.get_text()
    rate.append(float(d))
# print(rate)


images = soup.find_all('img',class_ = 'UCc1lI')
# print(images)
image = []
for i in images[0:10]:
    d = i['src']
    image.append(d)
# print(image)


df = pd.DataFrame()
# print(df)
df["Names"] = name
df["Prices"] = price
df["Ratings"] = rate
df["Images"] = image
print(df)
df.to_csv("Mobilesjan.csv")

# sam = {}
# sam['user'] = 1234
# print(sam)