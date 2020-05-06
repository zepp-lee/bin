# -*- coding: utf-8 -*-
import re

import geocoder
import scrapy

from achr.scrapy.items import TripAdvisorReviewItem


class TripAdvisorSpider(scrapy.Spider):
    name = 'tripadvisor'
    allowed_domains = ['tripadvisor.com']
    start_urls = ['http://tripadvisor.com/']

    def start_requests(self):
        yield scrapy.Request(f"https://www.tripadvisor.com/Hotels-{self.geo_id}", self.parse_hotels, meta={'start_request': True})

    def parse_hotels(self, response):
        for i, a in enumerate(response.css('a[id^=property_]::attr(href)').getall()):
            yield scrapy.Request(response.urljoin(a), self.parse_hotel, meta={'first_hotel_request': i == 0})
        if response.meta.get('start_request'):
            last_offset = int(response.css('a.pageNum:last-child::attr(data-offset)').get())
            for offset in range(30, last_offset + 1, 30):
                yield scrapy.Request(f"https://www.tripadvisor.com/Hotels-{self.geo_id}-oa{offset}", self.parse_hotels)

    def parse_hotel(self, response):
        for review in response.xpath('//div[@data-reviewid]/parent::*'):
            if hometown := review.css('[class*=hometown]::text').get():
                yield TripAdvisorReviewItem(
                    title=review.css('div[class*=reviewTitle] a span span::text').get().strip(),
                    text=' '.join(review.css('q[class*=reviewText] span::text').getall()).strip(),
                    country=geocoder.osm(hometown).country_code,    # TODO: Batch geocoding requests
                    source_url=response.url,
                )
        if response.meta.get('first_hotel_request'):
            if last_offset_url := response.css('a.pageNum:last-child::attr(href)').get():
                dest_id, last_offset = re.search("-(d\d+)-Reviews-or(\d+)", last_offset_url).groups()
                for offset in range(5, int(last_offset) + 1, 5):
                    yield scrapy.Request(f"https://www.tripadvisor.com/Hotel_Review-{self.geo_id}-d{dest_id}-or{offset}", self.parse_hotel)
