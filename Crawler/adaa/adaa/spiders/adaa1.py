# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from adaa.items import AdaaItem
from time import localtime, strftime
import uuid

class Adaa1Spider(CrawlSpider):
    name = 'adaa1'
    allowed_domains = ['adaa.org']
    start_urls = ['https://adaa.org/supportgroups#']

    rules = (
        Rule(LinkExtractor(allow=(),restrict_css=('.pager__item--next',)),
             callback="parse_item1",
             follow=True),)

    def parse_item1(self, response):
    	item_links = response.css('.views-field-title a::attr(href)').extract()
    	for a in item_links:
    		yield scrapy.Request(response.url+a, callback=self.parse_item)

    def parse_item(self, response):
    	item = AdaaItem()
        item["url"] = response.url
        item["doc_id"] = str(uuid.uuid1())
        item["raw_content"] = response.text
        item["timestamp_crawl"] = strftime("%Y-%m-%dT%H:%M:%SZ", localtime())
        yield item