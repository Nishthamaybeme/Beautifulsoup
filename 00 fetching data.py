import requests
def fetchAndSaveToFile(url, path):
    r=requests.get(url)
    with open(path,"w") as f:
        f.write(r.text)


url="https://timesofindia.indiatimes.com/city/agra"

fetchAndSaveToFile(url,"data/times.html")
# import requests
# from bs4 import BeautifulSoup

# proxies={
#      "http": "http://103.125.160.172.82",

# }

# url="https://www.amazon.in/s?k=samsung&crid=UTKDNSWQ5UA1&sprefix=samsung%2Caps%2C354&ref=nb_sb_noss_1"
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# r= requests.get(url,headers=headers)
# soup=BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify)
# # import requests
# from bs4 import BeautifulSoup

# proxies = {
#     "http": "http://103.101.24.77",
# }

# url = "https://www.amazon.in/s?k=samsung&crid=UTKDNSWQ5UA1&sprefix=samsung%2Caps%2C354&ref=nb_sb_noss_1"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
# }

# r = requests.get(url, headers=headers, proxies=proxies)
#   # Raise an exception for HTTP errors (4xx or 5xx)
# soup = BeautifulSoup(r.text, 'html.parser')
#     # print(soup.prettify())

 
# spans=soup.find(class_="a-size-medium")
# print(spans)
# # import requests
# # from bs4 import BeautifulSoup

# # proxies = {
# #     "http": "http://52.183.8.192:3128",
# # }

# # url = "https://www.amazon.in/s?k=samsung&crid=UTKDNSWQ5UA1&sprefix=samsung%2Caps%2C354&ref=nb_sb_noss_1"
# # headers = {
# #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
# # }

# # try:
# #     r = requests.get(url, headers=headers, proxies=proxies)
# #     r.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
    
# #     soup = BeautifulSoup(r.text, 'html.parser')
    
# #     # Find all elements with class "a-size-medium"
# #     spans = soup.select("div.puisg-col-inner")
    
# #     for span in spans:
# #         print(span.text.strip())  # Print the text content of each element
    
# # except requests.exceptions.RequestException as e:
# #     print("Error fetching page:", e)
# # import requests
# # from bs4 import BeautifulSoup

# # proxies = {
# #     "http": "http://52.183.8.192:3128",
# # }

# # url = "https://www.amazon.in/s?k=samsung&crid=UTKDNSWQ5UA1&sprefix=samsung%2Caps%2C354&ref=nb_sb_noss_1"
# # headers = {
# #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
# # }

# # try:
# #     r = requests.get(url, headers=headers, proxies=proxies)
# #     r.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
    
# #     soup = BeautifulSoup(r.text, 'html.parser')
    
# #     # Find all product containers
# #     products = soup.find_all('div', class_='s-result-item')
    
# #     for product in products:
# #         # Extract title
# #         title_element = product.find('span', class_='a-size-medium')
#         title = title_element.text.strip() if title_element else 'No Title Found'
        
#         # Extract price
#         price_element = product.find('span', class_='a-price')
#         price = price_element.find('span', class_='a-offscreen').text.strip() if price_element else 'Price Not Available'
        
# #         # Print title and price
# #         print(f"Title: {title}")
# #         print(f"Price: {price}")
# #         print("-" * 30)
    
# # except requests.exceptions.RequestException as e:
# #     print("Error fetching page:", e)
# # import requests
# # from bs4 import BeautifulSoup

# # proxies = {
# #     "http": "http://139.5.16.177",
# # }

# # url = "https://www.amazon.in/s?k=samsung&crid=UTKDNSWQ5UA1&sprefix=samsung%2Caps%2C354&ref=nb_sb_noss_1"
# # headers = {
# #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
# # }

# # try:
# #     r = requests.get(url, headers=headers, proxies=proxies)
# #     r.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
    
# #     soup = BeautifulSoup(r.text, 'html.parser')
    
# #     # Print the prettified HTML (for demonstration purposes)
# #     # print(soup.prettify())
# #     spans=soup.find(class_="a-size-medium")
# #     print(spans)

# # except requests.exceptions.RequestException as e:
# #     print("Error fetching page:", e)
# import requests
# from bs4 import BeautifulSoup

# proxies = {
#     "http": "http://139.5.16.177",
# }

# url = "https://www.amazon.in/s?k=samsung&crid=UTKDNSWQ5UA1&sprefix=samsung%2Caps%2C354&ref=nb_sb_noss_1"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
# }

# try:
#     r = requests.get(url, headers=headers, proxies=proxies)
#     r.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
    
#     soup = BeautifulSoup(r.text, 'html.parser')
    
#     # Find all product containers
#     products = soup.find_all('div', {'data-component-type': 's-search-result'})
    
#     for product in products:
#         # Extract title
#         title_element = product.find('span', class_='a-size-medium')
#         title = title_element.text.strip() if title_element else 'No Title Found'
        
