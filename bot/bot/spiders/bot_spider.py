import scrapy 

class BotSpider(scrapy.Spider):
    name = "posts"

    start_urls = [
        # 'https://blog.scrapinghub.com/page/1/',
        # 'https://blog.scrapinghub.com/page/2/ 
        # 'https://www.zyte.com/blog/page/2'
        # 'https://www.samsung.com/us/'
        'https://www.facebook.com/'
        # 'https://www.bengalsaroma.com/category/blog/'
        # 'https://www.bengalsaroma.com/category/blog/page/2/'
        # 'https://www.bengalsaroma.com/category/blog/page/3/'      
      
    ]
    def parse(self, response):
        page = response.url.split('/')[-1]
        filename = 'posts-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
            # run this with scrapy shell https://www.banglasaroma.com/category/blog/


    # def parse(self, response):
    #     for post in response.css('div.post-item'):
    #         yield{
    #             'title' : post.css('.entry-header h2 a::text')[0].get()
    #             'date' : post.css('.post-header a::text')[1].get(),
    #             'author' : post.css('.post-header a::text')[2].get(),
    #         }
    #     next_page = response.css('a.next-posts-link::attr(href').get()
    #     if next_page is not None:
    #         next_page = response.urljoin(next_page)
    #         yield scrapy.Request(next_page, callback-self.parse)
    #         # run scrapy crawl posts -o posts.json
        