# Reading-Data-from-sql-in-jupyter
Our first step will be to create a connection to our SQL database. A few common SQL databases used with Python include: 

1. Microsoft SQL Server 
2. Postgres 
3. MySQL 
4. AWS Redshift 
5. AWS Aurora 
6. Oracle DB 
7. Terradata 
8. Db2 Family Many, many others

Each of these databases will require a slightly different setup, and may require credentials (username &amp; password), tokens, or other access requirements. We'll be using sqlite3 to connect to our database, but other connection packages include:

SQLAlchemy (most common)
psycopg2
MySQLdb


There are a number of common paramters that can be used to read in SQL data with formatting:

coerce_float:  Attempt to force numbers into floats
parse_dates:   List of columns to parse as dates
chunksize: Number of rows to include in each chunk
