import requests
import pdfplumber
import pandas as pd

def download_file(url):
    local_filename = url.split('/'[-1])

    with requests.get(url) as r:
        with open(local_filename, 'wb') as f:
            f.write(r.content)

    return local_filename

ap_url = 'https://cmsweb.cms.csus.edu/psc/CSACPRD/view/%7bV2%7dr7Q4Yag29ArLGOdew0LI4eoTlA8I6hzwBaB0Cix2dWR0h8T07N0EJ51fmzuy7Sa2VucLG68p50CaubnZDLuMnD2YmNbtDrDZ79brHlksAMP1YOCiePcFOPPNdr_lxutt6ZGChyKN0Z3HKKDguNoeqc8Vzj0CM6eq07IOUHoAecIvCqaDvgGnbJAxlYGnrgXi/SSR_TSRPT.pdf'

ap = download_file(ap_url)

with pdfplumber.open(ap) as pdf:
    page = pdf.pages[15]
    text = page.extract_text()

print(text)
