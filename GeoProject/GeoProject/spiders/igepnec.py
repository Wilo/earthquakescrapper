from scrapy import Spider
from scrapy.selector import Selector
from GeoProject.items import IgepnItem

class IgepnSpider(Spider):
    name = "igepnSpider"
    allowed_domains = ["eventos.igepn.edu.ec"]
    start_urls = (
        'http://eventos.igepn.edu.ec/eqevents/events.xml',
    )

    def parse(self, response):
        selector = Selector(response)
        site = selector.xpath('//markers/marker')
        items = []
        # print site
        #return items

        for feed in site:
            ignepn =  IgepnItem()
            ignepn['Latitud'] = feed.xpath('@lat').extract()
            ignepn['Longitud'] = feed.xpath('@lng').extract()
            ignepn['Magnitud'] = feed.xpath('@mg').extract()
            ignepn['Localizacion'] = feed.xpath("@localizacion").extract()
            ignepn['Fecha'] = feed.xpath('@fecha').extract()
            ignepn['Z'] = feed.xpath('@z').extract()
            items.append(ignepn)
            # print ignepn
            print items
