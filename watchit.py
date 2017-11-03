import scrapy
import re
import sys

class WatchSeries(scrapy.Spider):
    name = 'watchseries'
    series = 'the_series'
    season = '1'
    episode = '1'
    start_urls = ['http://ewatchseries.to/episode/'+ series +'_' + 's' + season + '_e' + episode + '.html']

    def parse(self, response):
        for title in response.xpath("//a[contains(@onclick, '.me/')]").extract():
            yield {'url': re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|(?:%[0-9a-fA-F][0-9a-fA-F]))[^\']+", title)[0]}

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)
