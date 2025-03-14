# -*- coding: utf-8 -*-
"""Day 8 - 4th December 2024.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p8TLhG8VMrGqyxOHQND-TdewsHxkT_-G

**Web Scraping**

**Basics Of HTML/CSS**

**Request**

**Beautiful Soup**

1. find()
2. find_all()
3. select()
4. select_one()
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

print("Lets Discuss!!")
base_url = "http://books.toscrape.com/index.html"
home_page = requests.get(base_url)
#print(home_page.content)

if home_page.status_code == 200:
    print("Success")
else:
    print(f"Failed: Status Code - {home_page.status_code}")

soup = BeautifulSoup(markup = home_page.content, parser = "html.parser")
books = soup.find_all(name = "li", class_ = "col-xs-6 col-sm-4 col-md-3 col-lg-3")
print(len(books))
#print(books)
books1 = books[0]
b1 = books1.find(name = "a").get("href")
print(b1)
book_url = urljoin(base_url, b1)
print(book_url)

book1_page = requests.get(book_url)
book_info = book1_page.content
#print(book_info)

soup = BeautifulSoup(markup = book_info, parser = "html.parser")
book_title = soup.find(name = "h1")
print(f"Book Name: {book_title.text}")
book_table = soup.find_all(name = "tr")
book_data = {}
for row in book_table:
  key = row.find(name = "th").text
  value = row.find(name = "td").text
  book_data[key] = value
#print(book_data)
print(f"Price: {book_data['Price (incl. tax)']}")
print(f"Availability: {book_data['Availability']}")

# Extract All The Books Details

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd


def scrapeBook(book_url):
  book_page = requests.get(book_url).content
  book_soup = BeautifulSoup(markup = book_page, parser = "html.parser")
  book_title = book_soup.find(name = "h1").text
  book_data = {}
  book_data["Title"] = book_title
  book_table = book_soup.find_all(name = "tr")
  for row in book_table:
    key = row.find(name = "th").text
    value = row.find(name = "td").text
    book_data[key] = value
  return book_data

count = 0
base_url = "http://books.toscrape.com/index.html"
i = 1
book_count = 1
books_data = []
while book_count != 20:
  page_url = f"https://books.toscrape.com/catalogue/page-{i}.html"
  page_content = requests.get(page_url).content
  page_soup = BeautifulSoup(markup = page_content, parser = "html.parser")
  page_books = page_soup.find_all(name = "li", class_ = "col-xs-6 col-sm-4 col-md-3 col-lg-3")
  book_count = len(page_books)
  #print(page_books)
  for books in page_books:
    book_url = books.findChild(name = "a").get("href")
    book_url = urljoin(base_url, "/catalogue/" + book_url)
    book_data = scrapeBook(book_url)
    books_data.append(book_data)
  count += len(page_books)
  i += 1
print(f"Total Number Of Books: {count}")

df = pd.DataFrame(books_data)
# Save the DataFrame to an Excel file
df.to_excel('Books Details.xlsx', index=False)
print("Data has been written to 'Books Details.xlsx'")

print(books_data)

from bs4 import BeautifulSoup

# HTML
html_snippet = """
<div>
  <p>Hello, <b>World!</b></p>
  <p>Welcome to <a href="https://example.com">Example</a>.</p>
</div>
"""

soup = BeautifulSoup(html_snippet, 'html.parser')

extracted_text = soup.find(name="div").getText()

print(extracted_text)

html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>News Portal</title>
</head>
<body>
    <div id="main-content">
        <p>Paragraph 1 in main content.</p>
        <p>Paragraph 2 in main content.</p>
    </div>
    <div id="sidebar">
        <p>Paragraph in sidebar.</p>
    </div>
    <div>
        <p>Paragraph in a div without an ID.</p>
    </div>
</body>
</html>
"""
soup = BeautifulSoup(html_code, 'html.parser')
res = soup.find('div', id='main-content').find_all('p')
print(res)

from bs4 import BeautifulSoup

html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Product Data</title>
</head>
<body>
    <table>
        <thead>
            <tr>
                <th>Product Name</th>
                <th>Price</th>
                <th>Category</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Laptop</td>
                <td>999</td>
                <td>Electronics</td>
            </tr>
            <tr>
                <td>Smartwatch</td>
                <td>250</td>
                <td>Wearables</td>
            </tr>
            <tr>
                <td>Novel</td>
                <td>15.99</td>
                <td>Books</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
"""
def scrape_table(html_content):
  # write your code here
  soup = BeautifulSoup(markup = html_content, parser = "html.parser")
  product_data = soup.find_all(name = "tr")
  print(product_data)
  p_data = []
  for i in range(len(product_data)):
    if i == 0:
      tag = "th"
    else:
      tag = "td"
    row = product_data[i].find_all(name = tag)
    data = []
    for j in row:
      data.append(j.text)
    p_data.append(data)
  return p_data

res = scrape_table(html_code)
print(res)

print("File End!!")