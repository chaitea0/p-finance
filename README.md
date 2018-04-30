EECS 280 Project 6: Finance
Project Description:
The end deliverable consists of a python script that pulls stock data from yahoo finance and evaluates each stock based on four different metrics: PEG, ROE, Cash flow, and debt/equity ratio. Between industries, due to notable differences of such metrics, this project is not a stock picker, rather an educational exercise in python programming. 
The project will be divided into three parts:
Stock data download from yahoo finance and insertion into SQL database
Stock data formatting from SQL database into python data structures
Stock data manipulation and evaluation in python
1. Pull stock data from yahoo finance and insert into mySQL database(yahoo.py)
When called, queries yahoo finance with a list of NASDAQ traded stocks and requests data for each. After parsing the data from JSON format, connect to mySQL database and insert data into db table. 
2. Read stock data from mySQL database into python data structures(
When called, take passed parameters required for a SQL server connection and read data from specified database table(see below). Read all rows from the database(shown below), formatting each row into a python list. Each table row and then formatted list will represent one stock. Combine all individual lists into a list of lists to be returned.
Ticker: Letters used on stock exchange to identify corporations.
PEG: Price/Earnings Growth ratio,  calculated as Price/Earnings/Growth
ROE: Return on equity
CF/S: Cash Flow per share, calculated as total cash flow/number of shares outstanding
D/E ratio: Debt Equity ratio, calculated as debt/equity
YTD: Year to date return, calculated as /current price.
Rank: Column of all zeros. 
3. Manipulate stock data in python to evaluate the stocks(
When called, this class will be passed a list of lists, in the format:
[ [ Ticker, PEG, ROE, CF/S, Debt/Equity, YTD ret, 0], [...], [...] … ]
This class will first sort the list along PEG column as the lamda key, looping through the list, adding its rank(place in masterlist) to the sixth value in the individual list. After repeating the process for ROE, CF/S, and Debt/Equity, sort the list along the rank column to rank the stocks in the list by their overall ranking. Finally, print the first twenty elements and their YTD return.
Integration of parts:
Write a main function with a simple print menu that allows the user to:
Update the database 
 Print results of sorted list

