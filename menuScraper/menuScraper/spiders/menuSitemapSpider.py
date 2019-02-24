from scrapy.spiders import SitemapSpider


class MySpider(SitemapSpider):
    name = "sitemapSpider"
    sitemap_urls = [
        "https://www.delish.com/robots.txt",
    ]

    def parse(self, response):
        # with open("image_data.txt", "a+") as f:
        for item in response.css("img"):
            # f.write(response.urljoin(url) + "\n")
            if item.css("::attr(src)").get() and item.css("::attr(alt)").get():
                yield {
                    'src': response.urljoin(item.css("::attr(src)").get()),
                    'page_title': response.css("title::text").get(),
                    'alt': response.urljoin(item.css("::attr(alt)").get())
                }
