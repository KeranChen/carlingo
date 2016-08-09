import scrapy

from carlingo.items import CarlingoItem

class carSpider(scrapy.Spider):
    name = "carlingo"
    allowed_domains = ["craigslist.org"]
    start_urls = [
        # just include one page in the current crawler
        "https://chicago.craigslist.org/sox/cto/5705630700.html",
    ]

    def parse(self, response):
        # initialize item
        item = CarlingoItem()
        sel = response.xpath('//span[@class="screen-reader-text"]')
        item['title'] = sel.xpath('//span[@id="titletextonly"]/text()').extract_first()
        item['location'] = sel.xpath('//small/text()').extract_first()
        item['price'] = sel.xpath('//span[@class="price"]/text()').extract_first()
            
        main = response.xpath('//section[@class = "userbody"]')
        item['post'] = main.xpath('//section[contains(@id,"postingbody")]/text()').extract()
        item['notice'] = main.xpath('//ul[@class="notices"]//li/text()').extract()
        item['time'] = main.xpath('//time[@class="timeago"]/@datetime').extract()

        for attr in main.xpath('//p[@class="attrgroup"]//span'):
            if attr.xpath("/text()").extract() == "":
                item['model']=attr.xpath("//b/text()").extract() 
            else:
                # not successfully run
                # item[attr.xpath("/text()").extract()] = attr.xpath("//b/text()").extract() 
                pass
        yield item
        #     