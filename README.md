Project by jfguan, mrele, eyjiang

info.py is for testing things related to getting info from yahoo finance
	See sample_data.txt for the various data types possible to request
update.py is for testing connecting to the amazon mysql db
yahoo.py is the main function for updating stocks in the database.

notes to self

ticker varchar(6) Primary
roc double
ep double
ranking int(11)
ytd_ret double