import grequests
import time

sites = ["https://public.naqa.gov.ua/api/v1/Accreditation/5154/Get" for _ in range(10)]

response = (grequests.get(url, verify=False) for url in sites)
#resp = grequests.map(response)

# requests_list = main()
start = time.time()

for i in grequests.map(response):
    print(i.json())
print(time.time() - start)
