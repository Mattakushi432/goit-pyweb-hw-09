import json
from itemadapter import ItemAdapter
from .items import QuoteItem, AuthorItem


class ScraperPipeline:
    def __init__(self):
        self.quotes = []
        self.authors = []
        self.author_names = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if isinstance(item, QuoteItem):
            self.quotes.append(adapter.asdict())
        elif isinstance(item, AuthorItem):
            author_name = adapter.get('fullname')
            if author_name not in self.author_names:
                self.authors.append(adapter.asdict())
                self.author_names.add(author_name)
        return item

    def close_spider(self, spider):
        with open('quotes.json', 'w', encoding='utf-8') as f:
            json.dump(self.quotes, f, ensure_ascii=False, indent=2)

        with open('authors.json', 'w', encoding='utf-8') as f:
            json.dump(self.authors, f, ensure_ascii=False, indent=2)