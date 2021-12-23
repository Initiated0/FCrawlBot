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
# print(soup.find_all('div', {'id':'d1'})[0].p.text)

data = soup.find_all('div', {'id':'d1'})[0].p.text

functions.write_to_file('./test.txt', data)

result = requests.get("https://google.com")
# print(result)
# print(result.text)


# main function -> requests
# make a http requests to the URL that you are interested -> beautifulsoup
# get specific text using BeautifulSoup library -> functions
# store the cleaned data -> functions
# read data and process em + delete em -> functions

# START FROM VIDEO 017 NEXT

def main_scraper(url, directory):
    functions.create_directory(directory)
    source_code = requests.get(url)
    print("Source code # ", source_code)
    source_text = source_code.text
    # print(source_text)

    # getting anchor tag
    soup = BeautifulSoup(source_text, "html.parser")
    # # this code took the first block of the featured course content
    # articles = soup.find_all('div', {'class':'course-block block featured_products'})

    # articles2 = soup.find_all('header', {'class':'header header-sticky'})
    
    # articles3 = soup.find_all('main', {'class':'view-school page-layout-v2 main'})

    # # the following code scrapes all the links inside first block of featured course content
    # articles4 = soup.find_all('div', {"class":"featured-product-card card-style-grid block__column b-79243210-card_background_color b-79243210-card_border_color b-79243210-card_border_width b-79243210-card_border_radius b-79243210-card_text_alignment"})

    # storing the data inside a .txt file
    articles5 = soup.find_all('div', {'class':'course-listing'})
    # this gives the headers from html
    articles6 = soup.find_all('div', {'class':'course-listing-title'}, {'role':'heading'})


    # # print(articles6)
    # print(articles6[0].text)
    i = 0

    for article in articles5:
        # print(article.div.get("title"))
        # print(article.a.get("href"))
        # print(article.a.text)
        primary_address = "https://calmandcode.teachable.com"
        # print(article.div.title)
        print("Title: " + articles6[i].text)
        print(" URL: " + primary_address + article.a.get("href"))
        article_formatted = "Title: " + articles6[i].text + "\nURL: " + primary_address + article.a.get("href") + "\n"
        i = i + 1
        if functions.does_file_exists(directory+"/articles.txt") is False:
            functions.create_new_file(directory+"/articles.txt")
        functions.write_to_file(directory+"/articles.txt", article_formatted)

    functions.read_data(directory+'/articles.txt')


main_scraper("https://calmandcode.teachable.com/courses", "Calmandcode")
