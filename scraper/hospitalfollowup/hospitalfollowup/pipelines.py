# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

import requests
import json


class HospitalfollowupPipeline:
    def process_item(self, item, spider):
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)

        w = session.put("http://django:8000/partial-update-civilian-hospital/", {
            "patient_capacity": item["patient_days"],
            "total_beds_for_patient_holding": item["total_beds"],
            "total_beds_occupied": item["staffed_beds"],
            "free_beds": item["total_beds"] - item["staffed_beds"]
        }, timeout=60)
        print("Status code: ", w.status_code, w.text)

        return item
