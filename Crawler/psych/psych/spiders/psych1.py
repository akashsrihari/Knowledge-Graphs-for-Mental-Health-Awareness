# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
from time import localtime, strftime
import uuid
from psych.items import PsychItem

class Psych1Spider(CrawlSpider):
    name = 'psych1'
    allowed_domains = ['www.psychologytoday.com']
    start_urls = ['https://www.psychologytoday.com/us/groups/alabama','https://www.psychologytoday.com/us/groups/alaska','https://www.psychologytoday.com/us/groups/arizona','https://www.psychologytoday.com/us/groups/arkansas','https://www.psychologytoday.com/us/groups/armed-forces-europe','https://www.psychologytoday.com/us/groups/california','https://www.psychologytoday.com/us/groups/colorado','https://www.psychologytoday.com/us/groups/connecticut','https://www.psychologytoday.com/us/groups/delaware','https://www.psychologytoday.com/us/groups/district-of-columbia','https://www.psychologytoday.com/us/groups/florida','https://www.psychologytoday.com/us/groups/georgia','https://www.psychologytoday.com/us/groups/guam','https://www.psychologytoday.com/us/groups/hawaii','https://www.psychologytoday.com/us/groups/idaho','https://www.psychologytoday.com/us/groups/illinois','https://www.psychologytoday.com/us/groups/indiana','https://www.psychologytoday.com/us/groups/iowa','https://www.psychologytoday.com/us/groups/kansas','https://www.psychologytoday.com/us/groups/kentucky','https://www.psychologytoday.com/us/groups/louisiana','https://www.psychologytoday.com/us/groups/maine','https://www.psychologytoday.com/us/groups/maryland','https://www.psychologytoday.com/us/groups/massachusetts','https://www.psychologytoday.com/us/groups/michigan','https://www.psychologytoday.com/us/groups/minnesota','https://www.psychologytoday.com/us/groups/mississippi','https://www.psychologytoday.com/us/groups/missouri','https://www.psychologytoday.com/us/groups/montana','https://www.psychologytoday.com/us/groups/nebraska','https://www.psychologytoday.com/us/groups/nevada','https://www.psychologytoday.com/us/groups/new-hampshire','https://www.psychologytoday.com/us/groups/new-jersey','https://www.psychologytoday.com/us/groups/new-mexico','https://www.psychologytoday.com/us/groups/new-york','https://www.psychologytoday.com/us/groups/north-carolina','https://www.psychologytoday.com/us/groups/north-dakota','https://www.psychologytoday.com/us/groups/ohio','https://www.psychologytoday.com/us/groups/oklahoma','https://www.psychologytoday.com/us/groups/oregon','https://www.psychologytoday.com/us/groups/pennsylvania','https://www.psychologytoday.com/us/groups/puerto-rico','https://www.psychologytoday.com/us/groups/rhode-island','https://www.psychologytoday.com/us/groups/south-carolina','https://www.psychologytoday.com/us/groups/south-dakota','https://www.psychologytoday.com/us/groups/tennessee','https://www.psychologytoday.com/us/groups/texas','https://www.psychologytoday.com/us/groups/utah','https://www.psychologytoday.com/us/groups/vermont','https://www.psychologytoday.com/us/groups/virgin-islands','https://www.psychologytoday.com/us/groups/virginia','https://www.psychologytoday.com/us/groups/washington','https://www.psychologytoday.com/us/groups/west-virginia','https://www.psychologytoday.com/us/groups/wisconsin','https://www.psychologytoday.com/us/groups/wyoming','https://www.psychologytoday.com/us/psychiatrists/alabama','https://www.psychologytoday.com/us/psychiatrists/alaska','https://www.psychologytoday.com/us/psychiatrists/arizona','https://www.psychologytoday.com/us/psychiatrists/arkansas','https://www.psychologytoday.com/us/psychiatrists/armed-forces-europe','https://www.psychologytoday.com/us/psychiatrists/california','https://www.psychologytoday.com/us/psychiatrists/colorado','https://www.psychologytoday.com/us/psychiatrists/connecticut','https://www.psychologytoday.com/us/psychiatrists/delaware','https://www.psychologytoday.com/us/psychiatrists/district-of-columbia','https://www.psychologytoday.com/us/psychiatrists/florida','https://www.psychologytoday.com/us/psychiatrists/georgia','https://www.psychologytoday.com/us/psychiatrists/guam','https://www.psychologytoday.com/us/psychiatrists/hawaii','https://www.psychologytoday.com/us/psychiatrists/idaho','https://www.psychologytoday.com/us/psychiatrists/illinois','https://www.psychologytoday.com/us/psychiatrists/indiana','https://www.psychologytoday.com/us/psychiatrists/iowa','https://www.psychologytoday.com/us/psychiatrists/kansas','https://www.psychologytoday.com/us/psychiatrists/kentucky','https://www.psychologytoday.com/us/psychiatrists/louisiana','https://www.psychologytoday.com/us/psychiatrists/maine','https://www.psychologytoday.com/us/psychiatrists/maryland','https://www.psychologytoday.com/us/psychiatrists/massachusetts','https://www.psychologytoday.com/us/psychiatrists/michigan','https://www.psychologytoday.com/us/psychiatrists/minnesota','https://www.psychologytoday.com/us/psychiatrists/mississippi','https://www.psychologytoday.com/us/psychiatrists/missouri','https://www.psychologytoday.com/us/psychiatrists/montana','https://www.psychologytoday.com/us/psychiatrists/nebraska','https://www.psychologytoday.com/us/psychiatrists/nevada','https://www.psychologytoday.com/us/psychiatrists/new-hampshire','https://www.psychologytoday.com/us/psychiatrists/new-jersey','https://www.psychologytoday.com/us/psychiatrists/new-mexico','https://www.psychologytoday.com/us/psychiatrists/new-york','https://www.psychologytoday.com/us/psychiatrists/north-carolina','https://www.psychologytoday.com/us/psychiatrists/north-dakota','https://www.psychologytoday.com/us/psychiatrists/ohio','https://www.psychologytoday.com/us/psychiatrists/oklahoma','https://www.psychologytoday.com/us/psychiatrists/oregon','https://www.psychologytoday.com/us/psychiatrists/pennsylvania','https://www.psychologytoday.com/us/psychiatrists/puerto-rico','https://www.psychologytoday.com/us/psychiatrists/rhode-island','https://www.psychologytoday.com/us/psychiatrists/south-carolina','https://www.psychologytoday.com/us/psychiatrists/south-dakota','https://www.psychologytoday.com/us/psychiatrists/tennessee','https://www.psychologytoday.com/us/psychiatrists/texas','https://www.psychologytoday.com/us/psychiatrists/utah','https://www.psychologytoday.com/us/psychiatrists/vermont','https://www.psychologytoday.com/us/psychiatrists/virgin-islands','https://www.psychologytoday.com/us/psychiatrists/virginia','https://www.psychologytoday.com/us/psychiatrists/washington','https://www.psychologytoday.com/us/psychiatrists/west-virginia','https://www.psychologytoday.com/us/psychiatrists/wisconsin','https://www.psychologytoday.com/us/psychiatrists/wyoming','https://www.psychologytoday.com/us/therapists/alabama','https://www.psychologytoday.com/us/therapists/alaska','https://www.psychologytoday.com/us/therapists/arizona','https://www.psychologytoday.com/us/therapists/arkansas','https://www.psychologytoday.com/us/therapists/armed-forces-europe','https://www.psychologytoday.com/us/therapists/california','https://www.psychologytoday.com/us/therapists/colorado','https://www.psychologytoday.com/us/therapists/connecticut','https://www.psychologytoday.com/us/therapists/delaware','https://www.psychologytoday.com/us/therapists/district-of-columbia','https://www.psychologytoday.com/us/therapists/florida','https://www.psychologytoday.com/us/therapists/georgia','https://www.psychologytoday.com/us/therapists/guam','https://www.psychologytoday.com/us/therapists/hawaii','https://www.psychologytoday.com/us/therapists/idaho','https://www.psychologytoday.com/us/therapists/illinois','https://www.psychologytoday.com/us/therapists/indiana','https://www.psychologytoday.com/us/therapists/iowa','https://www.psychologytoday.com/us/therapists/kansas','https://www.psychologytoday.com/us/therapists/kentucky','https://www.psychologytoday.com/us/therapists/louisiana','https://www.psychologytoday.com/us/therapists/maine','https://www.psychologytoday.com/us/therapists/maryland','https://www.psychologytoday.com/us/therapists/massachusetts','https://www.psychologytoday.com/us/therapists/michigan','https://www.psychologytoday.com/us/therapists/minnesota','https://www.psychologytoday.com/us/therapists/mississippi','https://www.psychologytoday.com/us/therapists/missouri','https://www.psychologytoday.com/us/therapists/montana','https://www.psychologytoday.com/us/therapists/nebraska','https://www.psychologytoday.com/us/therapists/nevada','https://www.psychologytoday.com/us/therapists/new-hampshire','https://www.psychologytoday.com/us/therapists/new-jersey','https://www.psychologytoday.com/us/therapists/new-mexico','https://www.psychologytoday.com/us/therapists/new-york','https://www.psychologytoday.com/us/therapists/north-carolina','https://www.psychologytoday.com/us/therapists/north-dakota','https://www.psychologytoday.com/us/therapists/ohio','https://www.psychologytoday.com/us/therapists/oklahoma','https://www.psychologytoday.com/us/therapists/oregon','https://www.psychologytoday.com/us/therapists/pennsylvania','https://www.psychologytoday.com/us/therapists/puerto-rico','https://www.psychologytoday.com/us/therapists/rhode-island','https://www.psychologytoday.com/us/therapists/south-carolina','https://www.psychologytoday.com/us/therapists/south-dakota','https://www.psychologytoday.com/us/therapists/tennessee','https://www.psychologytoday.com/us/therapists/texas','https://www.psychologytoday.com/us/therapists/utah','https://www.psychologytoday.com/us/therapists/vermont','https://www.psychologytoday.com/us/therapists/virgin-islands','https://www.psychologytoday.com/us/therapists/virginia','https://www.psychologytoday.com/us/therapists/washington','https://www.psychologytoday.com/us/therapists/west-virginia','https://www.psychologytoday.com/us/therapists/wisconsin','https://www.psychologytoday.com/us/therapists/wyoming','https://www.psychologytoday.com/us/treatment-rehab/alabama','https://www.psychologytoday.com/us/treatment-rehab/alaska','https://www.psychologytoday.com/us/treatment-rehab/arizona','https://www.psychologytoday.com/us/treatment-rehab/arkansas','https://www.psychologytoday.com/us/treatment-rehab/armed-forces-europe','https://www.psychologytoday.com/us/treatment-rehab/california','https://www.psychologytoday.com/us/treatment-rehab/colorado','https://www.psychologytoday.com/us/treatment-rehab/connecticut','https://www.psychologytoday.com/us/treatment-rehab/delaware','https://www.psychologytoday.com/us/treatment-rehab/district-of-columbia','https://www.psychologytoday.com/us/treatment-rehab/florida','https://www.psychologytoday.com/us/treatment-rehab/georgia','https://www.psychologytoday.com/us/treatment-rehab/guam','https://www.psychologytoday.com/us/treatment-rehab/hawaii','https://www.psychologytoday.com/us/treatment-rehab/idaho','https://www.psychologytoday.com/us/treatment-rehab/illinois','https://www.psychologytoday.com/us/treatment-rehab/indiana','https://www.psychologytoday.com/us/treatment-rehab/iowa','https://www.psychologytoday.com/us/treatment-rehab/kansas','https://www.psychologytoday.com/us/treatment-rehab/kentucky','https://www.psychologytoday.com/us/treatment-rehab/louisiana','https://www.psychologytoday.com/us/treatment-rehab/maine','https://www.psychologytoday.com/us/treatment-rehab/maryland','https://www.psychologytoday.com/us/treatment-rehab/massachusetts','https://www.psychologytoday.com/us/treatment-rehab/michigan','https://www.psychologytoday.com/us/treatment-rehab/minnesota','https://www.psychologytoday.com/us/treatment-rehab/mississippi','https://www.psychologytoday.com/us/treatment-rehab/missouri','https://www.psychologytoday.com/us/treatment-rehab/montana','https://www.psychologytoday.com/us/treatment-rehab/nebraska','https://www.psychologytoday.com/us/treatment-rehab/nevada','https://www.psychologytoday.com/us/treatment-rehab/new-hampshire','https://www.psychologytoday.com/us/treatment-rehab/new-jersey','https://www.psychologytoday.com/us/treatment-rehab/new-mexico','https://www.psychologytoday.com/us/treatment-rehab/new-york','https://www.psychologytoday.com/us/treatment-rehab/north-carolina','https://www.psychologytoday.com/us/treatment-rehab/north-dakota','https://www.psychologytoday.com/us/treatment-rehab/ohio','https://www.psychologytoday.com/us/treatment-rehab/oklahoma','https://www.psychologytoday.com/us/treatment-rehab/oregon','https://www.psychologytoday.com/us/treatment-rehab/pennsylvania','https://www.psychologytoday.com/us/treatment-rehab/puerto-rico','https://www.psychologytoday.com/us/treatment-rehab/rhode-island','https://www.psychologytoday.com/us/treatment-rehab/south-carolina','https://www.psychologytoday.com/us/treatment-rehab/south-dakota','https://www.psychologytoday.com/us/treatment-rehab/tennessee','https://www.psychologytoday.com/us/treatment-rehab/texas','https://www.psychologytoday.com/us/treatment-rehab/utah','https://www.psychologytoday.com/us/treatment-rehab/vermont','https://www.psychologytoday.com/us/treatment-rehab/virgin-islands','https://www.psychologytoday.com/us/treatment-rehab/virginia','https://www.psychologytoday.com/us/treatment-rehab/washington','https://www.psychologytoday.com/us/treatment-rehab/west-virginia','https://www.psychologytoday.com/us/treatment-rehab/wisconsin','https://www.psychologytoday.com/us/treatment-rehab/wyoming']

    rules = (
        Rule(LinkExtractor(allow=("https://www\.psychologytoday\.com/us/[groups|therapists|psychiatrists|treatment-rehab].*state=.*=ResultsName")),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
    	item = PsychItem()
        item["url"] = response.url
        item["doc_id"] = str(uuid.uuid1())
        item["raw_content"] = response.text
        item["timestamp_crawl"] = strftime("%Y-%m-%dT%H:%M:%SZ", localtime())
        yield item