import scrapy

from hospitalfollowup.items import HospitalfollowupItem


class FollowupSpider(scrapy.Spider):
    name = 'followup'
    allowed_domains = ['vhi.org']
    start_urls = ['http://www.vhi.org/Bon%20Secours%20DePaul%20Medical%20Center.html?tab=&?=h8084/']

    def parse(self, response):
        total_beds = response.xpath("//a[contains(@data-content,'Licensed beds')]/../../td[2]/text()").get()
        staffed_beds = response.xpath("//a[contains(@data-content,'deemed to be operational to receive patients')]/../../td[2]/text()").get()
        patient_days = response.xpath("//a[contains(@data-content,'Patient days')]/../../td[2]/text()").get()
        patient_days = patient_days.replace(",", "").replace(" ", "")

        item = HospitalfollowupItem()
        item["total_beds"] = int(total_beds)
        item["staffed_beds"] = int(staffed_beds)
        item["patient_days"] = int(patient_days)

        print(item["total_beds"], item["staffed_beds"], item["patient_days"])

        yield item
