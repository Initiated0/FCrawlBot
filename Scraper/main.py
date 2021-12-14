from bs4 import BeautifulSoup
import os

html = "<div>This is a div </div> <p>This is a parargraph tag</p>"


soup = BeautifulSoup(html,"html.parser")

print(soup)
print(soup.div.text)
print(soup.p.text)
