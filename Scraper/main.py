from bs4 import BeautifulSoup
import os
import functions
import requests

html = """

            <div id="d1" class="wide">
                <p id="p1">Since the love that you left is all that I get
I want you to know that if I can't be close to you
I settle for the ghost of you
I miss you more than life (more than life)
                            </p>
                <img src=""/>
                <a id="a1"></a>
            </div>
            <div id="d2" class="small">
                <p id="p2">This memory is ecstacy</p>
                <img src=""/>
                <a id="a2"></a>
            </div>

            """


soup = BeautifulSoup(html,"html.parser")

# print(soup)
# print(soup.div.text)
# print(soup.p.text)
# print(soup.find_all('div'))  #fina all returns an array

# print(soup.find_all('div')[1])
# print(soup.find_all('p', {'id':'p4'}))
print(soup.find_all('div', {'id':'d1'})[0].p.text)

data = soup.find_all('div', {'id':'d1'})[0].p.text

functions.write_to_file('./test.txt', data)

result = requests.get("https://google.com")
print(result)
print(result.text)


# main function -> requests
# make a http requests to the URL that you are interested -> beautifulsoup
# get specific text using BeautifulSoup library -> functions
# store the cleaned data -> functions
# read data and process em + delete em -> functions

# START FROM VIDEO 017 NEXT