import urllib.request, json 
from yahoo_finance import Share


with urllib.request.urlopen("https://query2.finance.yahoo.com/v10/finance/quoteSummary/{}?modules=assetProfile".format("NVDA")) as url:
	data = json.loads(url.read().decode())
	jsondata = data["quoteSummary"]["result"]
	for item in data
		print(item)
