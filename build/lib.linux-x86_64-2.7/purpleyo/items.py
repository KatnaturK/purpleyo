# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PurpleyoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    data_id = scrapy.Field()
    platform = scrapy.Field()
    city = scrapy.Field()
    listing_date = scrapy.Field()
    txn_type = scrapy.Field()
    property_type = scrapy.Field()
    status = scrapy.Field()
    lat = scrapy.Field()
    lng = scrapy.Field()
    locality = scrapy.Field()
    areacode = scrapy.Field()
    address = scrapy.Field()
    building_name = scrapy.Field()
    sqft = scrapy.Field()
    url	= scrapy.Field()
    desc = scrapy.Field()
    management_by_landlord = scrapy.Field()
    selling_price = scrapy.Field()
    rent = scrapy.Field()
