# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TripAdvisorReviewItem(scrapy.Item):
    title = scrapy.Field()
    text = scrapy.Field()
    rating = scrapy.Field()
    country = scrapy.Field()
    source_url = scrapy.Field()
