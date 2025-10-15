import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from quotes_scraper.spiders.toscrape import ToScrapeSpider

if __name__ == '__main__':
    settings = get_project_settings()

    process = CrawlerProcess(settings)

    process.crawl(ToScrapeSpider)

    process.start()

    print("\n[+] Скрапинг завершен. Файлы quotes.json и authors.json созданы.")
