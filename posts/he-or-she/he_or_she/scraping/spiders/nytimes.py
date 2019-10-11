# -*- coding: utf-8 -*-
import json
import os
import scrapy

from he_or_she.scraping.items import ArticleItem


class NYTimesSpider(scrapy.Spider):
    name = 'nytimes'
    allowed_domains = ['nytimes.com']
    start_urls = ['http://nytimes.com/']
    api_url = 'https://www.nytimes.com/svc/collections/v1/publish/'

    def start_requests(self):
        nytimes_authors_path = os.path.join(os.path.dirname(__file__), 'nytimes_authors.json')
        with open(nytimes_authors_path) as nytimes_authors_fp:
            nytimes_authors = json.load(nytimes_authors_fp)
            for author in nytimes_authors:
                if author['gender'] != 'unclear':
                    query_url = f"{author['url']}?sort=newest&page=0"
                    yield scrapy.Request(f"{self.api_url}{query_url}", meta={'author': author})

    def parse(self, response):
        response_json = json.loads(response.body_as_unicode())
        for page in range(response_json['members']['total_pages']):
            query_url = f"{response.meta['author']['url']}?sort=newest&page={page}"
            yield scrapy.Request(f"{self.api_url}{query_url}", self.parse_article_list, meta=response.meta)

    def parse_article_list(self, response):
        response_json = json.loads(response.body_as_unicode())
        for item in response_json['members']['items']:
            if len(item['authors']) == 1:
                yield ArticleItem(
                    headline=item['headline'],
                    summary=item['summary'],
                    author_gender=response.meta['author']['gender'],
                )

