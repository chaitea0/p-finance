import MySQLdb
import urllib.request, json 
from yahoo_finance import Share

def insert(db):
	#Text file that stores list of NASDAQ stocks
	stream = open('nasdaqlisted.txt', 'r')
	nasdaq_list = stream.readlines()

	cursor = db.cursor()
	#Clear and add all stocks in NASDAQ listed to DB 
	db.query("TRUNCATE TABLE stock_info")
	for line in nasdaq_list: 
		ticker = line.split('|', 1)[0] #Parse for ticker only
		print(ticker)
		try:
			#Get JSON data from yahoo
			with urllib.request.urlopen("https://query2.finance.yahoo.com/v10/finance/quoteSummary/{}?modules=financialData".format(ticker)) as url:
				data = json.loads(url.read().decode())
				jsondata = data["quoteSummary"]["result"]
			roc = jsondata[0].get("financialData").get("returnOnEquity").get("raw")
			ep = jsondata[0].get("financialData").get("revenuePerShare").get("raw") / jsondata[0].get("financialData").get("currentPrice").get("raw")
			#Cases where no ROC or EP data
			if roc == None:
				roc = 0
			if ep == None:
				ep = 0
			#Insert into db
			cursor.execute("""INSERT INTO stock_info values (%s, %s, %s, %s, %s)""", (ticker, roc, ep, 0, 0))
		except:
			print("Skip or Error")
	db.commit()
	cursor.close()
def update_info(db):
	cursor = db.cursor()
	cursor.execute("SELECT * from stock_info")
	#Update all tickers in db	
	for stock_row in cursor: 
		ticker = stock_row[0]
		print(ticker)
		try:
			with urllib.request.urlopen("https://query2.finance.yahoo.com/v10/finance/quoteSummary/{}?modules=financialData".format(ticker)) as url:
				data = json.loads(url.read().decode())
				jsondata = data["quoteSummary"]["result"]
			roc = jsondata[0].get("financialData").get("returnOnEquity").get("raw")
			ep = jsondata[0].get("financialData").get("revenuePerShare").get("raw") / jsondata[0].get("financialData").get("currentPrice").get("raw")
			#Cases where no ROC or EP data
			if roc == None:
				roc = 0
			if ep == None:
				ep = 0
			cursor.execute("""UPDATE stock_info SET ROC = %s, EP = %s WHERE ticker = %s""", (roc, ep, ticker) )
		except:
			print("Skip or Error")
	db.commit()
	cursor.close()

def calc_ranks(db):
	
	#Clear previous rankings
	cursor = db.cursor()
	cursor.execute("UPDATE stock_info set Ranking = 0")
	
	#Update rankings
	cursor.execute("SELECT * from stock_info ORDER BY ROC DESC")
	calc_rank_helper(db, cursor)
	cursor.execute("SELECT * from stock_info ORDER BY EP DESC")
	calc_rank_helper(db, cursor)

	cursor.close()

def calc_rank_helper(db, cursor):
	rank = 0;
	#For each stock, add its relative ranking to its overall ranking score
	for stock_row in cursor: 
		ticker = stock_row[0] 
		print(ticker)
		cursor.execute("""UPDATE stock_info SET Ranking = %s WHERE ticker = %s""", (rank + stock_row[3], ticker) )
		rank += 1
	db.commit()

def print_info(db):
	cursor = db.cursor()
	#Select top 10 stocks
	cursor.execute("""SELECT * from stock_info ORDER BY Ranking LIMIT 10""")
	for stock_row in cursor:
		print(stock_row)
	cursor.close()

