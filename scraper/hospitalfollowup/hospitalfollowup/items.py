# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HospitalfollowupItem(scrapy.Item):
    staffed_beds = scrapy.Field()  # ok
    total_beds = scrapy.Field()  # ok
    patient_days = scrapy.Field()  # ok

