import scrapy
import re
import sys

class WatchSeries(scrapy.Spider):
    name = 'watchseries'

    def __init__(self, *args, **kwargs):
        series = kwargs.pop('series', []) 
        season = kwargs.pop('season', []) 
        episode = kwargs.pop('episode', []) 
        self.season = season
        self.episode = episode
        self.start_urls = ['http://ewatchseries.to/episode/'+ series +'_' + 's' + season + '_e' + episode + '.html']
        self.logger.info(self.start_urls)
        super(WatchSeries, self).__init__(*args, **kwargs)

    def parse(self, response):
        for title in response.xpath("//a[contains(@onclick, '.me/')]").extract():
            yield {'url': re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|(?:%[0-9a-fA-F][0-9a-fA-F]))[^\']+", title)[0]}

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)
