from __future__ import absolute_import, unicode_literals

from celery import shared_task

from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

import requests


@shared_task
def run_hospital_scraping():
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    w = session.get("http://self_internal_worker_1:6543/followup/", timeout=60)
    return w.status_code
