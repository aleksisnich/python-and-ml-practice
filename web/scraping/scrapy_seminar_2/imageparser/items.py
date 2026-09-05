# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Compose

def process_name(value):
    value = value[0].strip()
    return value

def process_price(value):
    value = value[0].strip().replace('\xa0', ' ').split()

    if value[0].isdigit():
        value[0] = int(value[0])
    if value[1].isdigit():
        value[1] = int(value[1])
    return value

def process_photo(value:str):
    print()
    if value.startswith("//"):
        value = 'https:' + value.split()[0]
    else:
        value = value.split()[1]
    return value

class ImageparserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor=Compose(process_name), output_processor=TakeFirst())
    price = scrapy.Field(input_processor=Compose(process_price))
    url = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field(input_processor=MapCompose(process_photo))
    _id = scrapy.Field()
