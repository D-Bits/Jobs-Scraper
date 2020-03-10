from scrapy import Spider, Request


# Create a spider for Indeed jobs
class IndeedSpider(Spider):

    name = "indeed"

    start_urls = [
        "https://www.indeed.com/jobs?q=python&l=Seattle%2C+WA",
    ]

    def parse(self, response):

        page = response.url.split("/")[-2]
        filename = "indeed.html" 

        with open(filename, 'wb') as file:

            file.write(response.body)

        self.log("Saved file %s" % filename)