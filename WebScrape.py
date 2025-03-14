# Extract All The Books Details

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd


def scrapeBook(book_url):
  book_page = requests.get(book_url).content
  book_soup = BeautifulSoup(book_page, "html.parser")
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
while book_count != 0:
  page_url = f"https://books.toscrape.com/catalogue/page-{i}.html"
  page_content = requests.get(page_url).content
  page_soup = BeautifulSoup(page_content, "html.parser")
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