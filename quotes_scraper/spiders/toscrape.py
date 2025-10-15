import scrapy
from ..items import QuoteItem, AuthorItem


class ToScrapeSpider(scrapy.Spider):
    name = "toscrape"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        for quote_div in response.css("div.quote"):
            quote_item = QuoteItem()
            quote_item['tags'] = quote_div.css("div.tags a.tag::text").getall()
            quote_item['author'] = quote_div.css("small.author::text").get()
            quote_item['quote'] = quote_div.css("span.text::text").get().strip('“”')
            yield quote_item

            author_page_link = quote_div.css("small.author + a::attr(href)").get()
            if author_page_link:
                yield response.follow(author_page_link, self.parse_author)

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_author(self, response):
        author_item = AuthorItem()
        author_item['fullname'] = response.css("h3.author-title::text").get().strip()
        author_item['born_date'] = response.css("span.author-born-date::text").get()
        author_item['born_location'] = response.css("span.author-born-location::text").get()
        author_item['description'] = response.css("div.author-description::text").get().strip()
        yield author_item