#         # Extract price
#         price_element = product.find('span', class_='a-price')
#         price = price_element.find('span', class_='a-offscreen').text.strip() if price_element else 'Price Not Available'
        
#         # Print title and price
#         print(f"Title: {title}")
#         print(f"Price: {price}")
# #         print("-" * 30)
    
# # except requests.exceptions.RequestException as e:
# #     print("Error fetching page:", e)
# import requests
# from bs4 import BeautifulSoup

# proxies = {
#     "http": "http://139.5.16.177",
# }

# url = "https://www.amazon.in/s?k=samsung&crid=UTKDNSWQ5UA1&sprefix=samsung%2Caps%2C354&ref=nb_sb_noss_1"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
# }

# try:
#     r = requests.get(url, headers=headers, proxies=proxies)
#     r.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
    
#     soup = BeautifulSoup(r.text, 'html.parser')
    
#     # Find all product containers
#     products = soup.find_all('div', {'data-component-type': 's-search-result'})
    
#     for product in products:
#         # Extract title
# #         title_element = product.find('span', class_='a-size-base-plus a-color-base a-text-normal')
# #         title = title_element.text.strip() if title_element else 'No Title Found'
        
# #         # Print title
# #         print(f"Title: {title}")
# #         print("-" * 30)
    
# # except requests.exceptions.RequestException as e:
# #     print("Error fetching page:", e)
# import requests
# from bs4 import BeautifulSoup

# proxies = {
# #     "http": "http://139.5.16.177",
# # }

# # url = "https://www.amazon.in/s?k=samsung&crid=UTKDNSWQ5UA1&sprefix=samsung%2Caps%2C354&ref=nb_sb_noss_1"
# # headers = {
# #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
# # }

# # try:
# #     r = requests.get(url, headers=headers, proxies=proxies)
# #     r.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
    
# #     soup = BeautifulSoup(r.text, 'html.parser')
    
# #     # Find all product containers
# #     products = soup.find_all('div', class_='s-result-item')
    
# #     for product in products:
# #         # Extract title
# #         title_element = product.find('span', class_='a-size-medium')
# #         title = title_element.text.strip() if title_element else 'No Title Found'
        
# #         # Extract price
# #         price_element = product.find('span', class_='a-price')
# #         price = price_element.find('span', class_='a-offscreen').text.strip() if price_element else 'Price Not Available'
        
# #         # Print title and price
# #         print(f"Title: {title}")
# #         print(f"Price: {price}")
# #         print("-" * 30)
    
# # except requests.exceptions.RequestException as e:
# import requests
# import pandas as pd
# from bs4 import BeautifulSoup
# import time
# import random

# proxies = {
#     "http": "http://139.5.16.177",
# }

# # List of User-Agents for rotation
# user_agents = [
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
#     'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
#     # Add more User-Agents here
# ]

# data = {'Title': [], 'Price': []}
# url = "https://www.amazon.in/s?k=samsung&crid=UTKDNSWQ5UA1&sprefix=samsung%2Caps%2C354&ref=nb_sb_noss_1"

# max_retries = 5

# for attempt in range(max_retries):
#     headers = {
#         'User-Agent': random.choice(user_agents)
#     }

#     try:
#         r = requests.get(url, headers=headers, proxies=proxies)
#         r.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        
#         if r.status_code == 200:
#             break  # If successful, break out of the retry loop

#     except requests.exceptions.RequestException as e:
#         print(f"Attempt {attempt + 1}: Error fetching page:", e)
#         time.sleep(10)  # Wait for 10 seconds before retrying

# # Only parse the HTML if a successful request was made
# if r.status_code == 200:
#     soup = BeautifulSoup(r.text, 'html.parser')

#     # Find all product containers
#     products = soup.find_all('div', class_='s-result-item')

#     for product in products:
#         # Extract title
#         title_element = product.find('span', class_='a-size-medium')
#         title = title_element.text.strip() if title_element else 'No Title Found'
#         data["Title"].append(title)
        
#         # Extract price
#         price_element = product.find('span', class_='a-price')
#         if price_element:
#             price = price_element.find('span', class_='a-offscreen')
#             price = price.text.strip() if price else 'Price Not Available'
#         else:
#             price = 'Price Not Available'
#         data["Price"].append(price)
        
#         # Print title and price
#         print(f"Title: {title}")
#         print(f"Price: {price}")
#         print("-" * 30)
# else:
#     print(f"Failed to fetch the page after {max_retries} attempts.")

# # Create DataFrame from data dictionary
# df = pd.DataFrame(data)

# # Export DataFrame to CSV file
# df.to_csv("amazon_samsung_products.csv", index=False)
# import requests
# proxies = {
#      'https':'https://140.227.69.170:6000'


# }
# response=requests.get("https://ipinfo.io/json", proxies=proxies)
# print(response.json()['country'])