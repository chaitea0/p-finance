import urllib.request, json 
from yahoo_finance import Share

stock = ['ticker', 0, 0, 0] #ticker, ROC, E/P, ranking
list_data = []

file1 = 'nasdaqlisted.txt'
file2 = 'data.txt'
stream1 = open(file1, 'r')
stream2 = open("data.txt", "w")
list1 = stream1.readlines()
'''
with urllib.request.urlopen("https://query2.finance.yahoo.com/v10/finance/quoteSummary/{}?modules=financialData".format("NVDA")) as url:
    data = json.loads(url.read().decode())
    jsondata = data["quoteSummary"]["result"]
    print(jsondata[0].get("financialData").get("returnOnEquity").get("raw"))
'''

#https://stackoverflow.com/questions/38567661/how-to-get-key-statistics-for-yahoo-finance-web-search-api
#https://stackoverflow.com/questions/16675849/python-parsing-json-data-set

for line in list1: #add all tickers from nasdaq listed
	ticker = line.split('|', 1)[0] # add only first word
	try:
		with urllib.request.urlopen("https://query2.finance.yahoo.com/v10/finance/quoteSummary/{}?modules=financialData".format(ticker)) as url:
			data = json.loads(url.read().decode())
			jsondata = data["quoteSummary"]["result"]
		stream2.write(ticker + "\n")
		stream2.write(str(jsondata[0].get("financialData").get("returnOnEquity").get("raw")) + "\n")
		stream2.write(str(jsondata[0].get("financialData").get("revenuePerShare").get("raw") / jsondata[0].get("financialData").get("currentPrice").get("raw"))+ "\n")
	except:
		print("skip")
stream2.close()
'''
	stock[0] = ticker
	stock[1] = jsondata[0].get("financialData").get("returnOnEquity").get("raw")
	stock[2] = jsondata[0].get("financialData").get("revenuePerShare").get("raw") / jsondata[0].get("financialData").get("currentPrice").get("raw")
	list_data.append(stock)
	#market cap todo

print(list_data)
'''
'''
for line in list2:#add from otherlisted
	ticker = line.split('|', 1)[0] # add only first word
'''