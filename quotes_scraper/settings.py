BOT_NAME = "quotes_scraper"

SPIDER_MODULES = ["quotes_scraper.spiders"]
NEWSPIDER_MODULE = "quotes_scraper.spiders"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   "quotes_scraper.pipelines.ScraperPipeline": 300,
}

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'