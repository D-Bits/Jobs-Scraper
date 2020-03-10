from scrapy import Spider, Request


# Create a spider for Indeed jobs
class IndeedSpider(Spider):

    name = "craigslist"

    start_urls = [
        "https://seattle.craigslist.org/search/jjj?query=python",
    ]

    # FIXME: Fix so it only scrapes certain elements
    def parse(self, response):

        page = response.url.split("/")[-2]
        filename = "craigslist.html" 

        with open(filename, 'wb') as file:

            file.write(response.body)

        self.log("Saved file %s" % filename)