Finance project
_________________________

Chaitea

MRele

Eyjiang
_________________________
EECS 280 Project 6: Finance
The end deliverable consists of a python program that pulls stock data from yahoo finance, and evaluates each stock based on four different metrics*, PEG, ROE, Cash flow, and debt/equity ratio. Due to notable differences of such metrics between industries, this project is not a stock picker rather an educational exercise in python programming. 

The project will be divided into three parts:
Pull stock data from yahoo finance and insert into mySQL database
Read stock data from mySQL database into python data structures
Manipulate stock data in python to evaluate the stocks

1. Pull stock data from yahoo finance and insert into mySQL database(yahoo.py)

2. Read stock data from mySQL database into python data structures(
Take passed parameters required for a SQL server connection, and read data from specified database table(see below). Read all rows from the database, formatting each row into a python list, and then combining all individual lists into a list of lists to be passed on. 
3. Manipulate stock data in python to evaluate the stocks(
will be passed a list of lists, in the format:
[ [ Ticker, PEG, ROE, CF/S, Debt/Equity, YTD ret, 0], [...], [...] … ]
Sort the list along PEG column as the lamda key.
Loop through the list, adding its rank(place in masterlist) to the sixth value in the individual list
Repeat for ROE, CF/S, and Debt/Equity
Sort along rank column for overall rank.
Print first twenty elements and their YTD return.

Integration of parts:
Write a main function with a simple print menu that allows the user to:
Update the database 
 Print results of sorted list

