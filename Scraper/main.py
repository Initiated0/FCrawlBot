from typing import Text
from bs4 import BeautifulSoup
import os
import functions
import requests

from flask import Flask, render_template

app = Flask(__name__)

html =  """

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

def main_scraper1(url, directory):
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


    # scraping images, grocery item list and info from "https://www.lazyfruits.com"

def main_scraper2(url, directory):
    i = 1
    # initial code
    functions.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")
    products = soup.find_all("div", {"class":"global-product-each"})
        
    # looping over products
    for product in products:
        image_tag = product.find('div', {'class':'global-product-img'})
        # print(image_tag.contents[3])
        # print('\n')
        image_code = image_tag.contents[3]
        s1 = BeautifulSoup(str(image_code),'html.parser')

        # image
        image_source = s1.a.find('img').get('src')
        print(image_source)
        
        # title
        image_title = s1.a.find('img').get('title')
        print("Image title : " + image_title)

        # name 
        name_tag = product.find('div', {'class':'global-product-name'})
        href = name_tag.find('a').get('href')
        name = name_tag.find('a').text
        print(name + '\n' + href)



        # price
        price_tag = product.find('div', {'class':'global-product-info-bottom-right'})
        price = price_tag.contents[1].text

        print("price : " + price)

        product_formatted = "Product #" + str(i) + ":\nName: " + name + "\nPrice: "+ str(price) + "\nImage: " + image_source + "\nhref: " + href + "\n\n"
        if functions.does_file_exists(directory+"/prodcut_inventory.txt") is False:
            functions.create_new_file(directory+"/prodcut_inventory.txt")
        functions.write_to_file(directory+"/prodcut_inventory.txt", product_formatted)
        i = i + 1

def main_scraper3(url, directory):
    # initial code
    functions.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")
    # till this point; it's always same
    # main modification starts below
    products = soup.find_all("div", {"class":"product"})

    for product in products:
        item = 1
        print('-----------------Product # ' + str(item) + '--------------')
        img_source = product.find('a').find('img').get('src')
        href = product.find('a').get('href')
        title = product.find('p').text
        price = product.find('p', {'class':'price'}).text

        print("Image: " + img_source)
        print("Title: " + title)
        print("href: " + href)
        print("price: " + price)

        item = item + 1

        print("-------------------------------------------------------")
        print("-------------------------------------------------------")

        

# main_scraper1("https://calmandcode.teachable.com/courses", "Calmandcode")

# main_scraper2("https://www.lazyfruits.com/","LazyFruits")

main_scraper3("https://www.thegreatcookie.com/","TheGreatCookie")