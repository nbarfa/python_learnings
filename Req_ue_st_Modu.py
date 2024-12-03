import requests
r = requests.get("https://site.financialmodelingprep.com/")
print(r.text)
print(r.status_code)